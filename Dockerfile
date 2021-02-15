FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install postgresql-client python3 python3-pip -y
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
