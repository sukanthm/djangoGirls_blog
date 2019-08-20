FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev vim -y
ADD ./ /code/
CMD python manage.py makemigrations \
    && python manage.py migrate \
    && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', '', 'hfmehfme')" | python manage.py shell \
    && python manage.py runserver 0.0.0.0:80