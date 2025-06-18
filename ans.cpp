#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n , k , p ;
    cin>> n >> k >> p ; 
    float ans = float(k) / float(p);
    ans = ceill( abs(ans));
    cout << ans << endl;
}