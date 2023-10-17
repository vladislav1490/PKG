#include <QFileDialog>
#include <QPushButton>
#include <QVBoxLayout>
#include <QDir>
#include <QImageWriter>
#include <QImage>
#include <QFileInfo>

#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{

    tableWidget = new QTableWidget(this);
    tableWidget->setColumnCount(5);
    tableWidget->setHorizontalHeaderLabels({"Имя файла", "Размер изображения (px)", "Разрешение (dpi)", "Глубина цвета", "Сжатие"});

    for (int i = 0; i < 5; i++) {
        tableWidget->setColumnWidth(i, 150);
    }

    QVBoxLayout *layout = new QVBoxLayout;

    QWidget *buttonContainer = new QWidget(this);
    QVBoxLayout *buttonLayout = new QVBoxLayout;
    QPushButton *openButton = new QPushButton("Выбрать папку", this);
    connect(openButton, &QPushButton::clicked, this, &MainWindow::openFolder);
    buttonLayout->addWidget(openButton);
    buttonContainer->setLayout(buttonLayout);

    layout->addWidget(tableWidget);
    layout->addWidget(buttonContainer);

    QWidget *centralWidget = new QWidget(this);
    centralWidget->setLayout(layout);
    setCentralWidget(centralWidget);
}


void MainWindow::openFolder()
{
    QString folderPath = QFileDialog::getExistingDirectory(this, "Select Folder");

    if (!folderPath.isEmpty()) {
        processImages(folderPath);
    }
}

void MainWindow::processImages(const QString &folderPath)
{
    QDir directory(folderPath);
    QStringList nameFilters = {"*.jpg", "*.gif", "*.tif", "*.bmp", "*.png", "*.pcx"};
    QStringList imageFiles = directory.entryList(nameFilters, QDir::Files);

    tableWidget->setRowCount(imageFiles.size());

    for (int i = 0; i < imageFiles.size(); ++i) {
        QString filePath = directory.filePath(imageFiles[i]);
        QImage image(filePath);
        QImageWriter imageWriter(filePath);

        QTableWidgetItem *fileNameItem = new QTableWidgetItem(imageFiles[i]);
        QTableWidgetItem *sizeItem = new QTableWidgetItem(QString("%1 x %2").arg(image.width()).arg(image.height()));
        QTableWidgetItem *resolutionItem = new QTableWidgetItem(QString("%1 x %2").arg(image.dotsPerMeterX() * 0.0254).arg(image.dotsPerMeterY() * 0.0254));
        QTableWidgetItem *colorDepthItem = new QTableWidgetItem(QString::number(image.depth()));
        QTableWidgetItem *compressionItem = new QTableWidgetItem(QString::number(imageWriter.compression()));

        fileNameItem->setForeground(QColor(255, 0, 0));
        sizeItem->setForeground(QColor(0, 0, 255));
        resolutionItem->setForeground(QColor(0, 128, 0));
        colorDepthItem->setForeground(QColor(255, 165, 0));
        compressionItem->setForeground(QColor(128, 0, 128));

        tableWidget->setItem(i, 0, fileNameItem);
        tableWidget->setItem(i, 1, sizeItem);
        tableWidget->setItem(i, 2, resolutionItem);
        tableWidget->setItem(i, 3, colorDepthItem);
        tableWidget->setItem(i, 4, compressionItem);
    }

    tableWidget->scrollToBottom();
}
