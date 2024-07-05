#include <iostream>

using namespace std;

string except(int x) {
    if (x < 0) {
        throw string{"Negative "};
    }
    return "Positive ";
}

// prints: "One Positive Negative  "
int main() {
    cout << "One ";
    try {
        cout << except(3);
        cout << except(-2);
        cout << except(5);
    }
    catch (string& ex) { cout << ex << " "; }

    return 0;
}
