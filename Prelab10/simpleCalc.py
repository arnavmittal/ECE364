# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.x=0
        self.y=0
        self.final=0
        self.operator=""
        self.calc=0
        self.finished=0
        self.decimal=0
        # Number buttons clicked and then add the value of button pressed to txtdisplay
        self.btn0.clicked.connect(self.display0)
        self.btn1.clicked.connect(self.display1)
        self.btn2.clicked.connect(self.display2)
        self.btn3.clicked.connect(self.display3)
        self.btn4.clicked.connect(self.display4)
        self.btn5.clicked.connect(self.display5)
        self.btn6.clicked.connect(self.display6)
        self.btn7.clicked.connect(self.display7)
        self.btn8.clicked.connect(self.display8)
        self.btn9.clicked.connect(self.display9)
        self.btnDot.clicked.connect(self.display_dot)

        # Store current txtdisplay value as x and then clear it and then proceed to store the next value as y
        self.btnPlus.clicked.connect(self.operation_add)
        self.btnMinus.clicked.connect(self.operation_sub)
        self.btnMultiply.clicked.connect(self.operation_mul)
        self.btnDivide.clicked.connect(self.operation_div)
        self.btnEqual.clicked.connect(self.operation_eql)
        self.btnClear.clicked.connect(self.operation_clr)

    # Mapping Clicked to Display in self.txtDisplay
    def display0(self):
        value='0'
        expr = self.txtDisplay.text()
        if self.calc == 1 and self.operator != "=":

            self.txtDisplay.setText(value)
        self.txtDisplay.setText(expr+value)

    def display1(self):
        value=1
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display2(self):
        value=2
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display3(self):
        value=3
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display4(self):
        value=4
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display5(self):
        value=5
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display6(self):
        value=6
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display7(self):
        value=7
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display8(self):
        value=8
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display9(self):
        value=9
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(str(float(expr)*10+value))

    def display_dot(self):
        value='.'
        expr = self.txtDisplay.text()
        self.txtDisplay.setText(expr+value)


    def operation_add(self):
        self.calc=1
        self.operator = '+'
        self.x = self.txtDisplay.text()

    def operation_sub(self):
        self.calc=1
        self.operator = '-'
        self.x = self.txtDisplay.text()

    def operation_mul(self):
        self.calc=1
        self.operator = '*'
        self.x = self.txtDisplay.text()

    def operation_div(self):
        self.calc=1
        self.operator = '/'
        self.x = self.txtDisplay.text()

    def operation_eql(self):
        self.finished=1
        self.operator = '='
        self.x = self.txtDisplay.text()

    def operation_clr(self):
        self.txtDisplay.setText("")

currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()
currentForm.show()
currentApp.exec_()
