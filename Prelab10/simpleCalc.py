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
        self.operator=0
        self.list=[]
        self.calc=0

        self.add_cnt=0
        self.sub_cnt=0
        self.mul_cnt=0
        self.div_cnt=0

        self.final_value=0.00000

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

    def gettext(self):
        current_disp = self.txtDisplay.text()
        if ',' in current_disp:
            new_str = current_disp.replace(",","")
        else:
            new_str = current_disp
        return new_str
    # Mapping Clicked to Display in self.txtDisplay
    def display0(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        self.strokes += 1
        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'0')

    def display1(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        self.strokes += 1
        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'1')

    def display2(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'2')
        self.strokes += 1

    def display3(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'3')
        self.strokes += 1

    def display4(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'4')
        self.strokes += 1

    def display5(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'5')
        self.strokes += 1

    def display6(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'6')
        self.strokes += 1

    def display7(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'7')
        self.strokes += 1

    def display8(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'8')
        self.strokes += 1

    def display9(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        self.txtDisplay.setText(current_disp+'9')
        self.strokes += 1

    def display_dot(self):
        if(self.strokes == 0):
            self.operation_clr()

        if(self.calc == 1):
            self.disp_clr()
            self.calc = 0

        current_disp = self.gettext()
        if '.' not in current_disp:
            self.txtDisplay.setText(current_disp+'.')
            self.strokes += 1


    def operation_add(self):
        self.calc=1
        self.operator+=1
        self.strokes+=1
        self.add_cnt+=1
        current_disp = self.gettext()
        self.list.append(current_disp)
        self.list.append('+')
        #-------------------------------MODIFIED
        #self.disp_clr()
        print("NUM OF OPERATORS")
        print(self.operator)
        print("BEFORE")
        self.debug_1()
        if self.operator >= 2:
            #ADDITION
            if self.list[1] == '+':
                try:
                    self.add_cnt-=1
                    self.final_value = (float(self.list[0]) + float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #MULTIPLICATION
            elif self.list[1] == '*':
                try:
                    self.mul_cnt-=1
                    self.final_value = (float(self.list[0]) * float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #SUBTRACTION
            elif self.list[1] == '-':
                try:
                    self.sub_cnt-=1
                    self.final_value = (float(self.list[0]) - float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #DIVISION
            elif self.list[1] == '/':
                try:
                    self.div_cnt-=1
                    self.final_value = (float(self.list[0]) / float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
        print("AFTER")
        self.debug_1()

    def operation_sub(self):
        self.calc=1
        self.operator+=1
        self.strokes+=1
        self.sub_cnt+=1
        current_disp = self.gettext()
        self.list.append(current_disp)
        self.list.append('-')
        #-------------------------------MODIFIED
        #self.disp_clr()
        print("NUM OF OPERATORS")
        print(self.operator)
        print("BEFORE")
        self.debug_1()
        if self.operator >= 2:
            #ADDITION
            if self.list[1] == '+':
                try:
                    self.operator-=1
                    self.add_cnt-=1
                    self.final_value = (float(self.list[0]) + float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #MULTIPLICATION
            elif self.list[1] == '*':
                try:
                    self.operator-=1
                    self.mul_cnt-=1
                    self.final_value = (float(self.list[0]) * float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #SUBTRACTION
            elif self.list[1] == '-':
                try:
                    self.operator-=1
                    self.sub_cnt-=1
                    self.final_value = (float(self.list[0]) - float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #DIVISION
            elif self.list[1] == '/':
                try:
                    self.operator-=1
                    self.div_cnt-=1
                    self.final_value = (float(self.list[0]) / float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
        print("AFTER")
        self.debug_1()

    def operation_mul(self):
        self.calc=1
        self.operator+=1
        self.strokes+=1
        self.mul_cnt+=1
        current_disp = self.gettext()
        self.list.append(current_disp)
        self.list.append('*')
        #-------------------------------MODIFIED
        #self.disp_clr()
        print("NUM OF OPERATORS")
        print(self.operator)
        print("BEFORE")
        self.debug_1()
        if self.operator >= 2:
            #ADDITION
            if self.list[1] == '+':
                try:
                    self.operator-=1
                    self.add_cnt-=1
                    self.final_value = (float(self.list[0]) + float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #MULTIPLICATION
            elif self.list[1] == '*':
                try:
                    self.operator-=1
                    self.mul_cnt-=1
                    self.final_value = (float(self.list[0]) * float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #SUBTRACTION
            elif self.list[1] == '-':
                try:
                    self.operator-=1
                    self.sub_cnt-=1
                    self.final_value = (float(self.list[0]) - float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #DIVISION
            elif self.list[1] == '/':
                try:
                    self.operator-=1
                    self.div_cnt-=1
                    self.final_value = (float(self.list[0]) / float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
        print("AFTER")
        self.debug_1()

    def operation_div(self):
        self.calc=1
        self.operator+=1
        self.strokes+=1
        self.div_cnt+=1
        current_disp = self.gettext()
        self.list.append(current_disp)
        self.list.append('/')
        #-------------------------------MODIFIED
        #self.disp_clr()
        print("NUM OF OPERATORS")
        print(self.operator)
        print("BEFORE")
        self.debug_1()
        if self.operator >= 2:
            #ADDITION
            if self.list[1] == '+':
                try:
                    self.operator-=1
                    self.add_cnt-=1
                    self.final_value = (float(self.list[0]) + float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #MULTIPLICATION
            elif self.list[1] == '*':
                try:
                    self.operator-=1
                    self.mul_cnt-=1
                    self.final_value = (float(self.list[0]) * float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #SUBTRACTION
            elif self.list[1] == '-':
                try:
                    self.operator-=1
                    self.sub_cnt-=1
                    self.final_value = (float(self.list[0]) - float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #DIVISION
            elif self.list[1] == '/':
                try:
                    self.operator-=1
                    self.div_cnt-=1
                    print(self.list)
                    self.final_value = (float(self.list[0]) / float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
        print("AFTER")
        self.debug_1()

    def debug_1(self):
        print('List = ')
        print(self.list)
        print('Add = '+str(self.add_cnt))
        print('Sub = '+str(self.sub_cnt))
        print('Mul = '+str(self.mul_cnt))
        print('Div = '+str(self.div_cnt))


    def operation_clr(self):
        self.txtDisplay.clear()
        self.txtDisplay.setText('')
        self.strokes=0
        self.list=[]
        self.add_cnt=0
        self.sub_cnt=0
        self.mul_cnt=0
        self.div_cnt=0
        self.final_value=0.000
        self.operator = 0

    def disp_clr(self):
        self.txtDisplay.clear()
        self.txtDisplay.setText('')

    def operation_eql(self):
        current_disp = self.gettext()
        self.list.append(current_disp)
        print("NUM OF OPERATORS")
        print(self.operator)
        if self.operator >= 1:
            #ADDITION
            if self.list[1] == '+':
                try:
                    self.operator-=1
                    self.add_cnt-=1
                    self.final_value = (float(self.list[0]) + float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #MULTIPLICATION
            elif self.list[1] == '*':
                try:
                    self.operator-=1
                    self.mul_cnt-=1
                    self.final_value = (float(self.list[0]) * float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #SUBTRACTION
            elif self.list[1] == '-':
                try:
                    self.operator-=1
                    self.sub_cnt-=1
                    self.final_value = (float(self.list[0]) - float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
            #DIVISION
            elif self.list[1] == '/':
                try:
                    self.operator-=1
                    self.div_cnt-=1
                    print(self.list)
                    self.final_value = (float(self.list[0]) / float(self.list[2]))
                    del self.list[0]
                    del self.list[0]
                    del self.list[0]
                    self.list.insert(0, str(self.final_value))
                except ValueError:
                    raise ValueError("The typed expression is invalid")
        print("FINAL")
        self.debug_1()
        del self.list[0]
        self.display()

    def display(self):

        text = str(self.cboDecimal.currentText())
        activated = self.chkSeparator.isChecked()
        activate = QtCore.Qt.Checked
        print('ACTIVATED STATUS')
        print(activate)
        if activated == True:
            comma= ','
        else:
            comma=''
        final_string='{:{sprtr}.{dec}f}'.format(self.final_value, sprtr= comma , dec=int(text))
        self.txtDisplay.setText(final_string)


currentApp = QApplication(sys.argv)
currentForm = CalculatorConsumer()
currentForm.show()
currentApp.exec_()