#include <iostream>
#include <vector>

using namespace std;

template <typename T>
class Adder {
private:
    vector<T> v;
public:
    Adder(const T& t) { v.push_back(t); }

    Adder& operator+(const T& t) {
        v.push_back(t);
        return *this;
    }

    Adder& operator++() {
        if (v.empty())
            throw std::runtime_error("No values!");
        v.push_back(v.back());
        return *this;
    }

    Adder& operator--() {
        if (v.empty())
            throw std::runtime_error("No more values!");
        v.pop_back();
        return *this;
    }

    T sum() const {
        T total{};
        for (const auto &t: v) {
            total += t;
        }
        return total;
    }
};

void function2() {
    Adder<int> add{5};
    add = add + 5 + 2;
    ++add;
    add + 8;
    cout << add.sum() << "\n";
    --add;
    cout << add.sum() << "\n";
    --(--add);
    cout << add.sum() << "\n";
    try {
        --(--(--add));
    }
    catch (runtime_error& ex) {
        cout << ex.what();
    }
}

int main() {
    function2();

//    return 0;
}
