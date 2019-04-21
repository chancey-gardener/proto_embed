#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "tokenize.h"
#include "skipgram.h"
#include "wordembedder.h"

using namespace std;

WordEmbedder::WordEmbedder(string corpusName) 
	: corpusName(corpusName) {}
		// methods to get and set corpus name
		string WordEmbedder::getCorpusName () {
			string corpusName = corpusName;
			return corpusName;
		}
		//void WordEmbedder::setCorpusName (name) {
		//	this.corpusName = name;
		//}

		// tokenize method
		vector<string>WordEmbedder::tokensFromFile(string& fname) {
			vector<string> tokens = tokenize(fname);
			return tokens;
		}

		// skipgram extractor (takes vector)
		unordered_map<string,vector<vector<int>> >
			WordEmbedder::skipgram (vector<string>& tokens, int wsize) {
					unordered_map<string,vector<vector<int>> >  
							out = tokensToSkipgram (tokens, wsize);
				return out;
		}
	//constructor
	//int main (WordEmbedder this, 
	//				string corpusName ) 
	//	{
	//		this.corpusName = corpusName;
	//		this.print();
	//		
	//
	//	return 0;
	//
	//} 
	int main() {
		return 0;
	}



