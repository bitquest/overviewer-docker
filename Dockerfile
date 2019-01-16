FROM debian:jessie
RUN sed -i 's%httpredir.debian.org%ftp.debian.org%' /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get -y install build-essential python-imaging python-dev python-numpy git nginx imagemagick
WORKDIR /overviewer
RUN git clone --single-branch --branch minecraft113 https://github.com/overviewer/Minecraft-Overviewer.git /overviewer
RUN python setup.py build
RUN chmod +x /overviewer/overviewer.py
# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Set the default command to execute
# when creating a new container
RUN apt-get install -y wget
RUN mkdir -p /root/.minecraft/versions/1.13.2/
RUN wget https://launcher.mojang.com/v1/objects/30bfe37a8db404db11c7edf02cb5165817afb4d9/client.jar -O ~/.minecraft/versions/1.13.2/1.13.2.jar

RUN rm -rf /var/www/html/*
COPY mini.py /overviewer/
COPY shot.sh /overviewer/
RUN chmod +x /overviewer/shot.sh
COPY config.py /overviewer/
CMD service nginx start
