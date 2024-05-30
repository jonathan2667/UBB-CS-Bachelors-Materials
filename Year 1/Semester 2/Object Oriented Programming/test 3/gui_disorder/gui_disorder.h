#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_gui_disorder.h"
#include <QWidget>
#include <QListWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QVBoxLayout>
#include "service.h"

class gui_disorder : public QWidget
{
    Q_OBJECT
private:
    Ui::gui_disorderClass ui;
    Service service;

    QListWidget* disordersList = new QListWidget();
    QLineEdit* searchDisorder = new QLineEdit();

    QLabel* labelForSymptoms = new QLabel("enter the Symptoms:");
    QLineEdit* searchSymptoms = new QLineEdit();
    QPushButton* searchButton = new QPushButton("Show Symptoms");
    QListWidget* symptomsList = new QListWidget();

public:
    gui_disorder(QWidget *parent = nullptr);
    ~gui_disorder();

    void populate();
public slots:
    void populateMatching();
    void showSymptoms();

};
