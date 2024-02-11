#include <iostream>
#include <vector>
using namespace std;
int get_sum(vector<int>& S,int a,int b){
    if(a==0)return S[b];
    else return S[b]-S[a-1];
}
int mss(vector<int>& A,vector<int>& S,int start,int stop){
    if(start==stop) return A[start];
    int m=(start+stop)/2;

    int r1=mss(A,S,start,m);
    int r2=mss(A,S,m+1,stop);

    //ms left
    int msl=get_sum(S,m,m);
    for(int i=start;i<m;i++){
        msl=max(msl,get_sum(S,i,m));
    }
    int msr=get_sum(S,m+1,m+1);
    for(int j=m+2;j<=stop;j++){
        msr=max(msr,get_sum(S,m+1,j));
    }
    int r3=msl+msr;

    return max(max(r1,r2),r3);


}
int main() {
    // Variable declarations
    // Initialization (if needed)

    // Your code here

    // Output (if any)A
    int n;
    cin>>n;
    vector<int> A(n);
    vector<int> S(n);
    int sum=0,i=0;
    for(int& x:A){
        cin>>x;
        sum=sum+x;
        S[i]=sum;
        i++;
    }
    cout<<mss(A,S,0,A.size()-1);
    return 0;
}