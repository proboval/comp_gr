from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtCore import Qt
from form import Ui_Form
import numpy as np
import sys


def x(t, r, a):
    return r * t - a * np.sin(t)


def y(t, r, a):
    return r - a * np.cos(t)


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.r = 1
        self.a = 1
        self.remove_coordinate_system = False
        self.remove_axle = False
        self.scale = 1

        self.ui = Ui_Form()
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
        self.ui.pushButton_4.clicked.connect(lambda: self.buttonClicked_3())
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Декартова система координат")
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
        self.scale = self.ui.doubleSpinBox.value()
        self.update()

    def buttonClicked_3(self):
        self.a = self.ui.doubleSpinBox_3.value()
        self.r = self.ui.doubleSpinBox_2.value()
        self.update()

    def paintEvent(self, e):
        t_array = np.linspace(-6 * np.pi, 6 * np.pi, 6000)
        cykloid_x = x(t_array, self.r, self.a)
        cykloid_y = y(t_array, self.r, self.a)

        size = self.size()
        dx = int(round(30 * self.scale))
        qp = QPainter()
        qp.begin(self)
        x0 = size.width() / 2
        y0 = (size.height() - 140) / 2
        for i in range(len(cykloid_x)):
            cykloid_x[i] = x0 + cykloid_x[i] * dx
            cykloid_y[i] = y0 - cykloid_y[i] * dx

        pen = QPen(Qt.black, 2)
        brush = QBrush(Qt.white)
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawRect(10, 5, size.width() - 20, size.height() - 150)

        pen1 = QPen(Qt.black, 1)
        brush1 = QBrush()
        qp.setBrush(brush1)
        qp.setPen(pen1)

        n = round(size.width() / 2 / dx)

        for i in range(0, n):
            if i == 0 and not self.remove_axle:
                qp.setPen(QPen(Qt.red))
                qp.drawLine(x0 + dx * i, 5, x0 + dx * i, size.height() - 145)
                qp.drawLine(x0 + dx * i, 5, x0 + dx * i - 4, 5 + 8)
                qp.drawLine(x0 + dx * i, 5, x0 + dx * i + 4, 5 + 8)
                if not self.remove_coordinate_system:
                    qp.drawText(x0 + dx * i + 4, 5 + 8, "y")
                qp.setPen((QPen(Qt.black)))
            else:
                qp.drawLine(x0 + dx * i, 5, x0 + dx * i, size.height() - 145)
                qp.drawLine(x0 - dx * i, 5, x0 - dx * i, size.height() - 145)

        k = ((size.height() - 140) // 2) // dx

        for i in range(0, k + 1):
            if i == 0 and not self.remove_axle:
                qp.setPen(QPen(Qt.red))
                qp.drawLine(10, y0 + dx * i, size.width() - 10, y0 + dx * i)
                qp.drawLine(size.width() - 10, y0 + dx * i, size.width() - 18, y0 + dx * i - 4)
                qp.drawLine(size.width() - 10, y0 + dx * i, size.width() - 18, y0 + dx * i + 4)
                if not self.remove_coordinate_system:
                    qp.drawText(size.width() - 18, y0 + dx * i - 6, "x")
                qp.setPen((QPen(Qt.black)))
            else:
                qp.drawLine(10, y0 + dx * i, size.width() - 10, y0 + dx * i)
                qp.drawLine(10, y0 - dx * i, size.width() - 10, y0 - dx * i)

        m = 0
        p = 0
        if not self.remove_coordinate_system and not self.remove_axle:
            for i in range(0, n):
                qp.drawText(x0 + dx * i, y0, str(m))
                qp.drawText(x0 - dx * i, y0, str(m * (-1)))
                m += 1

            for i in range(0, k + 1):
                qp.drawText(x0, y0 + dx * i, str(p * (-1)))
                qp.drawText(x0, y0 - dx * i, str(p))
                p += 1

        qp.setPen(Qt.darkBlue)
        for i in range(len(cykloid_x)):
            if (size.width() - 10 >= cykloid_x[i] >= 10) and (size.height() - 145 >= cykloid_y[i] >= 5):
                qp.drawPoint(cykloid_x[i], cykloid_y[i])

        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = mywindow()

    sys.exit(app.exec())
