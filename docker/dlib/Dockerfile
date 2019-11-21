FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk cmake make

RUN wget http://dlib.net/files/dlib-19.18.tar.bz2 \
	&& tar -xvf dlib-19.18.tar.bz2 \
	&& rm dlib-19.18.tar.bz2 \
	&& cd dlib-19.18 \
	&& cd examples \
	&& mkdir build \
	&& cd build \
	&& cmake .. \
	&& cmake --build . --config Release

WORKDIR /dlib-19.18/examples/build