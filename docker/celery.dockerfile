FROM ubuntu:20.04

ENV PATH = "/script:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt install -y gcc
RUN apt install -y python3.9-dev
RUN apt install -y python3.9-venv
RUN apt install -y python3.9
RUN apt-get install -y python3.9-distutils
RUN apt install -y python3-pip
RUN apt install -y libcap-dev
RUN apt install make
RUN pip install --upgrade pip

RUN mkdir /app
COPY /src /app
RUN mkdir /app/staticfiles
COPY /script /app/script
RUN chmod +x /app/script/*

WORKDIR /app

COPY django.env /app
RUN python3.9 -m venv venv
RUN . venv/bin/activate
RUN pip install -r /requirements.txt
RUN chmod +x script/entrypoint.sh

USER root

CMD ["/script/entrypoint.sh"]
