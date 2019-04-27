#include <sstream>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <csignal>
#include "tokenize.h"

using namespace std;

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
				int i;
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
	}
	infile.close();
	return out;
}


// to run it as a single file thing..
//int main(int argc, char** argv) {
//	for (int i=1; i < argc; ++i) {
//		string ifname = argv[i];
//		string ofname = ifname + "_" + to_string(i) + ".csv";
//		ofstream out_n (ofname);
//		vector<string> tokens = tokenize(ifname);
//		for (int tki=0; tki < tokens.size(); ++tki) {
//			 string tok = tokens[tki];
//			 char app;
//			 if (tki == tokens.size()-1) {
//				app  = '\n';
//			 }
//			 else {
//				app = ',';
//			 }
//			 out_n << tok+app;
//		 }
//		out_n.close();
//	}	
//	return 0;
//} 
