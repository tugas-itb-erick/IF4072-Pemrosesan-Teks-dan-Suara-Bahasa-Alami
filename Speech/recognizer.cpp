#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[]) {
	if (argc == 1) {
		cout << "Input filename" << endl;
		return 0;
	}
	string cp = "HCopy -A -D -C analysis/analysis.conf ";
	for (int i=0;argv[1][i];++i) {
		cp.push_back(argv[1][i]);
	}
	cp.push_back(' ');
	for (int i=0;argv[1][i];++i) {
		cp.push_back(argv[1][i]);
	}
	while (cp.back() != '.') cp.pop_back();
	cp.push_back('m'); cp.push_back('f'); cp.push_back('c'); cp.push_back('c');
	char * cstr = cp.c_str();
	strcat(cstr, " > /dev/null");
	system(cstr);
	string cm = "HVite -A -D -T 1 -H model/hmm20/pasang -H model/hmm20/alarm -H model/hmm20/hapus -H model/hmm20/nyalakan -H model/hmm20/matikan -H model/hmm20/pukul -H model/hmm20/jam -H model/hmm20/setengah -H model/hmm20/seperempat -H model/hmm20/kurang -H model/hmm20/lebih -H model/hmm20/nol -H model/hmm20/satu -H model/hmm20/dua -H model/hmm20/tiga -H model/hmm20/empat -H model/hmm20/lima -H model/hmm20/enam -H model/hmm20/tujuh -H model/hmm20/delapan -H model/hmm20/sembilan -H model/hmm20/sepuluh -H model/hmm20/sebelas -H model/hmm20/belas -H model/hmm20/puluh -H model/hmm20/sil -i tmp.mlf -w net.slf dict.txt hmmlist.txt ";
	for (int i=0;argv[1][i];++i) {
		cm.push_back(argv[1][i]);
	}
	while (cm.back() != '.') cm.pop_back();
	cm.push_back('m'); cm.push_back('f'); cm.push_back('c'); cm.push_back('c');
	cstr = cm.c_str();
	strcat(cstr, " > /dev/null");
	system(cstr);
	string s,t,sil="sil";
	ifstream in("tmp.mlf");
	getline(in, s);
	getline(in, s);
	while (getline(in, s)) {
		int sp = 0;
		t.clear();
		for (int i=0;i<s.size();++i) {
			if (sp==2) {
				for (int j=i;j<s.size() && s[j]!=' ';++j) {
					t.push_back(s[j]);
				}
				break;
			}
			if (s[i]==' ') ++sp;
		}
		if (!t.empty() && t != sil) cout << t <<  ' ';
	}
	cout << endl;
	return 0;
}