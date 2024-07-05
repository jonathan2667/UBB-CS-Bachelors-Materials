#include <iostream>
#include <vector>

using namespace std;
// start: 16:21 - 16:40~


class Expression {
public:
    virtual double evaluate() const = 0;
    virtual ~Expression() = default;
};

class Constant: public Expression {
private:
    double value;
public:
    Constant(double value) : value(value) {}

    double evaluate() const override {
        return value;
    }
};

class UnaryExpression: public Expression {
private:
    Expression* expression;
public:
    UnaryExpression(Expression *expression) : expression(expression) {}

    virtual double evaluate() const override {
        return expression->evaluate();
    }

    virtual ~UnaryExpression() { delete expression; }
};

class Negate: public UnaryExpression {
public:
    Negate(Expression *expression) : UnaryExpression(expression) {}

    double evaluate() const override {
        return -UnaryExpression::evaluate();
    }
};

class BinaryExpression: public UnaryExpression {
protected:
    Expression* left;
    Expression* right;
public:
    BinaryExpression(Expression *left, Expression *right) : UnaryExpression(nullptr), left(left), right(right) {}

    virtual ~BinaryExpression() {
        delete left;
        delete right;
    }
};

class Adder: public BinaryExpression {
public:
    Adder(Expression *left, Expression *right) : BinaryExpression(left, right) {}

    double evaluate() const override {
        return left->evaluate() + right->evaluate();
    }
};

class Subtracter: public BinaryExpression {
public:
    Subtracter(Expression *left, Expression *right) : BinaryExpression(left, right) {}

    double evaluate() const override {
        return left->evaluate() - right->evaluate();
    }
};

class MathHomework {
private:
    vector<Expression*> v;
public:
    void addExpression(Expression *expression) {
        v.push_back(expression);
    }

    ~MathHomework() {
        for (auto e: v) {
            delete e;
        }
    }

    auto getResults() const {
        vector<double> r;
        for (auto e: v) {
            r.push_back(e->evaluate());
        }
        return r;
    }
};

int main() {
    MathHomework mh;

    // -5 + (9 - 3) = -5 + 6 = 1
    mh.addExpression(new Adder(
            new Negate(new Constant(5)),
            new Subtracter(
                    new Constant(9),
                    new Constant(3))));

    mh.addExpression(new Subtracter(
            new Negate(new Adder(
                    new Constant(4),
                    new Constant(2))),
            new Negate(new Constant(10))));

    // -(4 + 2) - (-10) = - 6 + 10 = 4
    for (auto r: mh.getResults()) {
        cout << r << " ";
    }

    return 0;
}
