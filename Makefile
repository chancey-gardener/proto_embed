

CXX = g++
CXXFLAGS = -Wall -g


main: 
	${CXX} src/main.cc src/wordembedder/wordembedder.cc src/skipgram/skipgram.cc src/tokenize/tokenize.cc -o wetest


