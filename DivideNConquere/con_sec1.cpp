#include <iostream>
#include <vector>
using namespace std;

void permu(vector<int> &sol,vector<bool> &used,int len,int count,int n,int k,int mx) {
  if (len < n) {
    sol[len]=0;
    int c1=0,m1=max(mx,c1);
    permu(sol, used, len + 1, c1, n, k,m1);
    sol[len]=1;
    int c2=count+1,m2=max(mx,c2);
    permu(sol, used, len + 1, c2, n, k,m2);

    
    
  } 
  if(len==n&&mx>=k) {
    for (int i = 0;i < n;i++) {
      cout << sol[i];
    }
    cout << "\n";
    
  }
  return;
}


int main() {
    int n,k;
    cin>>n>>k;
    vector<int> sol(n);
    vector<bool> used(n);
    permu(sol,used,0,0,n,k,0);//n,sol,len,used,count

    return 0;
}