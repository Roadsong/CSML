FROM alpine:3.10

RUN apk update \
	&& apk add --no-cache gtk+2.0 gtk+2.0-dev pkgconfig python python-dev py-numpy \ 
	py-numpy-dev py2-numpy py-numpy-f2py py2-numpy-f2py ffmpeg ffmpeg-libs \
	ffmpeg-dev zip make cmake gcc g++ vim
RUN cd /usr \
	&& mkdir src \
	&& cd src \
	&& mkdir app \
	&& cd app \
	&& wget https://github.com/opencv/opencv/archive/3.4.1.zip \
	&& unzip 3.4.1.zip \
	&& rm 3.4.1.zip \
	&& cd /usr/src/app/opencv-3.4.1/modules/python/src2/ \
	&& rm cv2.cpp \
	&& wget https://raw.githubusercontent.com/Roadsong/CSML/master/opencv/cv2.cpp \
	&& cd /usr/src/app/opencv-3.4.1/ \
	&& mkdir build \
	&& cd build \
	&& cmake -D CMAKE=BUILD_TYPE=Release -D BUILD_TESTS=ON -D BUILD_EXAMPLES=ON \ 
	-D ENABLE_PRECOMPILED_HEADERS=OFF -D CMAKE_INSTALL_PREFIX=/usr/local ./.. \
	&& make -j$(nproc) \
	&& make install \
	&& cp -r /usr/local/lib/python2.7/site-packages/cv2.so \
	/usr/lib/python2.7/site-packages/ \
	&& cp -r /usr/local/lib/python3.7/site-packages/cv2.cpython-37m-x86_64-linux-gnu.so \
	/usr/lib/python3.7/site-packages/ \
	&& cd /usr/src/app/ \
	&& wget https://github.com/opencv/opencv_extra/archive/3.4.1.zip \
	&& unzip 3.4.1.zip \
	&& rm 3.4.1.zip
	

ENV OPENCV_BUILD_DIR /usr/src/app/opencv-3.4.1/build

ENV OPENCV_TEST_DATA_PATH /usr/src/app/opencv_extra-3.4.1/testdata

WORKDIR /usr/src/app/
