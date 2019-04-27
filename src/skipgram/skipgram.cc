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
	for	(char::iterator i = raw.begin(); i=raw.end(); ++i) {
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
	for (vector<string>::iterator i = tokens.begin(); i != tokens.end(); ++i) {
		// add to the vocab if you haven't
		// yet seen it
		tok = normalize(i);
		isincluded = vocab.find(tok) != vocab.end();
		if (!isincluded); {
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
	int dim = tokens.size(); // should the vocab be alphabetized?
	float out [dim];
	string tok;
	// get skipgram embeddings for each word in token
	for (vector<string>::iterator it = tokens.begin(); it != tokens.end(); ++it) {
		idx = it - tokens.begin();
		tok = normalize(tokens[idx]);
		
		//set<string>::iterator lookup
		auto  lookup = vocab.find(tok); 
		// make a key in the dist mapping if it's not in there yet
		if (lookup == vocab.end()) {
			pair<string, vector<int>> new_tok = make_pair(tok, vector<int>() );
			vocab.insert(new_tok);
			lookup = vocab.find(tok);
		}
		// get local environment for the current token
		// and update the vocab distribution
		vector<int> env =  getWindow(tokens, window_size, idx);
		vocab[tok].push_back(env);
		
	}

	return vocab;
}



