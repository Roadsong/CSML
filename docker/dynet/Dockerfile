FROM alpine:3.10

RUN apk update && apk add --no-cache alpine-sdk cmake make mercurial vim moreutils python3
RUN wget https://github.com/clab/dynet/archive/2.1.zip \
	&& hg clone https://bitbucket.org/eigen/eigen/ -r b2e267d \
	&& unzip 2.1.zip \
	&& rm 2.1.zip \ 
	&& cd dynet-2.1 \
	&& mkdir build \
	&& cd build \
	&& cmake .. -DEIGEN3_INCLUDE_DIR=/eigen -DENABLE_CPP_EXAMPLES=ON \
	&& make -j$(nproc) && make install \
	&& cd / \
	&& mkdir results \
	&& cd /results \
	&& mkdir dynet

WORKDIR /dynet-2.1/build/examples