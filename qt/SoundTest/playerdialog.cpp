#include "playerdialog.h"
#include "ui_playerdialog.h"
#include <QFileInfo>
#include <QStandardPaths>

PlayerDialog::PlayerDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::PlayerDialog)
{
    ui->setupUi(this);
    QString extFileLocation = QStandardPaths::locate(QStandardPaths::HomeLocation,
                                                QString(),
                                                QStandardPaths::LocateDirectory);
    oggSound = new QSound(extFileLocation + "finish_first.ogg", this);
    wavSound = new QSound(extFileLocation + "finish_first.wav", this);
    mp3Player = new QMediaPlayer(this);
    mp3Player->setMedia(QUrl::fromLocalFile(extFileLocation + "/39-boulder-canyon.mp3"));

}

PlayerDialog::~PlayerDialog()
{
    delete ui;
}

void PlayerDialog::on_pb_ogg_clicked()
{
    oggSound->play();
}

void PlayerDialog::on_pb_wav_clicked()
{
    wavSound->play();
}

void PlayerDialog::on_pb_mp3_clicked()
{
    switch (mp3Player->state())
    {
    case QMediaPlayer::StoppedState:
        mp3Player->play();
        break;
    case QMediaPlayer::PlayingState:
        mp3Player->stop();
        mp3Player->setPosition(0);
    default:
        break;
    }
}
