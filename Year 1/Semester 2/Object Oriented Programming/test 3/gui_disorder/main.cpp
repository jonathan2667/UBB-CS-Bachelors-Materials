#include "gui_disorder.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    gui_disorder w;
    w.show();
    return a.exec();
}
