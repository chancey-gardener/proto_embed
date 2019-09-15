#include <iostream>
#include "/home/chanceygardener/repos/proto_embed/src/wordembedder/wordembedder.h"
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
#include "/home/chanceygardener/repos/proto_embed/src/fake_task/fake_task.h"


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
    vector<string> tokens;
    tokens = emb.tokensFromFile(argc-1, argv+1);
	//unordered_map<string,vector<double> >* dist = new unordered_map;
    unordered_map<string,vector<double> > dist;
    dist = emb.skipgram(tokens, WINDOW);
    string ofname = "test_sg_classics.csv";
    emb.writeSkipgramsToCsv(ofname, dist);
    //delete dist;
    dist.clear();
    unordered_map<string,vector<string>> conts =
            emb.getContextsByToken(tokens, WINDOW);

	return 0;
}
