# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from calculator import *

class CalculatorConsumer(QMainWindow, Ui_Calculator):

    def __init__(self, parent=None):
        super(CalculatorConsumer, self).__init__(parent)
        self.setupUi(self)

        self.strokes=0
        #self.current_disp = self.txtDisplay.text()
        self.list=[]

        self.final_value=0
        self.operator=""
        self.calc=0
        self.eql=0
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
        if(self.strokes == 0):
            self.operation_clr()
        self.strokes += 1
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'0')

    def display1(self):
        if(self.strokes == 0):
            self.operation_clr()
        self.strokes += 1
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'1')

    def display2(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'2')
        self.strokes += 1

    def display3(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'3')
        self.strokes += 1

    def display4(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'4')
        self.strokes += 1

    def display5(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'5')
        self.strokes += 1

    def display6(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'6')
        self.strokes += 1

    def display7(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'7')
        self.strokes += 1

    def display8(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'8')
        self.strokes += 1

    def display9(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        self.txtDisplay.setText(current_disp+'9')
        self.strokes += 1

    def display_dot(self):
        if(self.strokes == 0):
            self.operation_clr()
        current_disp = self.txtDisplay.text()
        if '.' not in current_disp:
            self.txtDisplay.setText(current_disp+'.')
            self.strokes += 1


    def operation_add(self):
        current_disp = self.txtDisplay.text()
        self.list.append(current_disp)
        self.list.append('+')
        self.operation_clr()

    def operation_sub(self):
        current_disp = self.txtDisplay.text()
        self.list.append(current_disp)
        self.list.append('-')
        self.operation_clr()

    def operation_mul(self):
        current_disp = self.txtDisplay.text()
        self.list.append(current_disp)
        self.list.append('*')
        self.operation_clr()

    def operation_div(self):
        current_disp = self.txtDisplay.text()
        self.list.append(current_disp)
        self.list.append('/')
        self.operation_clr()

    def operation_eql(self):
        pass

    def operation_clr(self):
        self.txtDisplay.clear()
        self.txtDisplay.setText('')

currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()
currentForm.show()
currentApp.exec_()
