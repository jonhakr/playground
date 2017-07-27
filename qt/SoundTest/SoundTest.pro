#-------------------------------------------------
#
# Project created by QtCreator 2017-02-22T09:01:28
#
#-------------------------------------------------

QT       += core gui multimedia

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = SoundTest
TEMPLATE = app


SOURCES += main.cpp\
        playerdialog.cpp

HEADERS  += playerdialog.h

FORMS    += playerdialog.ui

INSTALLS += \
    target

target.path = /home/pi
target.files += TARGET
