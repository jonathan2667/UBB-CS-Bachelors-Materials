#include <iostream>

using namespace std;

class Channel {
public:
    virtual void send() const noexcept(false) = 0;
    virtual ~Channel() = default;
};

class Telephone: public Channel {
private:
    string number;
public:
    Telephone(const string &number) : number(number) {}
    virtual void send() const noexcept(false) override {
        if (rand() % 10 < 5)
            throw std::exception();
        fprintf(stdout, "dialling %s\n", number.c_str());
    }
};

class Fax: public Telephone {
public:
    Fax(const string &number) : Telephone(number) {}
    void send() const noexcept(false) override {
        Telephone::send();
        cout << "sending fax\n";
    }
};

class SMS: public Telephone {
public:
    SMS(const string &number) : Telephone(number) {}
    void send() const noexcept(false) override {
        Telephone::send();
        cout << "sending sms\n";
    }
};

class Failover: public Channel {
private:
    Channel* c1, *c2;
public:
    Failover(Channel *c1, Channel *c2) : c1(c1), c2(c2) {}
    ~Failover() { delete c1; delete c2; }
    void send() const noexcept(false) override {
        try { c1->send(); }
        catch (std::exception&) { c2->send(); }
    }
};

class Contact {
private:
    Channel *c1, *c2, *c3;
public:
    Contact(Channel *c1, Channel *c2, Channel *c3) : c1(c1), c2(c2), c3(c3) {}
    ~Contact() { delete c1; delete c2; delete c3; }
    void sendAlarm() const noexcept(true) {
        while (true) {
            try { c1->send(); return; }
            catch (std::exception&) {
                try { c2->send(); return; }
                catch (std::exception&) {
                    try { c3->send(); return; }
                    catch (std::exception& e) { /*throw e;*/ } // should sendAlarm() throw or not?
                }
            }

            // another way of writing it
            try { c1->send(); return; }
            catch (std::exception&) {}
            try { c2->send(); return; }
            catch (std::exception&) {}
            try { c3->send(); return; }
            catch (std::exception&e) { /*throw e;*/ }
        }
    }
};

Contact* createContact(string number) {
    auto c1 = new Telephone(number);
    auto c2 = new Failover(new Fax(number),
                           new SMS(number)
                           );
    auto c3 = new Failover(new Telephone(number),
                           new Failover(new Fax(number),
                                        new SMS(number)
                           )
                           );
    return new Contact(c1, c2, c3);
}

int main() {
    srand(time(nullptr));
    auto c = createContact("112");
    c->sendAlarm();
    delete c;

    return 0;
}
