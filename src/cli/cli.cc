#include <unordered_map>
#include <vector>
#include "/home/chanceygardener/repos/proto_embed/src/wordembedder/wordembedder.h"
using namespace std;

typedef void (*Procedure)(void);

int run(int argc char* argv[], Embedder) {
    const unordered_map<string,Procedure> cmd_bank;
    cmd_bank["tokenize"] = (*Embedder->tokensFromFile);
    cmd_bank["skipgram"] = (*Embedder->tokensToSkipgram);
    cmd_bank["contexts"] = (*Embedder->getTokensInContext);

}