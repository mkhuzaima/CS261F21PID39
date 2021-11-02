import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from Gui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.pushButton.clicked.connect(self.printStart)
    '''	self.action_Exit.triggered.connect(self.close)
	self.action_Find_Replace.triggered.connect(self.findAndReplace)
	self.action_About.triggered.connect(self.about)'''


    def printStart(self):
        print("Start button clicked")
        for i in range(1, 101):
        
            time.sleep(.1)
            win.progressBar.setValue(i)
            print(win.progressBar.value())
        
    #     # in pyqt5 it needs to be PyQt5.QtWidgets
    #     msg=QMessageBox() # create an instance of it
    #     msg.setIcon(QMessageBox.Information) # set icon
    #     msg.setText("This is a message box") # set text
    #     msg.setInformativeText("This is additional information") # set information under the main text
    #     msg.setWindowTitle("MessageBox demo") # set title
    #     msg.setDetailedText("The details are as follows:") # a button for more details will add in
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel) # type of buttons associated
    #     msg.buttonClicked.connect(self.myfunc) # connect clicked signal
    #     return_value =msg.exec_() # get the return value
    #     print("value of pressed message box button:", str(return_value)) # print result
    # def myfunc(self):
    #     print('inside my function')



'''    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )'''

'''class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("ui/find_replace.ui", self)'''


import time

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    
    
    sys.exit(app.exec())