# Start from a fedora
FROM fedora

RUN dnf -y update

# Install python
RUN dnf -y install python

# For ifconfig
RUN dnf -y install net-tools

# OpenCV dependences (core)
RUN dnf -y install cmake
RUN dnf -y install python-devel numpy
RUN dnf -y install gcc gcc-c++

# OpenCV dependences (GTK)
RUN dnf -y install gtk2-devel libdc1394-devel libv4l-devel gstreamer-plugins-base-devel

# OpenCV dependences (image formats)
RUN dnf -y install libpng-devel libjpeg-turbo-devel jasper-devel openexr-devel libtiff-devel libwebp-devel

# OpenCV dependences (optimized maths and other yerbas)
RUN dnf -y install tbb-devel eigen3-devel python-sphinx texlive

WORKDIR /raspy

# OpenCV sources
ADD opencv-3.2.0 opencv
ADD opencv_contrib-3.2.0 opencv_contrib

# Compile OpenCV
RUN cd opencv && mkdir build
RUN cd opencv/build && cmake -D CMAKE_BUILD_TYPE=RELEASE \
                             -D CMAKE_INSTALL_PREFIX=/usr/local \
                             -D WITH_TBB=ON \
                             -D WITH_EIGEN=ON \
                             -D BUILD_DOCS=ON \
                             -D BUILD_TESTS=OFF \
                             -D BUILD_PERF_TESTS=OFF \
                             -D BUILD_EXAMPLES=OFF \
                             -D WITH_OPENCL=OFF \
                             -D WITH_CUDA=OFF \
                             -D BUILD_opencv_gpu=OFF \
                             -D BUILD_opencv_gpuarithm=OFF \
                             -D BUILD_opencv_gpubgsegm=OFF \
                             -D BUILD_opencv_gpucodec=OFF \
                             -D BUILD_opencv_gpufeatures2d=OFF \
                             -D BUILD_opencv_gpufilters=OFF \
                             -D BUILD_opencv_gpuimgproc=OFF \
                             -D BUILD_opencv_gpulegacy=OFF \
                             -D BUILD_opencv_gpuoptflow=OFF \
                             -D BUILD_opencv_gpustereo=OFF \
                             -D BUILD_opencv_gpuwarping=OFF \
						     -D INSTALL_PYTHON_EXAMPLES=ON \
						     -D INSTALL_C_EXAMPLES=OFF \
                             -D OPENCV_EXTRA_MODULES_PATH=/raspy/opencv_contrib/modules \
                             -D PYTHON_EXECUTABLE=/usr/bin/python \
                             .. && make

# Install OpenCV
RUN cd opencv/build && make install
RUN export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python2.7/site-packages
RUN ldconfig && ln -s /usr/local/lib/python2.7/site-packages/cv2.so cv2.so

EXPOSE 8000
