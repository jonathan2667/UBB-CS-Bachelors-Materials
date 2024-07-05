#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

template<typename T>
T fct(vector<T> v) {
    if (v.empty())
        throw exception{};
//    return accumulate(v.begin() + 1, v.end(), v[0], std::max); // doesn't work
//    return accumulate(v.begin() + 1, v.end(), v[0], [](T a, T b) { return max(a, b); }); // works
    return *max_element(begin(v), end(v)); // works
//    return *max_element(v.begin(), v.end());
}

void testFct() {
    vector<int> v1{4, 2, 1, 6, 3, -4};
    assert(fct<int>(v1) == 6);
    vector<int> v2;
    try {
        fct<int>(v2);
        assert(false);
    }
    catch (std::exception&) {
        assert(true);
    }

    vector<double> v3{2, 10.5, 6.33, -100, 9, 1.212};
    assert(fct<double>(v3) == 10.5);

    vector<string> v4{"y", "q", "a", "m"};
    assert(fct<string>(v4) == "y");
}

int main() {
    testFct();
    return 0;
}
