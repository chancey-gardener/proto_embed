cmake_minimum_required(VERSION 3.9)
project(probed)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_VERBOSE_MAKEFILE FALSE)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

#include_directories(/usr/include/c++/8/eigen3)

find_package (Eigen3 3.3 REQUIRED NO_MODULE)

add_executable(probed
        src/freqdist/freqdist.cc
        src/freqdist/freqdist.h
        src/utils/utils.cc
        src/utils/utils.h
        src/tokenize/tokenize.cc
        src/fake_task/fake_task.cc
        src/fake_task/fake_task.h
        src/tokenize/tokenize.h
        src/wordembedder/wordembedder.cc
        src/wordembedder/wordembedder.h
        src/main.cc)
target_link_libraries (probed Eigen3::Eigen)

