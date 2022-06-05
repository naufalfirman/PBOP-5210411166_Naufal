# import sys
# # from tkinter import Widget
# from PyQt5.QtWidgets import *

# class mainform(QWidget):
#     def __init__(self) :
#         super().__init__()
#         self.setupU1()
#     def setupU1(self):
#         self.resize(200,100)
#         self.setWindowTitle('Demo gridLayout')
#         self.label1=QLabel('username')
#         self.usernameEdit=QLineEdit()
#         self.label2=QLabel('username')
#         self.passwordEdit=QLineEdit()
#         self.loginButton=QPushButton('Login')
#         self.exitButton=QPushButton('Exit')

#         grid=QGridLayout()
#         grid.addWidget(self.label1,0,0)
#         grid.addWidget(self.usernameEdit,0,1,1,2)
#         grid.addWidget(self.label2,1,0)
#         grid.addWidget(self.passwordEdit,1,1,1,2)
#         grid.addWidget(self.loginButton,2,1)
#         grid.addWidget(self.exitButton,2,2)

#         self.setLayout(grid)


# if __name__=='__main__':
#     a=QApplication(sys.argv)
#     form=mainform()
#     form.show()
#     a.exec_()
        

import sys

from PyQt5.QtWidgets import *


class Mf(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.label1=QLabel('Bilangan 1')
        self.numedit1=QLineEdit()
        self.label2=QLabel('Bilangan 2')
        self.numedit2=QLineEdit()
        self.label3=QLabel('Hasil Perhitungan')
        self.resuledit=QLineEdit()
        self.addbutton=QPushButton('Tambah')
        self.subtarcbutton=QPushButton('Kurang')
        self.mulbutton=QPushButton('Kali')
        self.bagbutton=QPushButton('Bagi')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.numedit1)
        vbox.addWidget(self.numedit2)
        vbox.addWidget(self.resuledit)
        vbox.addStretch()


        hbox = QHBoxLayout()
        hbox.addWidget(self.addbutton)
        hbox.addWidget(self.subtarcbutton)
        hbox.addWidget(self.mulbutton)
        hbox.addWidget(self.bagbutton)

        mainly = QVBoxLayout()
        mainly.addLayout(vbox)
        mainly.addLayout(hbox)

        self.setLayout(mainly)
        self.addbutton.clicked.connect(lambda:self.calculate('+'))
        self.subtarcbutton.clicked.connect(lambda:self.calculate('-'))
        self.mulbutton.clicked.connect(lambda:self.calculate('*'))
        self.bagbutton.clicked.connect(lambda:self.calculate('/'))

    def calculate(self,operator):

        num1 = float(self.numedit1.text())
        num2 = float(self.numedit2.text())
        
        if operator=="+":
            result=num1+num2
            operation="Penjumlahan"
        elif operator=="-":
            result=num1-num2
            operation = 'pengurangan'
        elif operator=="*":
            result=num1-num2
            operation = 'Perkalian'
        elif operator=="/":
            result=num1-num2
            operation = 'pembagian'

        self.label3.setText("Hasil %s"%operation)
        self.resuledit.setText(str(result))


if __name__=='__main__':
    a=QApplication(sys.argv)
    form=Mf()
    form.show()
    a.exec_()
