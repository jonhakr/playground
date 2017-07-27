#ifndef PLAYERDIALOG_H
#define PLAYERDIALOG_H

#include <QDialog>
#include <QSound>
#include <QMediaPlayer>
#include <QDir>

namespace Ui {
class PlayerDialog;
}

class PlayerDialog : public QDialog
{
    Q_OBJECT

public:
    explicit PlayerDialog(QWidget *parent = 0);
    ~PlayerDialog();

private slots:
    void on_pb_ogg_clicked();

    void on_pb_wav_clicked();

    void on_pb_mp3_clicked();

private:
    Ui::PlayerDialog *ui;
    QDir audioDir;
    QSound *oggSound;
    QSound *wavSound;
    QMediaPlayer *mp3Player;
};

#endif // PLAYERDIALOG_H
