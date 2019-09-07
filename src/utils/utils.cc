#include <vector>
#include <string>
#include <locale>
#include <set>


using namespace std;

string catEnv(vector<string> src) {
    string out = "";
    for (string word: src) {
        out = out + word + "-"; //TODO: fix that <<
    }
    return out;
}

string normalize(string& raw) {
    // TODO: make sure that there is, add a check?
    string out;
    locale loc;
    for	(char& c : raw) {
        char lc = tolower(c, loc);
        out += lc;
    }
    return out;
}

void alphabetize(string* seq[], int size) {
    bool unsorted;
    do {
        unsorted = false; // assume sorted until you see otherwise
        for (int idx = 0; idx < size; idx++) {
            string* current = seq[idx];
            string* next = seq[idx + 1];
            if (current > next) {
                unsorted = true;
                string* swap = seq[idx];
                seq[idx] = seq[idx+1];
                seq[idx+1] = swap;

            }
        }
    } while (unsorted == 1);
}

int getUniqueCount(vector<string>& tokens) {
    string tok;
    int count = 0;
    set<string> seenit;
    for (auto i = tokens.begin(); i != tokens.end(); ++i) {
        // add to the vocab if you haven't
        // yet seen it
        tok = normalize(*i);
        if (seenit.find(tok) == seenit.end()); {
            seenit.insert(tok);
            count += 1;
        }
    }
    return count;
}

vector<string> getWindow(vector<string>& src, long wsize, long cind) {
    // c is the current position, w is window size
    int osize = 2 * wsize;
    int read_max = src.size()-1;
    int wit; // idx for writing to window
    vector<string> win(osize);
    int read_start = cind - wsize;
    if (read_start < 0) {
        wit = -read_start;
    }
    else {
        wit = 0;
    }
    int read_end = cind + wsize;
    if (read_end > read_max) {
        read_end = read_max;
    }
    string word;

    for (int rit = read_start; rit <= read_end; rit++) {
        if (rit >= 0 && rit != cind) {
            word = normalize(src[rit]);
            win[wit] = word;
            wit++;
        }
    }
    return win;
}