#include <iostream>
#include "/home/chanceygardener/repos/proto_embed/src/wordembedder/wordembedder.h"
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

int main(int argc, char* argv[]) {
	WordEmbedder emb = WordEmbedder("test");

//	string hard_code_path =
//	        "/home/chanceygardener/repos/proto_embed/data/raw/paradise_lost.txt";
//	//vector<string> *test = new vector<string>;
//	vector<string> test = emb.tokensFromFile(hard_code_path);
//	cout << "processed hard coded path.." << "\n" << endl;
//	cout << test << "\n" << endl;

    vector<string> tokens;
    tokens = emb.tokensFromFile(argc-1, argv+1);
	//unordered_map<string,vector<double> >* dist = new unordered_map;
    unordered_map<string,vector<double> >* dist =
            new unordered_map<string,vector<double> >;
    *dist = emb.skipgram(tokens, WINDOW);
    for (pair<string, vector<double> > elem: *dist) {
        cout << elem.first << " " << elem.second << endl;
    }
    delete dist;
	return 0;
}
