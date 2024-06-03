FROM python:3.9-alpine3.20

WORKDIR /HelloWorld
COPY requirements.txt /HelloWorld
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /HelloWorld
EXPOSE 5000