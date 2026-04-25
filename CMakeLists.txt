cmake_minimum_required(VERSION 3.12)
project(LeetCode_CPlusPlus)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 加上 CONFIGURE_DEPENDS，这样新建文件后不需要手动重载 CMake
file(GLOB_RECURSE ALL_CPP_FILES CONFIGURE_DEPENDS "*.cpp")
# 过滤掉 build 文件夹里面的所有临时 .cpp 文件
list(FILTER ALL_CPP_FILES EXCLUDE REGEX "build")
# 将所有的 exe 文件统一输出到一个 build/bin 目录下，防止和源码混在一起导致文件夹太乱
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

foreach(CPP_FILE ${ALL_CPP_FILES})
    get_filename_component(TARGET_NAME ${CPP_FILE} NAME_WE)
    add_executable(${TARGET_NAME} ${CPP_FILE})
endforeach()