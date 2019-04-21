#ifndef SKIPGRAM_H
#define SKIPGRAM_h

#include <string>
#include <vector>
#include <locale>
#include <unordered_map>


using namespace std;

// convert tokens to all lower case
string normalize(string& raw);
// get a skipgram model from vector of tokens
unordered_map<string,vector<vector<int> > > tokensToSkipgram(
				vector<string>& tokens, int window_size
				);




#endif
