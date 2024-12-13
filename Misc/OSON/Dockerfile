FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    socat \
    python3 

RUN useradd -UM usrsentrix

COPY src/chall.py /home/usrsentrix/chall.py
COPY run.sh /home/usrsentrix/run.sh
RUN chmod +x /home/usrsentrix/chall.py


RUN chmod 655 /home/usrsentrix/run.sh
USER usrsentrix

WORKDIR /home/usrsentrix
EXPOSE 20037
CMD /home/usrsentrix/run.sh
