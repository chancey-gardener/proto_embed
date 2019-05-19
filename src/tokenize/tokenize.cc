#include <sstream>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <csignal>
#include "tokenize.h"

using namespace std;

// TODO: find bug that makes "i'd" become "i" "p" "d"
vector<string> tokenize(string& fname) {
	ifstream infile;
	infile >> noskipws; // make the stream include whitespace chars
	infile.open(fname);
	char c;
	char mem; // allows for a single char lookbehind; useful for contractions
	string wordbuff;
	vector<string> out;
	if (infile.is_open()) {
		while (!infile.eof()) {
			mem = c;
			infile >> c;
			//cout << c;
			while (isspace(c) && !infile.eof()) {
			//	cout << c << endl;
				mem = c;
				infile >> c;
			}
			while (isalnum(c) && !infile.eof()) {
				wordbuff += c;
				mem = c;
				infile >> c;
			}
			if (!wordbuff.empty()) {
				out.push_back (wordbuff);
			//	cout << "\n\nout array:\n" << endl;
				// print 'out' for debugging
				for (int i = out.size(); i >=0; i--) {
						
			//			cout << out[i-1] << '\n' << endl;
				}
				//cout << wordbuff << '\n' << endl;
				wordbuff = "";
			}
			
			if (c=='\'') {
				wordbuff += mem+c;
			}
			if (wordbuff.empty()) {
				while (!PUNCT.find(c)==-1 && !infile.eof()) {
					wordbuff += c;
					mem << c;
					infile >> c;
				}
				continue;
			}
			// flush wordbuff to out
			out.push_back (wordbuff);
			wordbuff = "";
			
		}
	infile.close();
    }
	else {
        cout << "\nError opening input file." << endl;

    }
	return out;
}

