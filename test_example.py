from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My App")
        layout = QtWidgets.QGridLayout()
        self.graph1Widget = pg.PlotWidget()
        self.graph1Widget.setBackground('w')
        layout.addWidget(self.graph1Widget,0,0)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.x1 = list(range(100))  # 100 time points
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        pen = pg.mkPen(color=(255, 0, 0))
        self.data1_line =  self.graph1Widget.plot(self.x1, self.y1, pen=pen)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x1 = self.x1[1:]  # Remove the first y element.
        self.x1.append(self.x1[-1] + 1)  # Add a new value 1 higher than the last.
        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append( randint(0,100))  # Add a new random value.
        print("self.data1_line: " , self.data1_line)
        self.data1_line.setData(self.x1, self.y1)  # Update the data.


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())