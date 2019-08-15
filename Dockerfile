FROM python:3.7
MAINTAINER k1m0ch1
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove && \
    apt-get autoclean

RUN apt-get install -y \
    nano \
    git

RUN git clone \
    https://github.com/rizkygtpens/perpustakaan.git \
    /var/www/apps/

WORKDIR /var/www/apps/

RUN pip install --no-cache-dir -r requirement.txt
EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate

STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]