FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    socat \
    python3 \
    less
RUN useradd -UM repjail

COPY src/chall.py /home/repjail/chall.py
COPY flag.txt /home/repjail/flag.txt
COPY run.sh /home/repjail/run.sh
RUN chown repjail:repjail /home/repjail/flag.txt && chmod 644 /home/repjail/flag.txt
RUN chown repjail:repjail /home/repjail/flag.txt && chmod 644 /home/repjail/flag.txt && \
    chmod +x /home/repjail/chall.py


RUN chmod 655 /home/repjail/run.sh
USER repjail

WORKDIR /home/repjail
EXPOSE 20037
CMD /home/repjail/run.sh
