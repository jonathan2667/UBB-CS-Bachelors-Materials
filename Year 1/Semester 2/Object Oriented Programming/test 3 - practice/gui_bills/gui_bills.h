#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_gui_bills.h"
#include "service.h"
#include <QWidget>
#include <QListWidget>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>


class gui_bills : public QMainWindow
{
    Q_OBJECT

public:
    gui_bills(QWidget *parent = nullptr);
    ~gui_bills();

    Service service;
    QListWidget *billsListWidget;
    QPushButton* sortBills;
    QLabel* userInputLabel;
    QLineEdit* userInput;
    QPushButton* calculateAmountOfUnpaidBill;
    QLabel* calculateAmountLabel;
    QLineEdit* totalAmount;

private:
    Ui::gui_billsClass ui;
    void loadBills();

public slots:
    void loadSortedBills();
    void showAmountOfBills();
};
