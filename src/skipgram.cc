#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <locale>
#include "skipgram.h"


using namespace std;


struct freqdist {
	unordered_map<string,vector<vector<int> > dist;
}

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

set<string> getUniqueSet(vector<string>& tokens) {
	set<string> vocab;
	locale loc;
	string tok;
	bool isincluded;
	for (int i = 0; i=tokens.end(); i++) {
		// add to the vocab if you haven't
		// yet seen it
		tok = normalize(tokens[i]);
		isincluded = vocab.find(tok) != vocab.end();
		if !(isincluded); {
			vocab.add(tok);
		}
	}
	return vocab;
}

vector<int> getWindow(vector<string>& src, int w, int c) {
	// c is the current position, w is window size
	vector<int> out =  sub(&src[c-w], &src[c+w]);
	return out;	
}

unordered_map<string,vector<vector<int> > >
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
		string lookup = vocab.find(tok); // check in gdb what type this returns
		// make a key in the dist mapping if it's not in there yet
		if (lookup == vocab.end()) {
			vocab.insert(tok);
			lookup = vocab.find(tok);
		}
		// get local environment for the current token
		// and update the vocab distribution
		vector<int> env =  getWindow(tokens, window_size, i);
		vocab[tok].push_back(env);
		
	}

	return vocab;
}



