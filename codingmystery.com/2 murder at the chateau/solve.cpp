#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int _lcps(string x, string y, int i, int j, int k, int l) {
	if (i > j || k > l) return 0;
	if (i == j && k == l && x[i] == x[j] == y[k] == y[l]) return 1;
	if (i < j && k < l && x[i] == x[j] && x[i] == y[k] && x[i] ==  y[l]) return 2 + _lcps(x, y, i+1, j-1, k+1, l-1);
	return max(max(max(_lcps(x, y, i + 1, j, k, l), _lcps(x, y, i, j - 1, k, l)), _lcps(x, y, i, j, k + 1, l)), _lcps(x, y, i, j, k, l - 1));
}

int lcps(string x, string y) {
	return _lcps(x, y, 0, x.length() - 1, 0, y.length() - 1);
}

int main() {
	ifstream traces;
	ifstream samples;
	traces.open("Object Dna Traces.txt");
	samples.open("Suspects And Victim Dna Samples.txt");
	string line;
	vector<string> traces_list;
	vector<string> samples_list;
	vector<string> matches;
	vector<string>::iterator it;
	while (getline(traces, line)) {
		traces_list.push_back(line.substr(0, 100));
	}
	while (getline(samples, line)) {
		samples_list.push_back(line);
	}
	for (int i = 0; i < traces_list.size(); i++) {
		for (int j = 0; j < samples_list.size(); j++) {
			if (lcps(traces_list[i], samples_list[j]) > 100) {
				matches.push_back(samples_list[j]);
			}
		}
	}
	for (it = matches.begin(); it != matches.end(); it++) {
		cout << *it << endl;
	}
	return 0;
}