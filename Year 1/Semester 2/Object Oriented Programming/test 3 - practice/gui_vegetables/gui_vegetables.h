#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_gui_vegetables.h"
#include <QWidget>
#include <QListWidget>
#include <QLineEdit>
#include <QPushButton>
#include <QVBoxLayout>
#include <QLabel>
#include<Service.h>

class gui_vegetables : public QWidget
{
 
private:
    Ui::gui_vegetablesClass ui;

    Service service;
    QListWidget * listWithFamilies = new QListWidget();
    QListWidget* listWithVegetables = new QListWidget();
    QLabel* labelForVegetable = new QLabel("enter the name:");
    QPushButton* searchButton = new QPushButton("search");
    QLineEdit* consumableParts= new QLineEdit();
    QLineEdit* searchVegetableLine = new QLineEdit();
public:
    gui_vegetables(QWidget *parent = nullptr);

    void populate();
public slots:
    void populateListWithVegetables();
    void searchVegetable();

};
