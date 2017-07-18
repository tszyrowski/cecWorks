# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\T\workspace\SCTsearcher\src\pyQtSource\ui_Cecylia.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgCecylia(object):
    def setupUi(self, dlgCecylia):
        dlgCecylia.setObjectName("dlgCecylia")
        dlgCecylia.resize(340, 112)
        self.widget = QtWidgets.QWidget(dlgCecylia)
        self.widget.setGeometry(QtCore.QRect(20, 20, 301, 44))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lblFeeling = QtWidgets.QLabel(self.widget)
        self.lblFeeling.setText("")
        self.lblFeeling.setObjectName("lblFeeling")
        self.gridLayout.addWidget(self.lblFeeling, 0, 1, 1, 1)
        self.btnFeelGood = QtWidgets.QPushButton(self.widget)
        self.btnFeelGood.setObjectName("btnFeelGood")
        self.gridLayout.addWidget(self.btnFeelGood, 1, 0, 1, 2)
        self.widget1 = QtWidgets.QWidget(dlgCecylia)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 146, 19))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdiHappines = QtWidgets.QRadioButton(self.widget1)
        self.rdiHappines.setObjectName("rdiHappines")
        self.horizontalLayout.addWidget(self.rdiHappines)
        self.rdiTiredness = QtWidgets.QRadioButton(self.widget1)
        self.rdiTiredness.setObjectName("rdiTiredness")
        self.horizontalLayout.addWidget(self.rdiTiredness)

        self.retranslateUi(dlgCecylia)
        QtCore.QMetaObject.connectSlotsByName(dlgCecylia)

    def retranslateUi(self, dlgCecylia):
        _translate = QtCore.QCoreApplication.translate
        dlgCecylia.setWindowTitle(_translate("dlgCecylia", "Dialog"))
        self.label.setText(_translate("dlgCecylia", "This is how I feel"))
        self.btnFeelGood.setText(_translate("dlgCecylia", "Feel good"))
        self.rdiHappines.setText(_translate("dlgCecylia", "happiness"))
        self.rdiTiredness.setText(_translate("dlgCecylia", "tiredness"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlgCecylia = QtWidgets.QDialog()
    ui = Ui_dlgCecylia()
    ui.setupUi(dlgCecylia)
    dlgCecylia.show()
    sys.exit(app.exec_())

