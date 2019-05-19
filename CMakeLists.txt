cmake_minimum_required(VERSION 3.9)
project(probed)

set(CMAKE_CXX_STANDARD 11)

add_executable(probed
        src/freqdist/freqdist.cc
        src/freqdist/freqdist.h
        src/skipgram/skipgram.cc
        src/skipgram/skipgram.h
        src/tokenize/tokenize.cc
        src/tokenize/tokenize.h
        src/wordembedder/wordembedder.cc
        src/wordembedder/wordembedder.h
        src/main.cc)
