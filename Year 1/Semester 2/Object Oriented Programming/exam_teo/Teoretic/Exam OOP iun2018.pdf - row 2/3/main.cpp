#include <iostream>
#include <vector>

using namespace std;

class SaleItem {
private:
    int code;
    double price;
public:
    SaleItem(int code, double price) : code(code), price(price) {}

    int getCode() const {
        return code;
    }

    double getPrice() const {
        return price;
    }
};

class Sale {
private:
    vector<SaleItem> items;
public:
    const vector<SaleItem> &getItems() const {
        return items;
    }
    void addItem(SaleItem si) {
        items.push_back(si);
    }
};

class Discount {
public:
    virtual double calc(Sale s) = 0;
    virtual ~Discount() = default;
};

class ItemDiscount: public Discount {
private:
    int code;
    int percentage;
public:
    ItemDiscount(int code, int percentage) : code(code), percentage(percentage) {}

    double calc(Sale s) override {
        double total = 0;
        for (auto si: s.getItems()) {
            if (si.getCode() == code)
                total += si.getPrice() * percentage / 100.0;
        }
        return total;
    }
};

class SumDiscount: public Discount {
private:
    vector<Discount*> discounts;
public:
    virtual ~SumDiscount() {
        for (auto d: discounts) {
            delete d;
        }
    }

    void add(Discount* d) { discounts.push_back(d); }

    double calc(Sale s) override {
        double total = 0;
        for (auto d: discounts) {
            total += d->calc(s);
        }
        return total;
    }
};


int main() {
    Sale s;
    s.addItem(SaleItem(0, 10));
    s.addItem(SaleItem(1, 150));
    s.addItem(SaleItem(2, 20));

    SumDiscount sd;
    sd.add(new ItemDiscount(0, 10));
    sd.add(new ItemDiscount(1, 15));
    cout << sd.calc(s);

    return 0;
}
