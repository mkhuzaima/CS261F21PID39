# from test import Ui_Dialog
from loader2 import Ui_MainWindow
from SelectAlgorithm import Ui_Dialog
import splashScreen
from PyQt5 import QtCore, QtGui, QtWidgets


'''from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow, 
    QPushButton,
    QVBoxLayout,
    QWidget,
)'''

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot





import time
import csv



# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = splashScreen.Ui_MainWindow()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlag(Qt.SplashScreen)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        #self.show()

        #self.progress()
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        ####################################################################################################################################################################################################
        self.counter = 95
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(self.counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = Window()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()
        # INCREASE COUNTER
        self.counter += 1


'''class AlgorithmSelecionDialog(QDialog):
    """Employee dialog."""
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)'''
        
# dialog
class AlgorithmSelecionDialog(QDialog, Ui_Dialog):


    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        #self.ui = Ui_Dialog()
        # Run the .setupUi() method to show the GUI
        self.setupUi(self)
        
        
        self.addEvents()
        
        

    def addEvents(self):
        self.radioButton_3.clicked.connect(self.sortClicked)
        self.radioButton_2.clicked.connect(self.searchClicked)
        self.radioButton.clicked.connect(self.filterClicked)
        
        

    def sortClicked(self):
        alg = [
            'Merge Sort',
            'Insertion Sort',
            'Counting Sort'
        ]
        self.comboBox.clear()
        for a in alg:
            self.comboBox.addItem(a)
        
    def searchClicked(self):
        print('radio button 3 clicked')
        self.comboBox.clear()
        alg = [
            'Linear Search',
            'Binary Search',
            'Ternary Search',
            'Exponential Search',
        ]
        
        for a in alg:
            self.comboBox.addItem(a)
            
    def filterClicked(self):
        alg = [
            'Filter',
        ]
        
        self.comboBox.clear()
        for a in alg:
            self.comboBox.addItem(a)
    
    


# our class
class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        
        super().__init__(parent)
        self.setupUi(self)
        self.addEvents()
        
        
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.continueLoading = True
        self.progressBarValue = 0
        
        
        
    
    def startLoading(self, start):
        self.continueLoading = True
        print('starting the progress bar')
        i = start
        while i <= 100 and self.continueLoading:
            print(self.continueLoading)
            self.progressBarValue = i
            
            self.progressBar.setValue(i)
            time.sleep(.05)
            i+=1
        print('done')
        
    
    
    def startLoading2(self, start = 0):
        worker = Worker(self.startLoading, start)
        self.threadpool.start(worker)
        
    
    def loadData(self):
        
        startingTime = time.time()
        print('loading the data')
        
        with open('data.csv', 'r', encoding='utf-8') as f:
            csvReader = csv.reader(f)
            
            
            row = 0
            for item in csvReader:
                self.tableWidget.setRowCount(row+1)
                i = 0
                for attribute in item:
                    self.tableWidget.setItem(row, i, QTableWidgetItem(attribute))
                    i += 1
                    
                    
                    
                row +=1
                
        endingTime = time.time()        
        print('data loaded successfully')
        print(f'Loading took {endingTime - startingTime} second(s) to complete')
        print(self.tableWidget.rowCount())
        
        
        '''people = [{"name": "Khuzaima", "age": 18}, {"name": "Musab", "age": 11}]
        
        r = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(r+len(people))
        
        row = r
        for p in people:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(p["name"]))
            a = str(p["age"])
            self.tableWidget.setItem(row, 1, QTableWidgetItem(a))
            row +=1'''
    
    
    def loadButtonClicked(self):
        loadDataWorker = Worker(self.loadData)
        self.threadpool.start(loadDataWorker)
    
    def selectDialogButton_clicked(self):
    
        dlg = AlgorithmSelecionDialog()
        
        
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
            
            
            
    def pauseLoading(self):
        self.continueLoading = False
    
    def resumeLoading(self):
        print('i\'ll resume loading ')
        self.startLoading2(self.progressBarValue)
    
    def addEvents(self):
        self.pushButton_2.clicked.connect(self.startLoading2)
        self.pushButton.clicked.connect(self.loadButtonClicked)
        self.pushButton_3.clicked.connect(self.selectDialogButton_clicked)
        self.pushButton_4.clicked.connect(self.pauseLoading)
        self.pushButton_5.clicked.connect(self.resumeLoading)
        
        
        #self.timer = QTimer()
        #self.timer.setInterval(5)
        #self.timer.timeout.connect(self.checkPainter)
        #self.timer.start()
        
        
        
    def checkPainter(self):
        
        #print(painter)
        if (self.painter.isActive()):
            print('painter is active')
        #print(self.painter.isActive())
        
    
class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        
        print("printing args",self.args, self.kwargs)
        self.fn(*self.args, **self.kwargs)


# running GUI instance
if __name__ == "__main__":
    import sys
    
    print('starting the application')

    
    app = QtWidgets.QApplication(sys.argv)
    
    win = SplashScreen()
    #win = Window()
    win.show()
    sys.exit(app.exec_())