'''
Created on 7 Jun 2017

@author: Cecylia
'''
import sys

from pyQtSource.ui_Cecylia import *


class Cecylia(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_dlgCecylia()
        self.ui.setupUi(self)
        
        self.listOfCecyliaFeeling = ['so, so', 'not bad', 'actually fine', 'quite well',
                                     'good', 'awsome','happy']
        self.listOfCecyliaTiredness = ['not too tired', "wan't sleep", 'sleepy']
        self.myFeeling = 0
        self.myTiredness = 0
        
        self.ui.btnFeelGood.clicked.connect(self.feeling)
           
    def feeling(self):
        print('inside function feeling in Cecylia',self.listOfCecyliaFeeling[self.myFeeling])
        
        self.ui.lblFeeling.setText(self.listOfCecyliaFeeling[self.myFeeling])
        self.myFeeling = self.myFeeling+1
        print(self.myFeeling)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Cecylia()
    ui.show()
    sys.exit(app.exec_())