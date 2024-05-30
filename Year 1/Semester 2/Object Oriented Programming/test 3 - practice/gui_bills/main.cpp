#include "gui_bills.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    gui_bills w;
    w.show();
    return a.exec();
}
