mkdir -p TensorFlowTokenizer/ud
mkdir -p TensorFlowMorphoSyntax/ud
mkdir -p TensorFlowLemmatizer/ud

cat c2lc.txt | perl scripts/generate_tokenizer_cmake.pl \
    > TensorFlowTokenizer/ud/CMakeLists.txt

cat c2lc.txt | perl scripts/generate_morphosyntax_cmake.pl \
    > TensorFlowMorphoSyntax/ud/CMakeLists.txt

cat c2lc.txt | perl scripts/generate_lemmatizer_cmake.pl \
    > TensorFlowLemmatizer/ud/CMakeLists.txt

rm -rf build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
cpack
