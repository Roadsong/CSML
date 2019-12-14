FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk python3 vim moreutils

RUN cd / \
    && mkdir results \
    && mkdir /management_code \
	&& wget -P /management_code https://raw.githubusercontent.com/Roadsong/CSML/master/code/management/management_start.sh