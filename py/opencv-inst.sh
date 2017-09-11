#!/usr/bin/env bash
set -eu

PYTHON_VERSION_MAJOR="3"
PYTHON_VERSION_MINOR="5"
OCV_VERSION="3.3.0"

OCV_SRC="https://github.com/Itseez/opencv/archive/${OCV_VERSION}.zip"
OCV_C_SRC="https://github.com/Itseez/opencv_contrib/archive/${OCV_VERSION}.zip"
OCV_DIR="${HOME}/OpenCV"

DEPS=""
# Tools
DEPS+=" build-essential cmake pkg-config"
# Photo deps
DEPS+=" libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev"
# Video deps
DEPS+=" libavcodec-dev libavformat-dev libswscale-dev libv4l-dev"
DEPS+=" libxvidcore-dev libx264-dev"
# GUI deps
DEPS+=" libgtk-3-dev"
# Optimization libs
DEPS+=" libatlas-base-dev gfortran"
# Python dev headers
DEPS+=" python2.7-dev python3.5-dev"


echo ">>> Updating..."
sudo apt-get update
sudo apt-get upgrade

echo ">>> Installing dependencies..."
sudo apt-get install -y ${DEPS}

echo ">>> Creating source/build directory..."
mkdir -p ${OCV_DIR}
cd ${OCV_DIR}

echo ">>> Downloading source..."
wget -O opencv.zip ${OCV_SRC}
unzip opencv.zip
wget -O opencv_contrib.zip ${OCV_C_SRC}
unzip opencv_contrib.zip

echo ">>> Installing and configuring Virtual Environment..."
sudo pip install virtualenv virtualenvwrapper
echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
# Create Python3 virtual environment
mkvirtualenv cv -p python3
#workon cv # if already created
# Install NumPy in virtual env.
pip install numpy

echo ">>> Configuring and building OpenCV..."
cd ${OCV_DIR}/opencv-${OCV_VERSION}/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_EXTRA_MODULES_PATH=${OCV_DIR}/opencv_contrib-${OCV_VERSION}/modules \
    -D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
    -D BUILD_EXAMPLES=ON ..
make -j4

echo ">>> Installing OpenCV..."
sudo make install
sudo ldconfig

echo ">>> Fixing Python 3 lib name issue..."
cd /usr/local/lib/python3.5/site-packages/
# Symlink or rename:
sudo ln -s cv2.cpython-35m-x86_64-linux-gnu.so cv2.so # symlink
# sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so # rename

echo "Symlink OpenCV bindings to Virtual Environment..."
cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
ln -s /usr/local/lib/python3.5/site-packages/cv2.so cv2.so

echo ">>> DONE"



