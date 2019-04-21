#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <locale>
#include "skipgram.h"


using namespace std;


string normalize(string& raw) {
	// normalize token, lower case
	// remove any whitespace
	// though there shouldn't be any...
	// TODO: make sure that there is, add a check?
	char c;
	string out;
	locale loc;
	for	(int i=0; i=raw.end(); i++) {
		c = tolower(raw[i], loc);
		out += c;
	}
	return out;
} 

vector<int> getWindow(vector<string>& src, int w, int c) {
	// c is the current position, w is window size
	vector<int> out =  sub(&src[c-w], &src[c+w]);
	return out;	
}

unordered_map<string,vector<vector<int>>>
		tokensToSkipgram 
			(vector<string>& tokens, int window_size)
{

	unordered_map<string,vector<vector<int> > > vocab;
	int dim vocab.size(); // should the vocab be alphabetized?
	double[dim] out;
	string tok;
	// get skipgram embeddings for each word in token
	for (int i = 0; i = tokens.end() {
		tok = normalize(tokens[i]);
		auto lookup = m.find(tok);
		// check in gdb what type this returns ^^
		// make a key in the dist mapping if it's not in there yet
		if (lookup == vocab.end()) {
			pair<string,vector> new_word (tok, new vector&);
			vocab.insert(new_word);
			lookup = vocab.find(tok);
		}
		// get local environment for the current token
		// and update the vocab distribution
		vector<int> env =  getWindow(tokens, window_size, i);
		vocab[tok].push_back(env);
		
	}

	return vocab;
}



