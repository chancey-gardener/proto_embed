#ifndef UTILS_H
#define UTILS_H

#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

vector<string> getWindow(vector<string>& src, long wsize, long cind);
string normalize(std::string& raw);
string catEnv(std::vector<std::string> src);
void alphabetize(string* seq[], int size);
int getUniqueCount(vector<string>& tokens);

#endif
