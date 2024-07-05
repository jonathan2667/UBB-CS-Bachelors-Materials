#include <iostream>

using namespace std;

class B {
public:
    B() {}
    B(const B& b) { cout << "copy "; }
    virtual void f() { cout << "B.f "; }
    void g(B b) { cout << "B.g "; }
    virtual ~B() { cout << "~B "; }
};

class D: public B {
public:
    D() {}
    void f() { B::f(); cout << "D.f "; }
    void g(D d) { B::g(d); cout << "D.g "; }
};

// prints: "B.f D.f copy B.g ~B ~B ~B"
int main() {
    B* b = new B{};
    B* d = new D{};
    d->f();
    d->g(*b);
    delete b;
    delete d;

    return 0;
}
