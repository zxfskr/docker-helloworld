FROM ossrs/srs:3

WORKDIR /usr/local/srs

RUN yum -y install logrotate

# COPY /config/logrotate-srs /etc/logrotate.d/logrotate-srs

CMD ["./objs/srs", "-c", "conf/srs.conf"]