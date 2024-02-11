#include <iostream>
#include <vector>
using namespace std;

// Function to calculate prefix sum difference and additional cost
long long P(const vector<long long>& S, int l, int M, long long k) {
    return S[M] - (l == 0 ? 0 : S[l - 1]) + (M - l + 1) * k;
}

// Function to find the cut using binary search
long long cut(const vector<long long>& S, int l, long long b, int n, long long k) {
    int L = 0, R = n - 1;
    int res = -1;
    while (L <= R) {
        int M = (L + R) / 2;
        if (P(S, l, M, k) <= b) {
            res = M;
            L = M + 1;
        } else {
            R = M - 1;
        }
    }
    return res == -1 ? 0 : S[res] - (l == 0 ? 0 : S[l - 1]);
}

int main() {
    int n, m;
    long long k;
    cin >> n >> m >> k;
    vector<long long> A(n), S(n);
    
    // Reading input and calculating prefix sums
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
        S[i] = A[i] + (i > 0 ? S[i - 1] : 0);
    }

    // Processing each query
    for (int i = 0; i < m; ++i) {
        int l;
        long long b;
        cin >> l >> b;
        // Adjusting for 0-based indexing if input is 1-based
        cout << cut(S, l, b, n, k) << endl;
    }

    return 0;
}
