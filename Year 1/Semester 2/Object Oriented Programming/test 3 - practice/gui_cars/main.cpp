#include "gui_cars.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    gui_cars w;
    w.show();
    return a.exec();
}
