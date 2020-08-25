FROM python:3.7


RUN apt-get update
RUN apt-get install -y \
        libatlas-base-dev gfortran nginx \
	&& apt-get clean \
        && pip3 install -U uwsgi \
        && useradd --no-create-home nginx \
        && rm /etc/nginx/sites-enabled/default \
        && rm -r /root/.cache \
        && rm -rf /var/lib/apt/lists/*

COPY uwsgi.ini /etc/uwsgi/
COPY nginx_service.conf /etc/nginx/conf.d/
COPY ssl /etc/ssl

WORKDIR /project

CMD ["/bin/bash", "-c", "chown -R www-data.www-data /etc/ssl /project && pip3 install -U -r requirements.txt && service nginx start && /usr/local/bin/uwsgi --ini /etc/uwsgi/uwsgi.ini"]

COPY /app /project
