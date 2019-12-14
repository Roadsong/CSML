FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk cmake make vim moreutils python3

RUN wget http://dlib.net/files/dlib-19.18.tar.bz2 \
	&& tar -xvf dlib-19.18.tar.bz2 \
	&& rm dlib-19.18.tar.bz2 \
	&& cd dlib-19.18 \
	&& cd examples \
	&& mkdir build \
	&& cd build \
	&& cmake .. \
	&& cmake --build . --config Release \
	&& cd / \
	&& mkdir results \
	&& cd /results \
	&& mkdir dlib \
	&& mkdir /app_code \
	&& wget -P /app_code https://raw.githubusercontent.com/Roadsong/CSML/master/code/app/dlib_start.sh

WORKDIR /dlib-19.18/examples/build