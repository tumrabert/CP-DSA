#include <iostream>
#include <vector>
using namespace std;
int bin_search(int num,vector<int> arr){
    //if(num<=arr.front()){return -1;}
    //if(num>=arr.back()){return arr.back();}
    int l=0,r=arr.size()-1,m,result=-1;
    while(l<=r){
        m=l+(r-l)/2;

        if(num==arr[m]){
            return arr[m];
        }else if(num>=arr[m]){
            result=arr[m];
            l=m+1;
        }
        else{
            r=m-1;
        }

    }

return result;
}

int main() {
    int n,m;
    cin>>n>>m;
    vector<int> arr(n);
    for (int& num : arr) {
        cin >> num;
    }

    vector<int> queries(m);
    for (int& query : queries) {
        cin >> query;
    }

    for (int query : queries) {
        cout << bin_search(query, arr) <<endl;
    }
    return 0;
}