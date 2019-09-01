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
			WordEmbedder(string corpusName);
			//get and set corpus name
			string getCorpusName();
			//void setCorpusName(string name);
			//tokenize from file
			vector<string> tokensFromFile(int fcount, char* fnames[]);
			//skipgram from tokens
			unordered_map<string,vector<double> >
					skipgram (vector<string>& tokens, int wsize);

};

#endif
