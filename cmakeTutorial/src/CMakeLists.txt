cmake_minimum_required (VERSION 2.6)
project (Tutorial)

set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

option (USE_MYMATH "Use tutorial provided math implementation" ON)

configure_file (
	"${PROJECT_SOURCE_DIR}/TutorialConfig.hpp.in"
	"${PROJECT_BINARY_DIR}/TutorialConfig.hpp" 
)

include_directories (
	"${PROJECT_BINARY_DIR}"
)

if (USE_MYMATH)
	include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
	add_subdirectory (MathFunctions)
	set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MYMATH)

add_executable (Tutorial tutorial.cpp)
target_link_libraries (Tutorial ${EXTRA_LIBS})

install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.hpp" DESTINATION include)
