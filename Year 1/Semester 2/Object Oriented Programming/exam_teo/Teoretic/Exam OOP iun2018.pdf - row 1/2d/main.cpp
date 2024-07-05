#include <iostream>
#include <vector>

using namespace std;


// prints: "a b b a "
int main() {
    vector<string> str{"a", "b", "c", "d"};
    vector<string>::iterator it = str.end();
    it--;
    *it = "a";
    it--;
    str.erase(it);
    str.insert(it, "b");
    for (it = str.begin(); it != str.end(); it++) {
        cout << *it << " ";
    }

    return 0;
}
