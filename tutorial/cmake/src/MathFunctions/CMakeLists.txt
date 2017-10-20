add_executable (MakeTable MakeTable.cpp)

add_custom_command (
	OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/Table.hpp
	COMMAND MakeTable ${CMAKE_CURRENT_BINARY_DIR}/Table.hpp
	DEPENDS MakeTable
	)

include_directories (${CMAKE_CURRENT_BINARY_DIR})

add_library (MathFunctions mysqrt.cpp ${CMAKE_CURRENT_BINARY_DIR}/Table.hpp)

install (TARGETS MathFunctions DESTINATION bin)
install (FILES MathFunctions.hpp DESTINATION include)
