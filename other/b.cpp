#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define ll long long
#define rep(i, n) for (ll i = 0;i < n;i++)

using namespace std;

int main() {
    ll n, a;
    vector<bool> flg(2001, true);
    cin >> n;
    rep(i, n) {
        cin >> a;
        flg[a] = false;
    }
    rep(i, 2001) {
        if (flg[i]) {
            cout << i << endl;
            exit(0);
        }
    }

    return 0;
}