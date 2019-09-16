cmake_minimum_required(VERSION 3.12.1)

install(
    FILES
        UD_English-EWT.conf
        UD_English-EWT.model
    COMPONENT
        morphosyntax-eng.ud-ewt
    DESTINATION
        share/apps/lima/resources/TensorFlowMorphoSyntax/eng.ud/ewt/
)

cpack_add_component(morphosyntax-eng.ud-ewt
    DISPLAY_NAME
        "UD English / EWT corpus"
    GROUP
        English
)

