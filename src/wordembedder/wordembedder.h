#ifndef WORDEMBEDDER_H
#define WORDEMBEDDER_H

#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include "/home/chanceygardener/repos/proto_embed/src/utils/utils.h"

using namespace std;

class WordEmbedder {
	private:
			const string corpusName;
			vector<string> schema;
			// begin functions
			static vector<string> _getSchema(vector<string> tokens);

            unordered_map<string,vector<double>> tokensToSkipgram(
            vector<string>& tokens, int window_size);

            unordered_map<string,vector<vector<string>>>
            getTokensInContext(vector<string>& tokens, int window_size, vector<string> schema);



            void _updateSchema(vector<string> tokens);

	public:
			WordEmbedder(string corpusName);
			//get and set corpus name
			static string getCorpusName();
			//void setCorpusName(string name);
			//tokenize from file
			vector<string> tokensFromFile(int fcount, char* fnames[]);
			//skipgram from tokens
			unordered_map<string,vector<double> >
					skipgram (vector<string>& tokens, int wsize);
			static void writeSkipgramsToCsv(string& ofname, unordered_map<string,
			        vector<double>> dat);

            unordered_map<string,vector<string>>
            getContextsByToken(vector<string>& tokens, int window_size);

};

#endif
