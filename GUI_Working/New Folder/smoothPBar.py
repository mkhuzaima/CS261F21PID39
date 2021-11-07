from PyQt5.QtWidgets import QApplication, QProgressBar, QWidget, QPushButton
from PyQt5.QtCore import QTimer
import time

app = QApplication([])

centralwidget =  QWidget()

pbar = QProgressBar(centralwidget)
pbar.setMinimum(0)
pbar.setMaximum(100)

pbar.show()
p = 0


def drawBar():
    global pbar
    global p
    p = p + 1
    pbar.setValue(p)
    pbar.update()

t = QTimer()
t.timeout.connect(drawBar)
t.start(100)

'''for i in range(1,101):
    time.sleep(0.1)
    pbar.setValue(i)'''

app.exec_()