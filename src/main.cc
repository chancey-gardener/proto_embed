#include <iostream>
#include "/home/chanceygardener/repos/probed/src/wordembedder/wordembedder.h"
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>


// FOR TESTING, so's we can print out dem std::vectors.
template<typename T>
std::ostream& operator<<(std::ostream& os, std::vector<T> vec) {
    os<<"{ ";
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<T>(os, " "));
    os<<"}";
    return os;
}

using namespace std;

const int WINDOW = 4;

int main() {
	string infile = "/home/chanceygardener/repos/probed/data/raw/paradise_lost.txt";
	WordEmbedder emb = WordEmbedder("test");
	vector<string> tokens = emb.tokensFromFile(infile);
	//unordered_map<string,vector<double> >* dist = new unordered_map;
    unordered_map<string,vector<double> >* dist = new unordered_map<string,vector<double> >;
    *dist = emb.skipgram(tokens, WINDOW);
    for (pair<string, vector<double> > elem: *dist) {
        cout << elem.first << " " << elem.second << endl;
    }
    delete dist;
	return 0;
}
