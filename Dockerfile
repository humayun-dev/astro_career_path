FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=production  # Set to production for deployment

EXPOSE 5000


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
