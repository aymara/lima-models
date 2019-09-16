cmake_minimum_required(VERSION 3.12.1)

add_subdirectory(ewt)

install(
    FILES
        cc.en.300.bin
    COMPONENT
        morphosyntax-eng.ud
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/eng.ud/
)

cpack_add_component(morphosyntax-eng.ud
    DISPLAY_NAME
        "UD English / FastText Embeddings"
    GROUP
        English
)

