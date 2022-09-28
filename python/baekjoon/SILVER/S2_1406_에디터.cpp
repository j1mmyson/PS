#include <iostream>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;

stack<char> l, r;
string input = "";
int n;

int main() {
    getline(cin, input);
    cin >> n;

    for (int i = 0; i < input.length(); i++) {
        l.push(input[i]);
    }

    for (int i = 0; i < n; i++) {
        char cmd, item;
        cin >> cmd;

        switch (cmd) {
        case 'P':
            cin >> item;
            l.push(item);
            break;
        
        case 'L':
            if (l.empty()) continue;
            
            r.push(l.top());
            l.pop();
            break;
        case 'D':
            if (r.empty()) continue;
            
            l.push(r.top());
            r.pop();
            break;
        case 'B':
            if (l.empty()) continue;

            l.pop();
            break;
        }
    }

    while (!l.empty()) {
        r.push(l.top());
        l.pop();
    }
    while (!r.empty()) {
        cout << r.top();
        r.pop();
    }
}
