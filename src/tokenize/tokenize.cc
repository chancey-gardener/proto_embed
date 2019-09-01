
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "tokenize.h"

using namespace std;

// TODO: find bug that makes "i'd" become "i" "p" "d"


void tokenize(char* fnames[], int fcount, std::vector<std::string> &tokens) {
    ifstream infile;
    infile >> noskipws; // make the stream include whitespace chars
    int file_idx = 0;
    string wordbuff;
    char c;
    char mem; // allows for a single char lookbehind; useful for contractions
    while (file_idx < fcount) {
        string fname = fnames[file_idx];
        infile.open(fname);
        if (infile.is_open()) {
            while (!infile.eof()) {
                mem = c;
                infile >> c;
                while (isspace(c) && !infile.eof()) {
                    mem = c;
                    infile >> c;
                }
                while (isalnum(c) && !infile.eof()) {
                    wordbuff += c;
                    mem = c;
                    infile >> c;
                }
                if (!wordbuff.empty()) {
                    tokens.push_back(wordbuff);
                    wordbuff = "";
                }

                if (c == '\'') {
                    wordbuff += mem + c;
                }
                if (wordbuff.empty()) {
                    while (!PUNCT.find(c) == -1 && !infile.eof()) {
                        wordbuff += c;
                        mem << c;
                        infile >> c;
                    }
                    continue;
                }
                // flush wordbuff to out
                tokens.push_back(wordbuff);
                wordbuff = "";

            }
            infile.close();

        } else {
            cout << "\nError opening input file." << endl;

        }
        file_idx ++;
    }
}
