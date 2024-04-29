FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY django_weather_app/settings.py django_weather_app/settings.py

EXPOSE 8000

#CMD python manage.py runserver 0.0.0.0:8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "django_weather_app.wsgi:application"]
