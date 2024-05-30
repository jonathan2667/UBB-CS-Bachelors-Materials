#include "gui_cars.h"
#include<fstream>

//schimbare Qmainwindow, extindere clasa

gui_cars::gui_cars(QWidget* parent) : QWidget(parent)
{
    //ui.setupUi(this);
    QVBoxLayout* mainLayout = new QVBoxLayout();
    mainLayout->addWidget(listWidgetAllCars);

    mainLayout->addWidget(searchByManufacturerLineEdit);
    mainLayout->addWidget(searchByManufacturerButton);
    mainLayout->addWidget(numberOfCarsLabel);
    mainLayout->addWidget(listWidgetFilteredCars);

    populateListWidgetAllCars();
    setLayout(mainLayout);


    QObject::connect(searchByManufacturerLineEdit, &QLineEdit::textChanged, this, &gui_cars::searchByManufacturer);
    QObject::connect(searchByManufacturerButton, &QPushButton::clicked, this, &gui_cars::searchByManufacturer);
    QObject::connect(searchByManufacturerLineEdit, &QLineEdit::returnPressed, this, &gui_cars::searchByManufacturer);
}

gui_cars::~gui_cars()
{}

void gui_cars::populateListWidgetAllCars() {
    for (auto car : service.getAllCars()) {
        listWidgetAllCars->addItem(QString::fromStdString(car.toString()));

        this->listWidgetAllCars->item(this->listWidgetAllCars->count() - 1)->setForeground(
            QColor(QString::fromStdString(car.getColor())));

    }
}


void gui_cars::searchByManufacturer() {
    string manufacturer = searchByManufacturerLineEdit->text().toStdString();
    listWidgetFilteredCars->clear();
    vector<Car> filteredCars = service.getCarsByManufacturer(manufacturer);
    for (auto car : filteredCars)
         this->listWidgetFilteredCars->addItem(QString::fromStdString(car.toString()));
    numberOfCarsLabel->setText(QString::fromStdString("Number of cars: " + to_string(filteredCars.size())));
} 