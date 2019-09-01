#ifndef TOKENIZE_H
#define TOKENIZE_H

#include <vector>
#include <string>

const std::string PUNCT;
void tokenize(char* fnames[], int fcount, std::vector<std::string> &tokens);

#endif
