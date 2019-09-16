cmake_minimum_required(VERSION 3.12.1)

set(CPACK_ARCHIVE_COMPONENT_INSTALL ON)
set(CPACK_COMPONENTS_GROUPING ONE_PER_GROUP)
set(CPACK_DEB_COMPONENT_INSTALL ON)
set(CPACK_GENERATOR "DEB")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "LIMA Publisher")
set(CPACK_PACKAGE_NAME lima-deep-models)
set(CPACK_PACKAGE_VERSION "0.1.3")
set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "all")
set(CPACK_DEBIAN_FILE_NAME DEB-DEFAULT)

include(CPack)

cpack_add_component_group(English)
cpack_add_component_group(French)

add_subdirectory(TensorFlowTokenizer)
add_subdirectory(TensorFlowMorphoSyntax)
