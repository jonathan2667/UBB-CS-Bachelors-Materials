#include "gui_vegetables.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    gui_vegetables w;
    w.show();
    return a.exec();
}
