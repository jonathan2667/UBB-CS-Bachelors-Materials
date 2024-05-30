#include "gui_bills.h"

gui_bills::gui_bills(QWidget *parent)
    : QMainWindow(parent)
{
   

    this->setWindowTitle("Bills");

    QVBoxLayout* mainLayout = new QVBoxLayout;  // Layout to manage widgets vertically

    // Initialize all widgets
    this->billsListWidget = new QListWidget;
    this->sortBills = new QPushButton("Sort the bills");
    this->userInputLabel = new QLabel("Enter the name of the company");
    this->userInput = new QLineEdit;
    this->calculateAmountOfUnpaidBill = new QPushButton("Calculate amount of bills");
    this->calculateAmountLabel = new QLabel("Total amount");
    this->totalAmount = new QLineEdit;

    // Add widgets to the layout
    mainLayout->addWidget(billsListWidget);
    mainLayout->addWidget(sortBills);
    mainLayout->addWidget(userInputLabel);
    mainLayout->addWidget(userInput);
    mainLayout->addWidget(calculateAmountOfUnpaidBill);
    mainLayout->addWidget(calculateAmountLabel);
    mainLayout->addWidget(totalAmount);

    // Create central widget and set the layout to it
    QWidget* centralWidget = new QWidget(this);
    centralWidget->setLayout(mainLayout);
    this->setCentralWidget(centralWidget);

    // Connect signals to slots
    connect(sortBills, &QPushButton::clicked, this, &gui_bills::loadSortedBills);
    connect(calculateAmountOfUnpaidBill, &QPushButton::clicked, this, &gui_bills::showAmountOfBills);

    // Load initial bills list
    this->loadBills();
    
}

gui_bills::~gui_bills()
{}

void gui_bills::loadBills()
{
    this->billsListWidget->clear();
    for (auto bill : this->service.getBills())
        this->billsListWidget->addItem(QString::fromStdString(bill.toString()));
}

void gui_bills::loadSortedBills() {
    this->billsListWidget->clear();
    for (auto bill : this->service.getBillsSorted())
        this->billsListWidget->addItem(QString::fromStdString(bill.toString()));
}

void gui_bills::showAmountOfBills() {
    string company = this->userInput->text().toStdString();
    this->totalAmount->setText(QString::number(this->service.calculateAmountOfBillsFromCompany(company)));
}