FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat patchelf
RUN useradd -UM part2

COPY p2 /home/part2/p2
COPY flag.txt /home/part2/flag.txt
COPY run.sh /home/part2/run.sh
RUN chown part2:part2 /home/part2/flag.txt && chmod 644 /home/part2/flag.txt
RUN chown part2:part2 /home/part2/flag.txt && chmod 644 /home/part2/flag.txt && \
    chmod +x /home/part2/p2

# RUN patchelf --set-interpreter /home/amnesia/ld-linux.so /home/amnesia/amnesia && \
# 	patchelf --replace-needed libc.so.6 ./libc.so.6 /home/amnesia/amnesia && \
#     patchelf --set-rpath /home/amnesia /home/amnesia/amnesia

RUN chmod 655 /home/part2/run.sh
USER part2

WORKDIR /home/part2

CMD /home/part2/run.sh
