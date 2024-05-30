

#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_gui_cars.h"
#include "Service.h"
#include <QWidget>
#include <QListWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QVBoxLayout>

class gui_cars : public QWidget
{
    Q_OBJECT
private:
    Ui::gui_carsClass ui;
    Service service;
    QListWidget* listWidgetAllCars = new QListWidget();
    
    QLineEdit* searchByManufacturerLineEdit = new QLineEdit();
    QPushButton* searchByManufacturerButton = new QPushButton("Search after manufacturer:");
    QLabel* numberOfCarsLabel = new QLabel("Number of cars:");
    QListWidget* listWidgetFilteredCars = new QListWidget();

public:
    gui_cars(QWidget* parent = nullptr);
    ~gui_cars();
    void populateListWidgetAllCars();
public slots:
    void searchByManufacturer();

};
