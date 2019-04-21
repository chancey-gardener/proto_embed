#include <iostream>
#include "wordembedder.h"
#include <string>

using namespace std;

int main() {
	string infile = "test.txt";
	WordEmbedder emb;
	vector<string> tokens = emb.tokenize(infile);
	unordered_map<string,vector<vector<int> > dist;
	return 0;
}
