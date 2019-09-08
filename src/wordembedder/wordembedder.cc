#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <unordered_map>
#include "/home/chanceygardener/repos/proto_embed/src/tokenize/tokenize.h"
#include "/home/chanceygardener/repos/proto_embed/src/wordembedder/wordembedder.h"
#include "/home/chanceygardener/repos/proto_embed/src/utils/utils.h"

using namespace std;

WordEmbedder::WordEmbedder(string corpusName)
	: corpusName(corpusName) {}
		// methods to get and set corpus name

		string WordEmbedder::getCorpusName () {
			string corpusName = corpusName;
			return corpusName;
		}
		// tokenize method
		vector<string>WordEmbedder::tokensFromFile(int fcount, char* fnames[]) {
            cout << "\ntokenizeing...\n" << endl;
			vector<string> tokens;
            tokenize(fnames, fcount,tokens);
            cout << "\nupdating schema\n" << endl;
            _updateSchema(tokens);
            cout << tokens.size() << "\n" << endl;
			return tokens;
		}

        unordered_map<string,vector<vector<string>>>
        WordEmbedder::getTokensInContext(vector<string>& tokens, int window_size, vector<string> schema) {
            // declare skipgram and word environment maps
            unordered_map<string, vector<vector<string>> > voc_inst;
            // get skipgram embeddings for each word in token
            long unq_idx = 0;
            for (int idx = 0; idx != tokens.size(); ++idx) {
                string tok = normalize(tokens[idx]);
                auto lookup = voc_inst.find(tok);
                // make a key in the dist mapping if it's not in there yet
                if (lookup == voc_inst.end()) {
                    voc_inst.insert(make_pair(tok,
                                              vector<vector<string>>(1, getWindow(tokens, window_size, idx) )));
                    schema.emplace_back(tok);
                    //unq_idx += 1; // is this var ncessary TODO: check
                    //lookup = voc_inst.find(tok);
                }
                //vector<string> env;
                //env = getWindow(tokens, window_size, idx);
                //lookup->second.push_back(env);

            }
            return voc_inst;
        }

        unordered_map<string,vector<double>>
        WordEmbedder::tokensToSkipgram
                (vector<string>& tokens, int window_size) {
            vector<string> schema;
            cout << "\ncompiling token contexts\n" << endl;
            unordered_map<string,vector<vector<string>>> voc_inst = getTokensInContext(tokens, window_size, schema);
            cout << "\ngenerating co-occurrence vectors\n" << endl;
            int vocab_size = voc_inst.size();
            //alphabetize(&schema, vocab_size);
            sort(schema.begin(), schema.end());
            // declare and populate skipgram
            unordered_map<string,vector<double>> skipgrams;
            // per token word

            // the following block is iterating over previously accumulated contexts
            // of unique tokens. Therefore this block's steps should be
            // independent and potentially executed in parallel.

            for (int widx = 0; widx != vocab_size; ++widx) {
                double n_hot[vocab_size];
                // vocab lookup
                string w = schema[widx];
                vector<vector<string> > wscope = voc_inst.find(w)->second;
                // per instance word
                int instance_count = 0;
                for (vector<string> en: wscope) {
                    // per word in instance
                    int wc_check = 0;
                    for (string neighbor : en) {
                        vector<string>::const_iterator schidx = find(schema.begin(),
                                                                     schema.end(), neighbor);
                        int ind = distance(schema.cbegin(), schidx);
                        //cout << ind << " " << wc_check << endl;
                        n_hot[ind] += 1.0;
                        wc_check++;
                    }
                    instance_count++;
                }
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

		// skipgram extractor (takes vector)
		unordered_map<string,vector<double> >
			WordEmbedder::skipgram (vector<string>& tokens, int wsize) {
                    cout << "\n\ncompiling skipgram vectors...\n\n" << endl;
					unordered_map<string,vector<double>>
							out = tokensToSkipgram (tokens, wsize);
				return out;
		}

        void WordEmbedder::_updateSchema(vector<string> tokens) {
            for (string token: tokens) {
                vector<string>::iterator lookup =
                        find(this->schema.begin(), this->schema.end(), token);
                if (lookup == this->schema.end()) {
                    this->schema.push_back(token);
                }
            }

        }

    unordered_map<string,vector<string>>
    WordEmbedder::getContextsByToken(vector<string>& tokens, int window_size) {
        unordered_map<string,vector<string>> cont_inst;
        unsigned long unq_idx = 0;
        for (int idx = 0; idx != tokens.size(); ++idx) {
            vector<string> window(window_size*2);
            string center_word = tokens[idx];
            string context = catEnv(getWindow(tokens, window_size, idx));
            auto lookup = cont_inst.find(context);
            if (lookup == cont_inst.end()) {
                vector<string> centry = vector<string>(1, center_word);
                cont_inst.insert( make_pair(context,  centry) );
            }
            else {
                lookup->second.push_back(center_word);
            }

        }
        return cont_inst;
    }


void WordEmbedder::writeSkipgramsToCsv(string& ofname,
                unordered_map<string,vector<double>> dat) {

            ofstream of;
            cout << "\nwriting to csv\n" << endl;
            // TODO(chanceygardener) set schema size as WEmb attribute
            of.open(ofname);
            of << ","; // so the indices line up in the file.
            for (pair<string, vector<double> > token: dat) {
                of << token.first << ",";
            }
            of << "\n";
            for (pair<string, vector<double> > token: dat) {
                of << token.first << ",";
                for (double sgval: token.second) {
                    of << sgval << ",";
                }
                of << "\n";
            }
            of.close();
        }




