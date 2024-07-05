#include <iostream>

using namespace std;

int fct(string v) {
    if (v == "") { throw string{"2"}; }
    cout << "1 ";
    if (v.size() > 4) { throw std::runtime_error{"Not empty"}; }
    return 0;
}

// prints: "1 0 1 Not empty"
int main() {
    try {
        cout << fct("Hi") << " ";
        cout << fct("Hello") << " ";
        cout << fct("") << " ";
    }
    catch (string& e) {
        cout << e;
    }
    catch (std::runtime_error& e) {
        cout << e.what();
    }
    return 0;
}
