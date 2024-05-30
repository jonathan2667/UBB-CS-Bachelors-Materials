#include "gui_disorder.h"

gui_disorder::gui_disorder(QWidget *parent)
    : QWidget(parent)
{
    QVBoxLayout* mainLayout = new QVBoxLayout();

    mainLayout->addWidget(disordersList);
    mainLayout->addWidget(searchDisorder);
    mainLayout->addWidget(labelForSymptoms);
    mainLayout->addWidget(searchSymptoms);
    mainLayout->addWidget(searchButton);
    mainLayout->addWidget(symptomsList);

    setLayout(mainLayout);

    populate();
    QObject::connect(searchDisorder, &QLineEdit::textChanged, this, &gui_disorder::populateMatching);
    QObject::connect(searchButton, &QPushButton::clicked, this, &gui_disorder::showSymptoms);
}


void gui_disorder::showSymptoms() {
    symptomsList->clear();
    vector<Disorder> disorders = service.getAllDisorders();


    string name = searchSymptoms->text().toStdString();
    vector<string> allSymptoms = service.getAllSymptomsFromName(name);


   
    int cnt = 0;
    for (auto f : allSymptoms) {
        cnt++;
        symptomsList->addItem(QString::fromStdString(f));
    }

    
    if (cnt == 0) {
        symptomsList->addItem(QString::fromStdString("Errors, nothing"));
    }
}

void gui_disorder::populateMatching() {
    disordersList->clear();
    vector<Disorder> disorders = service.getAllDisorders();

    for (auto f : disorders) {
        string line = searchDisorder->text().toStdString();
        if (f.getCategory().find(line) != std::string::npos or f.getName().find(line) != std::string::npos)
            disordersList->addItem(QString::fromStdString(f.toString()));
    }
}

gui_disorder::~gui_disorder()
{}

void gui_disorder::populate() {
    disordersList->clear();
    vector<Disorder> disorders = service.getAllDisorders();

    for (auto f : disorders) {
        disordersList->addItem(QString::fromStdString(f.toString()));
    }
}