#include <iostream>
#include <vector>

using namespace std;

class SaleItem {
private:
    int code;
    double price;
public:
    SaleItem(int code, double price) : code(code), price(price) {}
    int getCode() const { return code; }
    double getPrice() const { return price; }
};


class Sale {
private:
    vector<SaleItem> v;
public:
    void add(SaleItem si) { v.push_back(si); }
    auto get() const { return v; }
};

class Discount {
public:
    virtual ~Discount() = default;
    virtual double calc(Sale s) const = 0;
};

class ItemDiscount: public Discount {
private:
    int code;
    int percentage;
public:
    ItemDiscount(int code, int percentage) : code(code), percentage(percentage) {}

    double calc(Sale s) const override {
        auto total = 0.0;
        for (auto si: s.get()) {
            if (si.getCode() == code) {
                total += si.getPrice() * percentage / 100.0;
            }
        }
        return total;
    }
};


class SumDiscount: public Discount {
private:
    vector<Discount*> v;
public:
    ~SumDiscount() { for (auto d: v) delete d; }
    void add(Discount* d) { v.push_back(d); }

    double calc(Sale s) const override {
        auto total = 0.0;
        for (auto d: v) {
            total += d->calc(s);
        }
        return total;
    }
};

int main() {
    Sale s;
    s.add(SaleItem(0, 10));
    s.add(SaleItem(1, 150));
    s.add(SaleItem(2, 14));
    SumDiscount sd;
    sd.add(new ItemDiscount(0, 10)); // 10% of 10 = 1
    sd.add(new ItemDiscount(1, 15)); // 15% of 150 = 22.5
    cout << sd.calc(s);

    return 0;
}
