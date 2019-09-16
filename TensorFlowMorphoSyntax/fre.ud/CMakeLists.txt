cmake_minimum_required(VERSION 3.12.1)

add_subdirectory(sequoia)

install(
    FILES
        cc.fr.300.bin
    COMPONENT
        morphosyntax-fre.ud
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/fre.ud/
)

cpack_add_component(morphosyntax-fre.ud
    DISPLAY_NAME
        "UD French / FastText Embeddings"
    GROUP
        French
)

