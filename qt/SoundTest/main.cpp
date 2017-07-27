#include "playerdialog.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    PlayerDialog w;
    w.show();

    return a.exec();
}
