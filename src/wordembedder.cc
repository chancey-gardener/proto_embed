#include <iostream>
#include <vector>
#include <string>
#include "tokenize.h"
#include "skipgram.h"
#include "wordembedder.h"

using namespace std;

class WordEmbedder {
	private:
		string corpusName;	
	public:
		// methods to get and set corpus name
		string getCorpusName () {
			return this.corpusName;
		}
		void setCorpusName (string name) {
			this.corpusName = name;
		}

		// tokenize method
		vector<string> tokensFromFile(string& fname) {
			vector<string> tokens tokenize(fname);
			return tokens
		}

		// skipgram extractor (takes vector)
		unordered_map<string,vector<vector<int> >
			   	skipgram (vector<string>& tokens) {
					unordered_map<string,vector<vector<int> > 
							out = tokensToSkipgram (tokens);
				return out;
		}
	//constructor
	int main (WordEmbedder this, 
					string corpusName ) 
		{
			this.corpusName = corpusName;
			this.print();
			
	
		return 0;

	 } 

}


