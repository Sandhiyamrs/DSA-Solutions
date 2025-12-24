#include <bits/stdc++.h>
using namespace std;

vector<int> dailyTemperatures(vector<int>& temps) {
    int n = temps.size();
    vector<int> res(n, 0);
    stack<int> st;

    for(int i = 0; i < n; i++) {
        while(!st.empty() && temps[st.top()] < temps[i]) {
            int idx = st.top(); st.pop();
            res[idx] = i - idx;
        }
        st.push(i);
    }
    return res;
}
