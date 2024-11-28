from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_circles(object):
    def setupUi(self, circles):
        circles.setObjectName("circles")
        circles.resize(635, 478)
        self.btn = QtWidgets.QPushButton(parent=circles)
        self.btn.setGeometry(QtCore.QRect(280, 420, 93, 28))
        self.btn.setObjectName("btn")

        self.retranslateUi(circles)
        QtCore.QMetaObject.connectSlotsByName(circles)

    def retranslateUi(self, circles):
        _translate = QtCore.QCoreApplication.translate
        circles.setWindowTitle(_translate("circles", "Form"))
        self.btn.setText(_translate("circles", "кнопка"))
