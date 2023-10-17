#include "mainwindow.h"
#include <QApplication>
#include <QStyleFactory>
#include <QPalette>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    MainWindow mainWindow;

    app.setStyle(QStyleFactory::create("Fusion"));

    QPalette brightPalette;
    brightPalette.setColor(QPalette::Window, QColor(255, 204, 153)); // Основной цвет фона окон
    brightPalette.setColor(QPalette::WindowText, Qt::black); // Цвет текста
    brightPalette.setColor(QPalette::Text, Qt::black); // Цвет текста
    brightPalette.setColor(QPalette::Button, QColor(255, 128, 64)); // Цвет кнопок
    brightPalette.setColor(QPalette::ButtonText, Qt::black); // Цвет текста на кнопках
    brightPalette.setColor(QPalette::Base, QColor(255, 255, 255)); // Цвет фона для элементов ввода
    brightPalette.setColor(QPalette::AlternateBase, QColor(255, 204, 153)); // Цвет фона для альтернативных элементов
    brightPalette.setColor(QPalette::ToolTipBase, QColor(255, 102, 0)); // Цвет фона для подсказок
    brightPalette.setColor(QPalette::ToolTipText, Qt::white); // Цвет текста в подсказках

    app.setPalette(brightPalette);

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #ff6600; border: 1px solid white; }");

    mainWindow.setFixedSize(770, 500);
    mainWindow.setWindowTitle("Lab_2");

    mainWindow.show();

    return app.exec();
}
