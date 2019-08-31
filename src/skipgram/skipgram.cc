#include <vector>
#include <string>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <locale>
#include <iterator>
#include "skipgram.h"
#include <iostream>

const int WINDOW_SIZE = 4;
const int ENV_SIZE = 2 * WINDOW_SIZE;

// FOR TESTING, so's we can print out dem std::vectors.
template<typename T>
std::ostream& operator<<(std::ostream& os, std::vector<T> vec) {
    os<<"{ ";
    std::copy(vec.begin(), vec.end(), std::ostream_iterator<T>(os, " "));
    os<<"}";
    return os;
}

using namespace std;

// structure for word
// environments. contains
// array of length ENV_SIZE
// containing pointers to schema array.
struct env {
    string symbols[ENV_SIZE*2];
};

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

int idx_from_schema(string* sch[], string* targ, int vsize) {
    //const int stop = sizeof(sch); //unnecessary
    for (unsigned int ix = 0; ix < vsize; ix++) {
        string* cw = sch[ix];
        if (cw == targ) {
            return ix;
        }
    }
    return vsize;
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
    //cout << "getWindow output for " << src[cind]  << ": " << win << "\n\n" << endl;
	return win;
}

unordered_map<string,vector<double>>
		tokensToSkipgram 
			(vector<string>& tokens, int window_size=WINDOW_SIZE) {
    // declare skipgram and word environment maps
    unordered_map<string, vector<vector<string>> > voc_inst;
    // get skipgram embeddings for each word in token
    vector<string> schema;
    long unq_idx = 0;
    for (int idx = 0; idx != tokens.size(); ++idx) {
        string tok = normalize(tokens[idx]);
        auto lookup = voc_inst.find(tok);
        // make a key in the dist mapping if it's not in there yet
        if (lookup == voc_inst.end()) {
            voc_inst.insert(make_pair(tok, vector<vector<string>>()));
            schema.emplace_back(tok);
            unq_idx += 1; // is this var ncessary TODO: check
            lookup = voc_inst.find(tok);
        }
    vector<string> env;
    env = getWindow(tokens, window_size, idx);
    lookup->second.push_back(env);

}
    int vocab_size = schema.size();
    //alphabetize(&schema, vocab_size);
    sort(schema.begin(), schema.end());
    // declare and populate skipgram
    unordered_map<string,vector<double>> skipgrams;
    // per token word
    for (int widx = 0; widx != vocab_size; ++widx) {
        double n_hot[vocab_size]; // INVALID READ/WRITE declared here
        // vocab lookup
        string w = schema[widx];
        vector<vector<string> > wscope = voc_inst.find(w)->second;
        // per instance word
        int instance_count = 0;
        int ws_check = 0;
        for (vector<string> en: wscope) {
            // per word in instance
            int wc_check = 0;
            for (string neighbor : en) {
                // watch the following two lines when they come up
                // You sure you iteratin' over wtf you think you iteratin' over bruh?
                vector<string>::const_iterator schidx = find(schema.begin(), schema.end(), neighbor);
                int ind = distance(schema.cbegin(), schidx);
                cout << ind << " "<< wc_check << endl;
                n_hot[ind] += 1.0;
                wc_check++;
                }
            cout << "\n\n" << endl;
            instance_count++;
            }
        ws_check++;
        cout << "\nword " << ws_check << endl;
        // divide array
        for (int i = 0; i < vocab_size; i++) {
            n_hot[i] = n_hot[i] / (instance_count);
        }
        vector<double> skipgram_entry (vocab_size);
        copy(n_hot, n_hot+vocab_size, skipgram_entry.begin());
        skipgrams.insert(std::make_pair(w, skipgram_entry));
        }
        return skipgrams;
    }





