#include <iostream>

using namespace std;

int except(bool ex) {
    if (ex)
        throw 10;
    cout << "Finished function." << endl;
}


// prints: "1 10 40 "
int main() {
    cout << 1 << " ";
    try {
        cout << except(true) << " ";
        cout << except(5 < 5) << " ";
    }
    catch (int& ex) {
        cout << ex << " ";;
    }
    cout << 40 << " ";
    return 0;
}
