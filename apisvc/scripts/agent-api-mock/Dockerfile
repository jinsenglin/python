FROM jimlintw/base:python-alpine

RUN apk --update add py-pip && \
    rm -rf /var/cache/apk/* /tmp/* /var/tmp/*

RUN pip install flask==0.12.2
