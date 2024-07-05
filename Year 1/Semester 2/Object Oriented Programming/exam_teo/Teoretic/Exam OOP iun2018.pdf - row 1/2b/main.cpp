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
    D(B* b) : b(*b) {}

    void f() override { b.f(); cout << "D.f "; }
    virtual ~D() { cout << "~D "; }

};

// prints: "B.f B.f D.f ~D ~B ~B "
int main() {
    B* b1 = new B{};
    b1->f();
    B* b2 = new D{b1};
    b2->f();
    delete b2;
    delete b1;

    return 0;
}
