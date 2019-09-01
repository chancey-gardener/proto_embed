#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include "/home/chanceygardener/repos/proto_embed/src/tokenize/tokenize.h"
#include "/home/chanceygardener/repos/proto_embed/src/skipgram/skipgram.h"
#include "/home/chanceygardener/repos/proto_embed/src/wordembedder/wordembedder.h"
#include "wordembedder.h"

using namespace std;

WordEmbedder::WordEmbedder(string corpusName)
	: corpusName(corpusName) {}
		// methods to get and set corpus name
		string WordEmbedder::getCorpusName () {
			string corpusName = corpusName;
			return corpusName;
		}
		// tokenize method
		vector<string>WordEmbedder::tokensFromFile(string& fname) {
            cout << "\ntokenizeing...\n" << endl;
			vector<string> tokens;
			tokens = tokenize(fname);
			return tokens;
		}

		// skipgram extractor (takes vector)
		unordered_map<string,vector<double> >
			WordEmbedder::skipgram (vector<string>& tokens, int wsize) {
                    cout << "\n\ncompiling skipgram vectors...\n\n" << endl;
					unordered_map<string,vector<double>>
							out = tokensToSkipgram (tokens, wsize);
				return out;
		}




