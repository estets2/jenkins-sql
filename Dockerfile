FROM ubuntu:20.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install postgresql-client python3 python3-pip python3-dev -y
RUN apt-get clean && rm -rf /var/lib/apt/lists /var/cache/apt
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY *.py /
