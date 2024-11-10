from datetime import datetime
import swisseph as swe

def calculate_planet_positions(birth_date, birth_time, latitude, longitude):
    birth_datetime = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    year, month, day = birth_datetime.year, birth_datetime.month, birth_datetime.day
    hour, minute = birth_datetime.hour, birth_datetime.minute

    swe.set_ephe_path('/path/to/ephemeris/')  # Replace with your ephemeris path
    jd = swe.julday(year, month, day, hour + minute / 60)

    planets = {
        "Sun": swe.SUN, "Moon": swe.MOON, "Mercury": swe.MERCURY, "Venus": swe.VENUS,
        "Mars": swe.MARS, "Jupiter": swe.JUPITER, "Saturn": swe.SATURN,
        "Uranus": swe.URANUS, "Neptune": swe.NEPTUNE, "Pluto": swe.PLUTO
    }

    positions = {}
    aspects = {}
    for planet1, code1 in planets.items():
        planet_pos1 = swe.calc_ut(jd, code1)[0][0]
        sign1 = get_zodiac_sign(planet_pos1)
        positions[planet1] = {"position": planet_pos1, "sign": sign1}

        for planet2, code2 in planets.items():
            if planet1 != planet2:
                planet_pos2 = swe.calc_ut(jd, code2)[0][0]
                angle = abs(planet_pos1 - planet_pos2)
                aspect_type = get_aspect_type(angle)
                aspects[f"{planet1}-{planet2}"] = aspect_type

    ascendant = swe.houses(jd, latitude, longitude, b'A')[0][0]
    asc_sign = get_zodiac_sign(ascendant)
    positions["Ascendant"] = {"position": ascendant, "sign": asc_sign}

    return positions, aspects

def get_zodiac_sign(degree):
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    sign_index = int((degree % 360) // 30)
    return signs[sign_index % 12]

def get_aspect_type(angle):
    if angle < 10 or angle > 350:
        return "Conjunction"
    elif 170 < angle < 190:
        return "Opposition"
    elif 270 < angle < 290 or 90 < angle < 110:
        return "Square"
    elif 120 < angle < 140 or 240 < angle < 260:
        return "Trine"
    elif 50 < angle < 70 or 290 < angle < 310:
        return "Sextile"
    else:
        return "No aspect"

def suggest_careers(positions):
    career_database = {
    "Leadership": {
        "keywords": ["leader", "management", "entrepreneur", "CEO", "executive", "visionary"],
        "interpretation": "Ideal for those with strong Sun placements or prominent fire signs."
    },
    "Creative Arts": {
        "keywords": ["artist", "musician", "writer", "actor", "designer", "painter", "sculptor"],
        "interpretation": "Suitable for individuals with Moon in Pisces or Venus in Libra."
    },
    "Technology": {
        "keywords": ["developer", "engineer", "IT specialist", "data scientist", "software engineer", "network administrator", "AI researcher"],
        "interpretation": "Great for those with strong Mercury or Uranus influences."
    },
    "Education": {
        "keywords": ["teacher", "trainer", "mentor", "professor", "educator", "counselor", "tutor"],
        "interpretation": "Ideal for individuals with Jupiter in Sagittarius or the 9th house."
    },
    "Healthcare": {
        "keywords": ["doctor", "nurse", "therapist", "health coach", "pharmacist", "dentist", "surgeon", "veterinarian", "naturopath"],
        "interpretation": "Best suited for Moon in Cancer or Scorpio placements."
    },
    "Finance": {
        "keywords": ["accountant", "financial analyst", "banker", "investment manager", "tax advisor", "auditor"],
        "interpretation": "Strong placements in Taurus or the 2nd house favor financial careers."
    },
    "Sports": {
        "keywords": ["athlete", "coach", "sports manager", "personal trainer", "cricketer", "football player", "basketball player", "sports therapist", "eSports player"],
        "interpretation": "Mars in the 1st or 5th house indicates strong sports potential."
    },
    "Politics": {
        "keywords": ["politician", "activist", "policy maker", "government official", "diplomat", "lobbyist"],
        "interpretation": "Influential placements in the 10th house or strong Sun/Moon aspects can lead to a career in politics."
    },
    "Social Services": {
        "keywords": ["social worker", "counselor", "nonprofit manager", "community organizer", "human rights activist", "mental health specialist"],
        "interpretation": "Prominent placements in the 4th or 12th house indicate a calling to serve others."
    },
    "Entrepreneurship": {
        "keywords": ["startup founder", "business consultant", "freelancer", "venture capitalist", "angel investor", "small business owner"],
        "interpretation": "Strong placements in Aries or the 1st house favor independent ventures."
    },
    "Research": {
        "keywords": ["scientist", "researcher", "analyst", "data analyst", "lab technician", "clinical researcher"],
        "interpretation": "Prominent placements in Virgo or Scorpio support investigative careers."
    },
    "Writing": {
        "keywords": ["journalist", "author", "editor", "blogger", "content creator", "poet", "playwright"],
        "interpretation": "Strong Mercury influences often lead to success in writing careers."
    },
    "Hospitality": {
        "keywords": ["chef", "hotel manager", "event planner", "travel consultant", "tour guide", "restaurant owner"],
        "interpretation": "Venus in the 4th or 5th house suggests a passion for service and enjoyment."
    },
    "Media": {
        "keywords": ["producer", "director", "photographer", "videographer", "broadcast journalist", "radio host", "cinematographer"],
        "interpretation": "Strong placements in Leo or aspects to Neptune enhance creative media pursuits."
    },
    "Law": {
        "keywords": ["lawyer", "legal consultant", "judge", "paralegal", "litigator", "corporate lawyer", "criminal lawyer"],
        "interpretation": "Libra or Saturn in the 7th house supports careers in law."
    },
    "Engineering": {
        "keywords": ["civil engineer", "mechanical engineer", "electrical engineer", "aerospace engineer", "chemical engineer", "structural engineer"],
        "interpretation": "Strong placements in Capricorn or Uranus favor technical fields."
    },
    "Science and Technology": {
        "keywords": ["biotechnologist", "computer scientist", "environmental scientist", "AI researcher", "robotics engineer", "nanotechnologist"],
        "interpretation": "Prominent placements in Aquarius support cutting-edge scientific careers."
    },
    "Fashion": {
        "keywords": ["fashion designer", "stylist", "model", "merchandiser", "fashion blogger", "makeup artist"],
        "interpretation": "Venus in Taurus or Libra enhances fashion and aesthetics."
    },
    "Marketing": {
        "keywords": ["marketing specialist", "advertising executive", "brand manager", "content strategist", "PR consultant", "event marketer"],
        "interpretation": "Strong Mercury and Venus influences favor creative marketing roles."
    },
    "Real Estate": {
        "keywords": ["real estate agent", "property manager", "real estate developer", "architect", "landscaper", "urban planner"],
        "interpretation": "Strong placements in Cancer or the 4th house indicate potential in real estate."
    },
    "Human Resources": {
        "keywords": ["HR manager", "recruiter", "organizational development", "talent acquisition", "employee relations specialist"],
        "interpretation": "Strong Venus or Jupiter placements support careers in HR."
    },
    "Information Technology": {
        "keywords": ["system analyst", "IT support specialist", "cybersecurity expert", "network administrator", "software tester", "cloud engineer"],
        "interpretation": "Strong placements in Gemini or Aquarius support IT careers."
    },
    "Public Relations": {
        "keywords": ["PR manager", "communications director", "public affairs specialist", "media relations manager", "brand ambassador"],
        "interpretation": "Strong Mercury placements enhance public relations skills."
    },
    "Transportation": {
        "keywords": ["pilot", "logistics manager", "transportation planner", "cargo manager", "flight attendant", "ship captain"],
        "interpretation": "Strong placements in Sagittarius or the 9th house suggest careers in transportation."
    },
    "Non-Profit Sector": {
        "keywords": ["nonprofit director", "philanthropist", "advocacy coordinator", "charity organizer", "social entrepreneur"],
        "interpretation": "Prominent placements in the 11th house indicate a calling to support social causes."
    },
    "Cybersecurity": {
        "keywords": ["cybersecurity analyst", "information security manager", "penetration tester", "network security specialist", "ethical hacker"],
        "interpretation": "Strong placements in Scorpio or with Uranus involved support careers in cybersecurity."
    },
    "Digital Marketing": {
        "keywords": ["SEO specialist", "content strategist", "social media manager", "digital marketing analyst", "influencer"],
        "interpretation": "Strong Mercury influences favor careers in digital marketing."
    },
    "Art Therapy": {
        "keywords": ["art therapist", "creative arts therapist", "music therapist", "dance movement therapist"],
        "interpretation": "Prominent placements in the 5th house support therapeutic careers in the arts."
    },
    "Gaming": {
        "keywords": ["game designer", "game developer", "eSports manager", "game tester", "streamer"],
        "interpretation": "Strong placements in Leo or Pisces indicate potential in the gaming industry."
    },
    "Criminal Justice": {
        "keywords": ["detective", "police officer", "criminologist", "forensic scientist", "corrections officer"],
        "interpretation": "Strong Mars or Pluto influences may point toward careers in law enforcement or criminology."
    },
    "Journalism": {
        "keywords": ["reporter", "news anchor", "investigative journalist", "editor", "photojournalist", "columnist"],
        "interpretation": "Strong Mercury or Neptune placements favor journalism."
    },
    "Performing Arts": {
        "keywords": ["dancer", "theater actor", "singer", "comedian", "ballet dancer", "opera singer"],
        "interpretation": "Individuals with prominent Neptune, Venus, or Leo placements often excel in performing arts."
    },
    "Science & Environment": {
        "keywords": ["ecologist", "marine biologist", "environmental consultant", "geologist", "climate change advocate", "sustainability expert"],
        "interpretation": "Strong placements in Virgo, Capricorn, or Aquarius may favor environmental sciences."
    },
    "Hospital Administration": {
        "keywords": ["hospital manager", "health services administrator", "medical office manager", "clinical operations manager"],
        "interpretation": "Strong Mercury or Saturn influences may support a career in healthcare management."
    },
    "Construction and Trades": {
        "keywords": ["construction manager", "architect", "electrician", "plumber", "carpenter", "builder"],
        "interpretation": "Mars, Saturn, or strong 10th house placements favor practical and hands-on careers."
    }
}

    suggested_careers = []
    sun_sign = positions['Sun']['sign']
    moon_sign = positions['Moon']['sign']
    ascendant_sign = positions['Ascendant']['sign']

    # for career, details in career_database.items():
    #     if sun_sign in details['interpretation']:
    #         suggested_careers.append({
    #             'Career': career,
    #             'Keywords': details['keywords'],
    #             'Interpretation': details['interpretation']
    #         })

    # unique_suggestions = []
    # for suggestion in suggested_careers:
    #     if suggestion not in unique_suggestions:
    #         unique_suggestions.append(suggestion)

    # return unique_suggestions
    # Match Sun sign
    for career, details in career_database.items():
        if sun_sign in details['interpretation']:
            suggested_careers.append({
                'Career': career,
                'Keywords': details['keywords'],
                'Interpretation': details['interpretation']
            })

    # Match Moon sign
    for career, details in career_database.items():
        if moon_sign in details['interpretation']:
            suggested_careers.append({
                'Career': career,
                'Keywords': details['keywords'],
                'Interpretation': details['interpretation']
            })

    # Match Ascendant sign
    for career, details in career_database.items():
        if ascendant_sign in details['interpretation']:
            suggested_careers.append({
                'Career': career,
                'Keywords': details['keywords'],
                'Interpretation': details['interpretation']
            })

    # Remove duplicates
    unique_suggestions = []
    for suggestion in suggested_careers:
        if suggestion not in unique_suggestions:
            unique_suggestions.append(suggestion)

    return unique_suggestions


def get_personality_insights(positions):
    insights = {}
    ascendant_sign = positions['Ascendant']['sign']
    sun_sign = positions['Sun']['sign']
    moon_sign = positions['Moon']['sign']

    insights['strengths'] = get_strengths(sun_sign, ascendant_sign, moon_sign)
    insights['weaknesses'] = get_weaknesses(moon_sign, ascendant_sign, sun_sign)
    insights['emotional_intelligence'] = get_emotional_intelligence(moon_sign, ascendant_sign)
    insights['learning_style'] = get_learning_style(sun_sign, ascendant_sign)
    insights['conflict_resolution'] = get_conflict_resolution(ascendant_sign, sun_sign)
    insights['life_purpose'] = get_life_purpose(sun_sign, ascendant_sign, moon_sign)

    return insights

def get_strengths(sun_sign, ascendant_sign, moon_sign):
    strengths = {
        'Sun': {"Leo": "Confident, passionate, generous", "Virgo": "Analytical, practical, precise"},
        'Ascendant': {"Aries": "Adventurous, confident", "Capricorn": "Disciplined, responsible"},
        'Moon': {"Cancer": "Empathetic, nurturing", "Gemini": "Adaptable, communicative"}
    }
    sun_strengths = strengths['Sun'].get(sun_sign, '')
    ascendant_strengths = strengths['Ascendant'].get(ascendant_sign, '')
    moon_strengths = strengths['Moon'].get(moon_sign, '')
    return f"Sun: {sun_strengths}, Ascendant: {ascendant_strengths}, Moon: {moon_strengths}"

def get_weaknesses(moon_sign, ascendant_sign, sun_sign):
    weaknesses = {
        'Moon': {"Cancer": "Emotionally sensitive", "Gemini": "Restless"},
        'Ascendant': {"Aries": "Impulsive", "Capricorn": "Overly critical"},
        'Sun': {"Leo": "Prideful", "Taurus": "Stubborn"}
    }
    moon_weaknesses = weaknesses['Moon'].get(moon_sign, '')
    ascendant_weaknesses = weaknesses['Ascendant'].get(ascendant_sign, '')
    sun_weaknesses = weaknesses['Sun'].get(sun_sign, '')
    return f"Moon: {moon_weaknesses}, Ascendant: {ascendant_weaknesses}, Sun: {sun_weaknesses}"

def get_emotional_intelligence(moon_sign, ascendant_sign):
    emotional_intelligence = {
        'Moon': {"Cancer": "Empathetic", "Gemini": "Adaptable"},
        'Ascendant': {"Cancer": "Emotionally intelligent", "Libra": "Diplomatic"}
    }
    moon_emotional_intelligence = emotional_intelligence['Moon'].get(moon_sign, '')
    ascendant_emotional_intelligence = emotional_intelligence['Ascendant'].get(ascendant_sign, '')
    return f"Moon: {moon_emotional_intelligence}, Ascendant: {ascendant_emotional_intelligence}"

def get_learning_style(sun_sign, ascendant_sign):
    learning_styles = {
        'Sun': {"Leo": "Visual, hands-on", "Virgo": "Analytical"},
        'Ascendant': {"Aries": "Hands-on", "Capricorn": "Structured"}
    }
    sun_learning_style = learning_styles['Sun'].get(sun_sign, '')
    ascendant_learning_style = learning_styles['Ascendant'].get(ascendant_sign, '')
    return f"Sun: {sun_learning_style}, Ascendant: {ascendant_learning_style}"

def get_conflict_resolution(ascendant_sign, sun_sign):
    conflict_resolution = {
        'Ascendant': {"Aries": "Direct", "Capricorn": "Strategic"},
        'Sun': {"Leo": "Confident", "Taurus": "Practical"}
    }
    ascendant_conflict_resolution = conflict_resolution['Ascendant'].get(ascendant_sign, '')
    sun_conflict_resolution = conflict_resolution['Sun'].get(sun_sign, '')
    return f"Ascendant: {ascendant_conflict_resolution}, Sun: {sun_conflict_resolution}"

def get_life_purpose(sun_sign, ascendant_sign, moon_sign):
    life_purpose = {
        'Sun': {"Leo": "Self-expression", "Virgo": "Service"},
        'Ascendant': {"Aries": "Adventure", "Capricorn": "Ambition"},
        'Moon': {"Cancer": "Family", "Gemini": "Curiosity"}
    }
    sun_life_purpose = life_purpose['Sun'].get(sun_sign, '')
    ascendant_life_purpose = life_purpose['Ascendant'].get(ascendant_sign, '')
    moon_life_purpose = life_purpose['Moon'].get(moon_sign, '')
    return f"Sun: {sun_life_purpose}, Ascendant: {ascendant_life_purpose}, Moon: {moon_life_purpose}"

# get house positions
def get_house_positions(positions):
    houses = {}
    for planet, details in positions.items():
        if planet != "Ascendant":
            house_number = get_house_number(details['position'])
            houses[house_number] = details
    return houses

# Helper function for house number calculation
def get_house_number(degree):
    return int((degree % 360) // 30) + 1

def generate_birth_chart(birth_date, birth_time, latitude, longitude):
    positions, aspects = calculate_planet_positions(birth_date, birth_time, latitude, longitude)
    career_suggestions = suggest_careers(positions)
    house_positions = get_house_positions(positions)
    personality_insights = get_personality_insights(positions)
    return {
        "positions": positions,
        "aspects": aspects,
        "career_suggestions": career_suggestions,
        "house_positions": house_positions,
        "personality_insights": personality_insights
    }
