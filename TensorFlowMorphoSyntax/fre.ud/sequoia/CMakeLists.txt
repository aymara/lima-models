cmake_minimum_required(VERSION 3.12.1)

install(
    FILES
        UD_French-Sequoia.conf
        UD_French-Sequoia.model
    COMPONENT
        morphosyntax-fre.ud-sequoia
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/fre.ud/sequoia/
)

cpack_add_component(morphosyntax-fre.ud-sequoia
    DISPLAY_NAME
        "UD French / Sequoia corpus"
    GROUP
        French
)

