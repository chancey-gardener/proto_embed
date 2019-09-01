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
	string hard_code_path = "/home/chanceygardener/repos/proto_embed/data/raw/paradise_lost.txt";
	vector<string> test = emb.tokensFromFile(hard_code_path);
	cout << "processed hard coded path.." << endl;
	cout << test;

	vector<string> *tokens = new vector<string>;
	for (char **fpath_point=argv+1; *fpath_point != argv[argc]; fpath_point++) {
	    string fpath = *fpath_point;
	    cout << fpath << endl;
        vector<string> *ftoks;
        *ftoks = emb.tokensFromFile(fpath);
        vector<string>::iterator tok_it;
        tok_it = tokens->begin();
        tokens->insert(tok_it+2, ftoks->begin(), ftoks->end());
        //delete ftoks;

    }
	cout << *tokens;
	//unordered_map<string,vector<double> >* dist = new unordered_map;
    unordered_map<string,vector<double> >* dist = new unordered_map<string,vector<double> >;
    *dist = emb.skipgram(*tokens, WINDOW);
    for (pair<string, vector<double> > elem: *dist) {
        cout << elem.first << " " << elem.second << endl;
    }
    delete dist;
	return 0;
}
