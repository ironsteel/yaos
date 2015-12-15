from ironsteel/django-1.4

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install libmysqlclient-dev python-dev


RUN mkdir /code
COPY ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
EXPOSE 8000
CMD ["/code/manage.py", "runserver", "0.0.0.0:8000"]
