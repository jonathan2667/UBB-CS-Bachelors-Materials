#include "gui_vegetables.h"

gui_vegetables::gui_vegetables(QWidget *parent)
    : QWidget(parent)
{
    QVBoxLayout* mainLayout = new QVBoxLayout();

    mainLayout->addWidget(listWithFamilies);
    mainLayout->addWidget(labelForVegetable);
    mainLayout->addWidget(searchVegetableLine);
    mainLayout->addWidget(searchButton);
    mainLayout->addWidget(listWithVegetables);
    mainLayout->addWidget(consumableParts);
    setLayout(mainLayout);
    
    populate();
    QObject::connect(listWithFamilies, &QListWidget::currentItemChanged, this, &gui_vegetables::populateListWithVegetables);
    QObject::connect(searchButton, &QPushButton::clicked, this, &gui_vegetables::searchVegetable);
    QObject::connect(searchVegetableLine, &QLineEdit::textChanged, this, &gui_vegetables::searchVegetable);
}

void gui_vegetables::populate() {
    listWithFamilies->clear();
    vector<string> families = service.getAllUniqueFamilies();

    for (auto f : families) {
        listWithFamilies->addItem(QString::fromStdString(f));
    }
}

void gui_vegetables::populateListWithVegetables() {
    string family = listWithFamilies->currentItem()->text().toStdString();
    listWithVegetables->clear();
    for (auto v : service.getAllVegetablesBelongingToFamily(family))
        this->listWithVegetables->addItem(QString::fromStdString(v.toString()));
}

void gui_vegetables::searchVegetable() {
    string name = searchVegetableLine->text().toStdString();
    Vegetables veg = service.getVegetableFromName(name);
    string family = veg.getFamily();
    consumableParts->setText(QString::fromStdString(veg.getList()));

    for (int i = 0; i < listWithFamilies->count(); i++) {
        if (this->listWithFamilies->item(i)->text().toStdString() == family)
            this->listWithFamilies->item(i)->setBackground(QBrush(Qt::red));
        else
            this->listWithFamilies->item(i)->setForeground(QColor(QString::fromStdString("White")));
    }
}