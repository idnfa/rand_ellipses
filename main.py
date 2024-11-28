import sys
from random import randint

from ui_file import Ui_circles
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QWidget, QApplication


class MyWidget(QWidget,Ui_circles):
    def __init__(self):
        super().__init__()
        self.btn = None
        self.rad = None
        self.shape = None
        self.setupUi(self)
        self.btn.clicked.connect(self.run)

    def run(self):
        self.shape = 'ellipse'
        self.rad = randint(20, 100)
        self.update()

    def paintEvent(self, event):
        if self.shape == 'ellipse':
            r = self.rad
            qp = QPainter(self)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setBrush(color)
            if self.shape == 'ellipse':
                qp.drawEllipse(QPointF(randint(100, 520), randint(100, 400)), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
