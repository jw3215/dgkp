FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1234"

RUN git clone https://github.com/jw3215/dgkp.git

WORKDIR /home/dgkp/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --settings=dgkp.settings.deploy --noinput && python manage.py migrate --settings=dgkp.settings.deploy && gunicorn dgkp.wsgi --env DJANGO_SETTINGS_MODULE=dgkp.settings.deploy --bind 0.0.0.0:8000"]