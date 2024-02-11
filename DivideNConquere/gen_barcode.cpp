#include <iostream>
#include <vector>
using namespace std;

void permu(vector<int> &sol,vector<bool> &used,int len,int count,int a,int b) {
  if (len < b) {
    sol[len]=0;
    permu(sol, used, len + 1, count, a, b);
    if (count < a) {
    sol[len]=1;
    permu(sol, used, len + 1, count+1, a, b);}

    
    
  } 
  if(len==b&&count==a) {
    for (int i = 0;i < b;i++) {
      cout << sol[i];
    }
    cout << "\n";
    
  }
  return;
}


int main() {
    int a,b;
    cin>>a>>b;
    vector<int> sol(b);
    vector<bool> used(b);
    permu(sol,used,0,0,a,b);//n,sol,len,used,count

    return 0;
}