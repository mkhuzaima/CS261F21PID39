# from test import Ui_Dialog
from loader2 import Ui_MainWindow
from SelectAlgorithm import Ui_Dialog
#import splashScreen
from ui_splash_screen import Ui_SplashScreen
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

from tqdm import tqdm
from random import randint




class Freelancer():
    def __init__(self, row):
        '''(self.name, self.tagline, self.country, 
            self.rating, self.earningLabel, self.rev,
                self.rate, self.description, self.skills, self.imgSrc) = row'''
                
        self.data = row
                
        '''self.name = name
        self.tagline = tagline
        self.country = country
        self.rating = rating
        self.earningLabel = earningLabel
        self.rev = rev
        self.rate = rate
        self.description = description
        self.skills = skills
        self.imgSrc = imgSrc'''

    
    
    '''def compareName(self, other):
        return self.name < other.name
        
    def compareTagline(self, other):
        return self.tagline < other.tagline
        
    def compareCountry(self, other):
        return self.country < other.country
    
    def compareRating(self, other):
        return self.rating < other.rating
        
    def compareEarningLabel(self, other):
        return self.earningLabel < other.earningLabel
        
    def compareRev(self, other):
        return self.rev < other.rev

    def compareRate(self, other):
        return self.rate < other.rate
    
    def compareDescription(self, other):
        return self.description < other.description
        
    def compareSkills(self, other):
        return self.skills < other.skills
    
    def compareImgSrc(self, other):
        return self.imgSrc< other.imgSrc'''
    
    
    
    ########################################
    #
    #           Operator Overloading
    #
    ########################################
    
    
    def __lt__(self, other):
        return self.data[Freelancer.comparingColumn] < other.data[Freelancer.comparingColumn]
        
    def __gt__(self, other):
        return self.data[Freelancer.comparingColumn] > other.data[Freelancer.comparingColumn]
        
    def __eq__(self, other):
        return self.data[Freelancer.comparingColumn] == other.data[Freelancer.comparingColumn]
        
    def __le__(self, other):
        return self.data[Freelancer.comparingColumn] <= other.data[Freelancer.comparingColumn]    
    
    def __ge__(self, other):
        return self.data[Freelancer.comparingColumn] >= other.data[Freelancer.comparingColumn]
        
    def __ne__(self, other):
        return self.data[Freelancer.comparingColumn] != other.data[Freelancer.comparingColumn]
    
    
        
    
    '''...'''
    
    
    
    
# SPLASH SCREEN
class SplashScreen(QMainWindow):





    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        self.progressBarMaximum = 55007
        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        '''## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)'''


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##
        
        
        
        self.counter = 0

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)
        
        self.main = Window()
        
        
        #QtCore.QTimer.singleShot(1000, self.readFile)
        worker = Worker(self.readFile)
        self.main.threadpool.start(worker)
        
        
        
        
    def readFile(self):
        print('reading the file')
        
        self.main.flist = []
        
        with open('data.csv', 'r', encoding='utf-8') as f:
            csvReader = csv.reader(f)
            
            #v = 0
            #row = 0
            for item in csvReader:
                #self.progressBarValue(v)
                #self.tableWidget.setRowCount(row+1)
                #i = 0
                self.main.flist.append(Freelancer(item))
                #for attribute in item:
                    #self.tableWidget.setItem(row, i, QTableWidgetItem(attribute))
                    #i += 1
                    
                    
                    
                #row += 1
                self.counter += 1
                #v += 1
                #print(v)
            #self.progress(v)
                

        self.main.updateTable(self.main.flist)
        
        

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        #global counter
        #global jumper
        value = self.counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(int(self.counter/self.progressBarMaximum*100)))

        #if(value > jumper):
        
        # APPLY NEW PERCENTAGE TEXT
        self.ui.labelPercentage.setText(newHtml)
        #jumper += 10
            
        #endif


        
        # CLOSE SPLASH SCREE AND OPEN APP
        if value > self.progressBarMaximum:
        
            
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            #self.main = Window()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()
            
        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than progressBarMaximum
        if value >= self.progressBarMaximum: value = self.progressBarMaximum
        self.progressBarValue(value)



        # INCREASE COUNTER
        #self.counter += 0.5

    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (self.progressBarMaximum - value) / self.progressBarMaximum

        #print(progress)


        # GET NEW VALUES
        if progress <= 0:
            stop_1 = '0'
        else:
            stop_1 = str(progress - 0.001)
        
        stop_2 = str(progress)


#        print(stop_1, stop_2)
        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


    """def __init__(self):
        QMainWindow.__init__(self)
        self.ui = splashScreen.Ui_MainWindow()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        
        
        #self.setWindowFlags(Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint);
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlag(Qt.SplashScreen)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setFixedSize(self.size())



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
        self.counter = 0
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)



        '''million = 1e6
        self.progressBar.setMaximum(million)
        i = 0
        for line in listOfitems:
            # add line to table
            self.progressBar.setValue(i)
            i += 1
            
        # hide this window and show new screen'''



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
        self.counter += 1"""


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
        self.radioButton_3.click()
        
        

    def addEvents(self):
        self.radioButton_3.clicked.connect(self.sortClicked)
        self.radioButton_2.clicked.connect(self.searchClicked)
        self.radioButton.clicked.connect(self.filterClicked)
        
        

    def sortClicked(self):
        print('radio button 3 clicked')
        print(self.radioButton_3.isChecked())
        alg = [
            'QuickSort',
            'Insertion Sort',
            'Merge Sort',
            'Bubble Sort',
            'Hybrid Sort | Tim Sort',
            'Radix Sort',
        ]
        self.comboBox.clear()
        for a in alg:
            self.comboBox.addItem(a)
        
    def searchClicked(self):
        print('radio button 2 clicked')
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
        print('radio button clicked')
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
        
        
        
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        self.continueLoading = True
        self.progressBarValue = 0
        
        
        self.flist = []
        self.displayedFreelancers = []
        
        self.addEvents()
        
        
        ##no need 
        ###############self.sortingRowIndex = -1
        
        
        # set function
        # pass the function to the sorting method
        self.comparingFunction = None
        
        
        # the list contains the algorithm mehtod of sorting the lsit 
        #  correspoding to the combobox index
        '''
            'QuickSort',
            'Insertion Sort',
            'Merge Sort',
            'Counting Sort'
            '''
        self.sortingFunctionList = [
            self.quickSort,
            self.insertionSortBinary,
            self.mergeSort,
            self.bubbleSort,
            self.hybridSort,
            self.radixSort,
        ]
        
        
        #selectAlgorithmDialog
        self.instanceOfAlgorithmSelecionDialog = None
        
        
        # default comparing Column
        Freelancer.comparingColumn = 0
        
        
        
        '''header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        for i in range(1,10):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)'''
        


    
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
        
    
    def updateTable(self, lst):
    
        self.displayedFreelancers = lst
        
        
        self.tableWidget.setRowCount(0)
    
        startingTime = time.time()
        #print('loading the data')
        
        
        row = 0
        for f in lst:
            
            self.tableWidget.setRowCount(row+1)
            
            for i in range(10):
                self.tableWidget.setItem(row, i, QTableWidgetItem(f.data[i]))
            
            '''self.tableWidget.setItem(row, 0, QTableWidgetItem(f.name))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(f.tagline))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(f.country))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(f.rating))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(f.earningLabel))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(f.rev))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(f.rate))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(f.description))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(f.skills))
            self.tableWidget.setItem(row, 9, QTableWidgetItem(f.imgSrc))'''
            
            
            row += 1
        
        endingTime = time.time()        
        #print('table updated successfully')
        print(f'Loading took {endingTime - startingTime} second(s) to complete')
        #print('loaded the data successfully')
        #print(self.tableWidget.rowCount())
        #print(f"displayed freelancers : {len(self.displayedFreelancers)}")
        #lst = None
        #print(f"displayed freelancers : {len(self.displayedFreelancers)}")
    
    def loadData(self):
        
        self.flist = []
        
        with open('100data.csv', 'r', encoding='utf-8') as f:
            csvReader = csv.reader(f)
            
            
            #row = 0
            for item in csvReader:
                #self.tableWidget.setRowCount(row+1)
                #i = 0
                self.flist.append(Freelancer(item))
                #for attribute in item:
                    #self.tableWidget.setItem(row, i, QTableWidgetItem(attribute))
                    #i += 1
                    
                    
                    
                #row += 1
                

        self.updateTable(self.flist)
        
        
        
        
        
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
    
    
        if self.instanceOfAlgorithmSelecionDialog is None:
            
    
            self.instanceOfAlgorithmSelecionDialog = AlgorithmSelecionDialog()
        
        
        if self.instanceOfAlgorithmSelecionDialog.exec():
            print("Success!")
            
            
            dlg = self.instanceOfAlgorithmSelecionDialog
            
            print(dlg.radioButton_3.isChecked())
            print(dlg.radioButton_3.text())
            if dlg.radioButton_3.isChecked():
                print('sorting selected')
                index = dlg.comboBox.currentIndex()
                print(index)
                print(dlg.comboBox.itemText(index))
                self.comparingFunction = self.sortingFunctionList[index]
                print(self.comparingFunction)
            
            
            
            
#            self.comparingFunction = dlg.comboBox.currentIndex()
#            print(dlg.comboBox.currentIndex())
        else:
            print("Cancel!")
            
            
            
    def pauseLoading(self):
        #self.continueLoading = False
        self.t.stop()
        self.timer.stop()
    
    def resumeLoading(self):
        print('i\'ll resume loading ')
        
        self.t.start()
        self.timer.start()
        #self.startLoading2(self.progressBarValue)
    
    
    def incrementProgressBar(self):
        
        max = self.progressBar.maximum()
        
        #currentValue = self.progressBar.value()
        
        #if currentValue >= self.progressBar.maximum():
        
        print(max, self.progressBarValue)
        
        if self.progressBarValue >= max:
            self.progressBarValue = max
            self.progressBar.setValue(self.progressBarValue)
            
            
            print('current value is greater than maximum value')
            self.progressBarValue = 0
            self.t.stop()
            self.timer.stop()
        else:
        
            self.progressBar.setValue(self.progressBarValue)
        
            #self.progressBar.setValue(self.progressBar.value()+1)
            print('incremented', self.progressBar.value() + 1)
    
    
    def progressBarLoading(self):
        self.progressBarValue = 0
        print('inside the progressBar')
        self.t.start()
        
        
        self.timer.start()
        
        
    def searchFreelancers(self):
        print('searching...')
        
        key = self.lineEdit.text()
        
        print(key)
        
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        print(rows, columns)
        r = 0
        
        searched = []
        for f in self.flist:
        
        
            '''if (key in f.name or key in f.tagline or key in f.country 
                or key in f.rating or key in f.earningLabel or key in f.rev
                    or key in f.rate or key in f.description or key in f.skills or key in f.imgSrc):'''
            if any (key in str(attr) for attr in f.data):
                
                searched.append(f)
        self.updateTable(searched)
        
        del searched
        '''#for r in range(1):
        #rcount = 10
        for _ in tqdm(range(rows)):
        #while r < rows:
            for c in range(columns):
                #found = False
                #if r < rows:
                    cellText = self.tableWidget.item(r, c).text()
                    #print(cellText)
                    if key in cellText:
                        #found = True
                        r += 1
                        break
                #else:
                #    r = 10000000
                        
            self.tableWidget.removeRow(r)
            rows -= 1'''
            
            
               
        print('searching done')
        print()
                

    ########################################
    #
    #           Quick Sort
    #
    ########################################
    
    
    def partition(self, arr, low, high):
    
        i = low -1
        pivot = arr[high]
        
        #rIndex = self.sortingRowIndex
        for j in range(low, high+1):
            #if arr[j].compareName(pivot):
            
            #if arr[j].data[rIndex] < pivot.data[rIndex]:
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
            
        return i+1
        
        

    def quickSort(self, arr, start, end):
        if start < end:
            
            index = randint(start, end-1)
            
            arr[index], arr[end-1] = arr[end-1], arr[index]
            
            p = self.partition(arr,start, end-1)
            self.quickSort(arr, start, p)
            self.quickSort(arr, p+1, end)

    ########################################
    #
    #           Insertion Sort
    #
    ########################################
    

    def binarySearchRightMost(self, arr, start, end, key):

        if start >= end:
            # True is treated as 1 and False is treated as 0.
            # So, we can add it to integers
            return end + (arr[start] <= key)

        #         if arr[start]< key:
        #             return end+1
        #         return end
        if start > end:
            print('\n\n\n\n----------------------------------------')
            print('start is greater than end in binary search \n')
            return start
        middle = (start + end) // 2

        if key < arr[middle]:
            return self.binarySearchRightMost(arr, start, middle - 1, key)
        else:   # if present on the right side, find the right most
            return self.binarySearchRightMost(arr, middle + 1, end, key)


    def __helpingInsertionSort(self, arr, start, end):
        #n = len(arr)
        self.progressBar.setMaximum(len(self.flist))
        
        self.progressBarValue = 0
        print(self.progressBar.maximum())
        
        for i in range(start, end):
            key = arr[i]

            index = self.binarySearchRightMost(arr, 0, i - 1, key)
            # to include index, (index-1) is used
            for j in range(i - 1, index-1, -1):
                arr[j+1] = arr[j]
            arr[index] = key
            
            self.progressBarValue += 1
            


    def insertionSortBinary(self, arr, start, end):
        self.t.start()
        worker = Worker(self.__helpingInsertionSort, arr, start, end)
        self.threadpool.start(worker)
    
    ########################################
    #
    #           Merge Sort
    #
    ########################################
    
    def merge(self, arr, start, middle, end):
        i = j = 0
        k = start
        left = arr[start:middle]
        right = arr[middle:end]
        
        leftSize = len(left)
        rightSize = len(right)
        
        
        while i < leftSize and j < rightSize:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+= 1
            k += 1
            
        while i < leftSize:
            arr[k] = left[i]
            k+=1
            i+=1
        while j < rightSize:
            arr[k] = right[j]
            k+=1
            j+=1
        
        
    def mergeSort(self, arr, start, end):
        if end == start +1:
            #return arr[start]
            return
        
        middle = (start + end) // 2
        self.mergeSort(arr, start, middle)
        self.mergeSort(arr, middle, end)
        self.merge(arr, start, middle, end)
    
    
    ########################################
    #
    #           Bubble Sort
    #
    ########################################
    
    def bubbleSort(self, array_element, start, end):
        #num = len(array_element)
        for index in range (start, end-1):
            for k in range (end-1, index, -1):
                # if second element is smaller (descending order), then swap
                if (array_element[k] < array_element[k-1]):
                    array_element[k], array_element[k-1] = array_element[k-1], array_element[k]
        #print(array_element[index].data[Freelancer.comparingColumn])


    
    ########################################
    #
    #           Radix Sort
    #
    ########################################

    def radixSort(self, arr, start, end):
        maxStrLen = 0
        for i in range(start, end):
            a = len(arr[i].data[Freelancer.comparingColumn])
            if a > maxStrLen:
                print(arr[i].data[Freelancer.comparingColumn])
                maxStrLen = a
                
                
        #print(f'maximum length of string is : {maxStrLen}')
        
        for i in tqdm(range(maxStrLen-1, -1, -1)):
        #i = maxStrLen -1
        #while i >= 0:
            self.RISort(arr, start, end, i)
            
            '''print(len(arr))
            for a in arr:
                print(a.data[0])
            print('-'*30)'''
            
            
        #    i -= 1
                
                
                

    def RISort(self, arr, start, end, charPosition):
        #print(charPosition)
        for i in range(start+1, end):
            
            key = arr[i]
            keyLetter = key.data[Freelancer.comparingColumn]
            keyLetter = keyLetter[charPosition] if len(keyLetter) > charPosition else '\0'
            

            #index = self.binarySearchRightMost(arr, 0, i - 1, key)
            
            
            # to include index, (index-1) is used
            j = i-1
            
            while j >= 0:
                a = arr[j].data[Freelancer.comparingColumn]
                #keyLetter < arr[j].data[Freelancer.comparingColumn][charPosition]
                
                if len(a) <= charPosition or keyLetter >= a[charPosition]:
                    break
                    
                '''print()
                for a in arr:
                    print(a.data[0])
                print()'''
            
                arr[j+1] = arr[j]
                
                j -= 1
            arr[j+1] = key
            
            #for j in range(i - 1, index-1, -1):
            #    arr[j+1] = arr[j]
            #arr[index] = key

    
    
    ########################################
    #
    #           Hybrid Sort
    #
    ########################################
    
    def hybridSort(self, arr, start, end):
        
        if end - start <= 100:
        
            #insetion sort
            for i in range(start, end):
                key = arr[i]

                index = self.binarySearchRightMost(arr, 0, i - 1, key)
                # to include index, (index-1) is used
                for j in range(i - 1, index-1, -1):
                    arr[j+1] = arr[j]
                arr[index] = key
                
            #return arr[start]
            print('100 done')
            return
        
        middle = (start + end) // 2
        self.hybridSort(arr, start, middle)
        self.hybridSort(arr, middle, end)
        self.merge(arr, start, middle, end)
    
    
    
    def onHeaderClicked(self, logicalIndex):
        print('old logical index: ', logicalIndex)
        
        print(self.tableWidget.horizontalHeaderItem(logicalIndex).text())
        
        #self.sortingRowIndex = logicalIndex
        Freelancer.comparingColumn = logicalIndex
        #print('new logical index: ', logicalIndex)
        
        print(self.comparingFunction)
        if self.comparingFunction is not None:
            start = time.time()
        
            #self.quickSort(self.flist, 0, len(self.flist)-1)
            self.comparingFunction(self.displayedFreelancers, 0, len(self.displayedFreelancers))
            
            end = time.time()
            
            print(f'time taken to sort is {round(end - start, 4)} s')
            
            self.updateTable(self.displayedFreelancers)
            
            #self.quickSort(self.flist, 0, len(self.flist) -1)
            
        
        
        #self.sortByName()
        
        
        
        
        print('OnHeaderClick Finished')
        

    def sortByName(self):
        start = time.time()
        self.quickSort(self.flist, 0, len(self.flist) -1)
        end = time.time()
        print(f'time taken to sort is {end - start} s')
        self.updateTable(self.flist)
        
    
    def addEvents(self):
    
    
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.onHeaderClicked)
        #self.pushButton_2.clicked.connect(self.sortByName)
        
    
    
        #self.pushButton_2.clicked.connect(self.startLoading2)
        
        
        self.pushButton_2.clicked.connect(self.progressBarLoading)
        
        self.pushButton.clicked.connect(self.loadButtonClicked)
        self.pushButton_3.clicked.connect(self.selectDialogButton_clicked)
        self.pushButton_4.clicked.connect(self.pauseLoading)
        self.pushButton_5.clicked.connect(self.resumeLoading)
        self.lineEdit.editingFinished.connect(self.searchFreelancers)
        
        
        self.progressBar.setMaximum(300)
        
        
        #worker = Worker()
        
        
        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.checkPainter)
        #self.timer.start()
        
        
        self.t = QTimer()
        self.t.timeout.connect(self.incrementProgressBar)
        self.t.setInterval(100)
        
        
        
    def checkPainter(self):
        
        self.progressBarValue+=1
        #print(painter)
        #if (self.painter.isActive()):
        #    print('painter is active')
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
        
        #print("printing args",self.args, self.kwargs)
        self.fn(*self.args, **self.kwargs)


# running GUI instance
if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2000)
    
    print('starting the application')

    
    app = QtWidgets.QApplication(sys.argv)
    
    win = SplashScreen()
    #win = Window()
    win.show()
    sys.exit(app.exec_())
    