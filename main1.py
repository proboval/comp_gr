from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt
from form import Ui_new
import sys
from math import sin, cos, radians


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.remove_coordinate_system = False
        self.remove_axle = False
        self.scale = 1

        self.ui = Ui_new()
        self.ui.setupUi(self)

        geo = self.ui.pushButton_3.geometry()
        geo.setX(geo.x() - 30)
        self.ui.pushButton_3.setGeometry(geo)
        sizeBut = self.ui.pushButton_2.size()
        self.ui.pushButton_2.resize(sizeBut.width() + 20, sizeBut.height() + 10)

        sizeBut = self.ui.pushButton_3.size()
        self.ui.pushButton_3.resize(sizeBut.width() + 20, sizeBut.height() + 10)

        sizeBut = self.ui.pushButton.size()
        self.ui.pushButton.resize(sizeBut.width() + 20, sizeBut.height() + 10)

        sizeBut = self.ui.pushButton_2.size()

        self.ui.pushButton.clicked.connect(lambda: self.buttonClicked())
        self.ui.pushButton_2.setText("Убрать систему координат")
        self.ui.pushButton_2.clicked.connect(lambda: self.buttonClicked_1())
        self.ui.pushButton_3.clicked.connect(lambda: self.buttonClicked_2())
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Полярная система координат")
        self.show()

    def buttonClicked(self):
        if self.ui.pushButton.text() == "Убрать ось":
            self.ui.pushButton.setText("Вернуть ось")
        elif self.ui.pushButton.text() == "Вернуть ось":
            self.ui.pushButton.setText("Убрать ось")
        self.remove_axle = not self.remove_axle
        self.update()

    def buttonClicked_1(self):
        if self.ui.pushButton_2.text() == "Убрать систему координат":
            self.ui.pushButton_2.setText("Вернуть систему координат")
        elif self.ui.pushButton_2.text() == "Вернуть систему координат":
            self.ui.pushButton_2.setText("Убрать систему координат")
        self.remove_coordinate_system = not self.remove_coordinate_system
        self.update()

    def buttonClicked_2(self):
        self.scale = self.ui.spinBox.value()
        self.update()

    def paintEvent(self, e):
        size = self.size()
        qp = QPainter()
        qp.begin(self)

        pen = QPen(Qt.black, 2)
        brush = QBrush(Qt.lightGray)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawRect(10, 5, size.width() - 20, 260 - 15)

        pen1 = QPen(Qt.darkCyan, 1)
        brush1 = QBrush()
        qp.setBrush(brush1)
        qp.setPen(pen1)
        dx = 30 * self.scale
        n = round(size.width() / (dx * 2))

        s = 1
        for i in range(1, n + 1):
            if dx * i < 250:
                qp.drawEllipse(size.width() // 2 - (dx / 2) * i, 250 // 2 - (dx / 2) * i, dx * i, dx * i)
                s += 1

        hypotenuse = dx * (n // 2)
        x_start = size.width() // 2
        y_start = 250 // 2
        s = 30
        for i in range(1, 13):
            pen = QPen(Qt.red)
            pen1 = QPen(Qt.black)
            if (30 * i) % 90 == 0 or not self.remove_axle:
                qp.drawLine(x_start, y_start, x_start + cos(radians(30 * i)) * hypotenuse, y_start + sin(radians(30 * i)) *
                            hypotenuse)
            qp.setPen(pen)

            if not self.remove_coordinate_system:
                qp.drawText(x_start + cos(radians(30 * i)) * hypotenuse, y_start + sin(radians(30 * i)) * hypotenuse + 4,
                            str(360 - 30 * i))
            qp.setPen(pen1)

        for i in range(4):
            pen = QPen(Qt.red)
            pen1 = QPen(Qt.black)
            if not self.remove_axle:
                qp.drawLine(x_start, y_start, x_start + cos(radians(45 + (90 * i))) * hypotenuse, y_start + sin(radians(45 +
                            90 * i)) * hypotenuse)
            qp.setPen(pen)

            if not self.remove_coordinate_system and not self.remove_axle:
                qp.drawText(x_start + cos(radians(45 + (90 * i))) * hypotenuse, y_start + sin(radians(45 + (90 * i))) * hypotenuse + 4,
                            str(360 - (45 + 90 * i)))
            qp.setPen(pen1)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = mywindow()

    sys.exit(app.exec())