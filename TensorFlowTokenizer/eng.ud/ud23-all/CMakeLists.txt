cmake_minimum_required(VERSION 3.12.1)

install(
    FILES
        UD_English-ALL.conf
        UD_English-ALL.model
    COMPONENT
        tokenizer-eng.ud-all
    DESTINATION
        share/apps/lima/resources/TensorFlowTokenizer/eng.ud/all/
)

cpack_add_component(tokenizer-eng.ud-all
    DISPLAY_NAME
        "UD English / All corpora"
    GROUP
        English
)

