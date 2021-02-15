FROM ubuntu:20.04
RUN apt update && apt upgrade -y
RUN apt postgresql-client -y 
