#include <iostream>
#include <vector>

using namespace std;

// prints: "a b b a "
int main() {
    vector<string> str{"a", "b", "c", "d"};
    str.erase(str.begin() + 2); // str={"a", "b", "", "d"}
    vector<string>::iterator it = str.begin();
    str.insert(it + 2, "b"); // str={"a", "b", "b", "d"}
    str.insert(str.end() - 1, "a"); // str={"a", "b", "b", "a", "d"}
    str.pop_back(); // str={"a", "b", "b", "a"}
    it = str.begin();
    while (it != str.end()) {
        cout << *it << " ";
        it++;
    }
    return 0;
}
