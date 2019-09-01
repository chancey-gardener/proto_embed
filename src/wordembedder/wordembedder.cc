#include <iostream>
#include <vector>
#include <string>
#include <fstream>
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
		vector<string>WordEmbedder::tokensFromFile(int fcount, char* fnames[]) {
            cout << "\ntokenizeing...\n" << endl;
			vector<string> tokens;
            tokenize(fnames, fcount,tokens);
            cout << tokens.size() << "\n" << endl;
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

		void WordEmbedder::writeToCsv(string& ofname,
                unordered_map<string,vector<double>> dat) {

            ofstream of;
            cout << "\nwriting to csv\n" << endl;
            // TODO(chanceygardener) set schema size as WEmb attribute
            of.open(ofname);
            of << ","; // so the indices line up in the file.
            for (pair<string, vector<double> > token: dat) {
                of << token.first;
            }
            of << "\n";
            for (pair<string, vector<double> > token: dat) {
                of << token.first << ",";
                for (double sgval: token.second) {
                    of << sgval << ",";
                }
                of << "\n";
            }
            of.close();
        }




