import sys
import re
from PySide.QtGui import *
from BasicUI import *


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.saveToTargetButton.setEnabled(False)

        self.clearButton.clicked.connect(self.clear_en)
        self.loadButton.clicked.connect(self.loadData)
        self.saveToTargetButton.clicked.connect(self.save_pressed)

        self.check()


    def check(self):
        self.firstNameLineEdit.textChanged.connect(self.save_en)
        self.lastNameLineEdit.textChanged.connect(self.save_en)
        self.addressLineEdit.textChanged.connect(self.save_en)
        self.cityLineEdit.textChanged.connect(self.save_en)
        self.stateLineEdit.textChanged.connect(self.save_en)
        self.zipLineEdit.textChanged.connect(self.save_en)
        self.emailLineEdit.textChanged.connect(self.save_en)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath, 'r') as inputFile:
            content = inputFile.readlines()
        for line in content:
            expr1 = r".*?<FirstName>(.*?)</FirstName>.*?"
            search1 = re.search(expr1, line)
            if search1:
                First = search1.group(1)

            expr2 = r".*?<LastName>(.*?)</LastName>.*?"
            search2 = re.search(expr2, line)
            if search2:
                Last = search2.group(1)

            expr3 = r".*?<Address>(.*?)</Address>.*?"
            search3 = re.search(expr3, line)
            if search3:
                Address = search3.group(1)

            expr4 = r".*?<City>(.*?)</City>.*?"
            search4 = re.search(expr4, line)
            if search4:
                City = search4.group(1)

            expr5 = r".*?<State>(.*?)</State>.*?"
            search5 = re.search(expr5, line)
            if search5:
                State = search5.group(1)

            expr6 = r".*?<ZIP>(.*?)</ZIP>.*?"
            search6 = re.search(expr6, line)
            if search6:
                Zip = search6.group(1)

            expr7 = r".*?<Email>(.*?)</Email>.*?"
            search7 = re.search(expr7, line)
            if search7:
                Email = search7.group(1)

        self.firstNameLineEdit.setText(First)
        self.lastNameLineEdit.setText(Last)
        self.addressLineEdit.setText(Address)
        self.cityLineEdit.setText(City)
        self.stateLineEdit.setText(State)
        self.zipLineEdit.setText(Zip)
        self.emailLineEdit.setText(Email)
        self.loadButton.setEnabled(False)

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def clear_en(self):
        self.firstNameLineEdit.setText("")
        self.lastNameLineEdit.setText("")
        self.addressLineEdit.setText("")
        self.cityLineEdit.setText("")
        self.stateLineEdit.setText("")
        self.zipLineEdit.setText("")
        self.emailLineEdit.setText("")
        self.loadButton.setEnabled(True)
        self.saveToTargetButton.setEnabled(False)

    def save_en(self):
        self.saveToTargetButton.setEnabled(True)

    def save_pressed(self):
        First = self.firstNameLineEdit.text()
        Last = self.lastNameLineEdit.text()
        Address = self.addressLineEdit.text()
        City = self.cityLineEdit.text()
        State = self.stateLineEdit.text()
        Zip = self.zipLineEdit.text()
        Email = self.emailLineEdit.text()

        err = 0
        err1 = 0
        err2 = 0
        if First == "":
            self.errorInfoLabel.setText("First Name is Empty")
            err = 1
        elif Last == "":
            self.errorInfoLabel.setText("Last Name is Empty")
            err = 1
        elif Address == "":
            self.errorInfoLabel.setText("Address is Empty")
            err = 1
        elif City == "":
            self.errorInfoLabel.setText("City is Empty")
            err = 1
        elif State == "":
            self.errorInfoLabel.setText("State is Empty")
            err = 1
        elif Zip == "":
            self.errorInfoLabel.setText("Zip is Empty")
            err = 1
        elif Email == "":
            self.errorInfoLabel.setText("Email is Empty")
            err = 1
        # Check States
        elif State not in self.states:
            self.errorInfoLabel.setText("State is Invalid")
            err = 1
        # Check Zip Length
        elif (len(Zip) != 5):
                self.errorInfoLabel.setText("Zip is Invalid")
                err = 1

        else:
            self.errorInfoLabel.setText("")
            err = 0


        # Check Zip Digits
        for number in Zip:
            if number in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                continue
                err1 = 0
            else:
                err1 = 1

        # Check Email
        expr = r"\w+@\w+\.\w+"
        if(re.match(expr, Email) == None):
            self.errorInfoLabel.setText('Email is Invalid!')
            err2 = 1
        else:
            err2 = 0

        if err == 0 and err1 == 0 and err2 == 0:
            with open("target.xml", "w") as inputFile:
                inputFile.writelines('<?xml version="1.0" encoding="UTF-8"?>\n<user>\n\t<FirstName>{0}</FirstName>\n\t<LastName>{1}</LastName>\n\t<Address>{2}</Address>\n\t<City>{3}</City>\n\t<State>{4}</State>\n\t<ZIP>{5}</ZIP>\n\t<Email>{6}</Email>\n</user>\n'.format(First, Last, Address, City, State, Zip, Email))


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
