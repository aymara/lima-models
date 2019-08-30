cmake_minimum_required(VERSION 3.12.1)

install(
    FILES
        UD_English-EWT.conf
        UD_English-EWT.model
    COMPONENT
        tokenizer-eng.ud-ewt
    DESTINATION
        share/apps/lima/resources/TensorFlowTokenizer/eng.ud/ewt/
)

cpack_add_component(tokenizer-eng.ud-ewt
    DISPLAY_NAME
        "UD English / EWT corpus"
    GROUP
        Tokenizer
)

