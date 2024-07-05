#include <iostream>

using namespace std;

template<typename T, typename U>
U fct2(T a, T b, U x, U y) {
    cout << a << " ";
    cout << b << " ";
    if (a == b)
        return x + y;
    return x;
}

class A {
    int a;
public:
    A(int a_) : a(a_) {}
};

// doesn't compile because class A doesn't have a '+' operator and a stream insertion operator
int main() {
    cout << fct2<int, int>(10, 10, 5, 5) << " ";
    cout << fct2<double, int>(10, 10.5, 5, 5) << " ";
    cout << fct2<int, string>(-2, -2, "Good ", "luck!") << " ";
    cout << fct2<int, A>(-2, -2, A{2}, A{3}) << " ";

    return 0;
}
