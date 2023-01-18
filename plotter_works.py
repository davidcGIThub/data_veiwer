from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys  # We need sys so that we can pass argv to QApplication
import numpy as np
import os
from random import randint
import time

class Plotter():
    def __init__(self):
        self._app = pg.QtWidgets.QApplication([])
        self._window = pg.QtWidgets.QMainWindow()
        self._layout = pg.QtWidgets.QGridLayout()
        self._graph_widget = pg.PlotWidget()
        self._layout.addWidget(self._graph_widget,0,0)
        self._widget = pg.QtWidgets.QWidget()
        self._widget.setLayout(self._layout)
        self._window.setCentralWidget(self._widget)
        pen = pg.mkPen(color=(0, 255, 0))
        self.x1 = list(range(100))  # 100 time points
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        self._data_line = self._graph_widget.plot(self.x1, self.y1, pen=pen)
        self._window.show()

  

    def update_plot_data(self, time_sleep = .1):
        print("update data")
        self.x1 = self.x1[1:] # Remove the first y element.
        self.x1.append(self.x1[-1] + 1) # Add a new value 1 higher than the last.
        self.y1 = self.y1[1:] # Remove the first
        self.y1.append( randint(0,100)) # Add a new random value.
        self._data_line.setData(self.x1, self.y1) # Update the data.
        self._app.processEvents()
        time.sleep(time_sleep)
        self._window.show()
        print("end of update data")


p = Plotter()
for i in range(10):
    p.update_plot_data()
