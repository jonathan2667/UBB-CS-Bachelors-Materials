#include <iostream>

using namespace std;

class B {
public:
    virtual void f() { cout << "B.f "; }
    virtual ~B() { cout << "~B "; }
};


class D: public B {
private:
    B& b;
public:
    D(B &b_) : b(b_) { cout << "D "; b.f(); }

    void f() override { cout << "D.f "; }
    ~D() { cout << "~D "; }
};

// prints: "B.f D B.f D.f ~D ~B ~B "
int main() {
    B* b1 = new B{};
    b1->f();
    B* b2 = new D{*b1};
    b2->f();
    delete b2;
    delete b1;

    return 0;
}
