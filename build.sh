rm -rf build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
cpack
