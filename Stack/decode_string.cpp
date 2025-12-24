#include <bits/stdc++.h>
using namespace std;

string decodeString(string s) {
    stack<int> numSt;
    stack<string> strSt;
    string curr = "";
    int num = 0;

    for(char c : s) {
        if(isdigit(c)) {
            num = num * 10 + (c - '0');
        } else if(c == '[') {
            numSt.push(num);
            strSt.push(curr);
            num = 0;
            curr = "";
        } else if(c == ']') {
            int k = numSt.top(); numSt.pop();
            string prev = strSt.top(); strSt.pop();
            while(k--) prev += curr;
            curr = prev;
        } else {
            curr += c;
        }
    }
    return curr;
}
