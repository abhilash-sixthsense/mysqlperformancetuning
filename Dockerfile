# FROM python:3.9-buster
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_14.x |  bash -
RUN apt-get install -y nodejs 
ENV TZ=Asia/Kolkata
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata -y
RUN DEBIAN_FRONTEND="noninteractive" apt-get install libmysqlclient-dev -y
RUN apt-get install -y  python3.9-dev python3-pip
RUN apt-get install python3.9-venv -y
RUN python3.9 -m venv /root/venv
ENV PATH="/root/venv/bin:$PATH"
COPY requirements.txt .
RUN apt-get install gcc libffi-dev -y
RUN pip install -U wheel pip 
RUN pip install -r requirements.txt
COPY . /root/app
RUN apt-get install git gitk -y
RUN apt-get install build-essential -y

