#include <iostream>
#include "/home/chanceygardener/repos/probed/src/wordembedder/wordembedder.h"
#include <string>

using namespace std;

const int WINDOW = 4;

int main() {
	string infile = "test.txt";
	WordEmbedder emb = WordEmbedder("test");
	vector<string> tokens = emb.tokensFromFile(infile);
	unordered_map<string,vector<vector<int> >> dist = emb.skipgram(tokens, WINDOW);
	cout << "It Worked!" << endl;
	return 0;
}
