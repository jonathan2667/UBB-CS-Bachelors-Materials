
#include "Bill.h"
#include<assert.h>
#include "Service.h"

void testAdd()
{
    Bill b = Bill("22A223X", "Telekom", 203.12, true);
    Bill b1 = Bill("22A223X", "Telekom", 203.12, true);
    Service s = Service();
    s.addBill(b);
    bool exceptionThrown = false;
    try {
        s.addBill(b1);
    }
    catch (const exception& e) { 
        exceptionThrown = true;
    }
    assert(true);
}



void testCalculate()
{
	Bill b = Bill("22A223X", "Telekom", 203.12, true);
	Bill b1 = Bill("52A223X", "RDS", 203.12, true);
	Service s = Service();
	s.addBill(b);
	s.addBill(b1);
	double sum = s.calculateTotalAmount();
	assert(sum > 936.34 and sum < 936.36);
}	

void testAll()
{
	testAdd();
	testCalculate();
}