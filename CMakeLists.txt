cmake_minimum_required(VERSION 3.12)
project(LeetCode_CPlusPlus)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Only scan problem source files under problems/.
file(GLOB_RECURSE ALL_CPP_FILES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/problems/*.cpp"
)

# Put all executables under build/bin to keep the workspace tidy.
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

foreach(CPP_FILE ${ALL_CPP_FILES})
    get_filename_component(TARGET_NAME ${CPP_FILE} NAME_WE)
    add_executable(${TARGET_NAME} ${CPP_FILE})
endforeach()
