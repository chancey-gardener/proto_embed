#ifndef WORDEMBEDDER_H
#define WORDEMBEDDER_H

#include <vector>
#include <string>
#include <unordered_map>
#include <set>

using namespace std;

class WordEmbedder {
	private:
			string corpusName;
	public:
			//get and set corpus name
			string getCorpusName();
			void setCorpusName();
			//tokenize from file
			vector<string> tokenize(string& fname);
			//skipgram from tokens
			unordered_map<string,vector<vector<int> > 
					skipgram (vector<string>& tokens);

};

#endif
