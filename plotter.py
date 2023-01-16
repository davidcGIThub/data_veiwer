from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import numpy as np
import os
from random import randint

class Plotter(QtWidgets.QMainWindow):

    def __init__(self,plots_per_row,window_title = "plotter"):
        super(Plotter, self).__init__()
        self.setWindowTitle(window_title)
        self._layout = QtWidgets.QGridLayout()
        self._plots_per_row = plots_per_row
        if self._plots_per_row < 1:
            self._plots_per_row = 1
        self._num_plots = 0
        self._plot_dict = {}
        self._xdata = []
        self._ydata = []
        self._data_lines = []
        widget = QtWidgets.QWidget()
        widget.setLayout(self._layout)
        self.setCentralWidget(widget)
        self._pen = pg.mkPen(color=(255, 0, 0))
        self._update_flag = False
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.animate_plot)
        self.timer.start()

    def add_plot(self, id="", xlabel="x_label", ylabel="y_label"):
        print("add plot data")
        row = self._num_plots//self._plots_per_row
        col = self._num_plots%self._plots_per_row
        plot_widget = pg.PlotWidget()
        plot_widget.setLabel('left', ylabel)
        plot_widget.setLabel('bottom', xlabel)
        self._layout.addWidget(pg.PlotWidget(),row,col)
        if id == "":
            id = str(self._num_plots)
        self._plot_dict[id] = self._num_plots
        self._xdata.append(np.array([]))
        self._ydata.append(np.array([]))
        data_line = self._layout.itemAt(0).widget().plot(np.array([]), np.array([]), pen=self._pen)
        self._data_lines.append(data_line)
        self._num_plots += 1

    def update_plot_data(self, id, xvalue, yvalue):
        print("update plot data")
        index = self._plot_dict[id]
        self._xdata[index] = np.append(self._xdata[index], xvalue)
        self._ydata[index] = np.append(self._ydata[index], yvalue)
        self._update_flag = True

    def animate_plot(self):
        if(self._update_flag):
            # data_line = self._data_lines[0]
            x_data = self._xdata[0]
            y_data = self._ydata[0]
            print("xdata: " , x_data)
            print("ydata: " , y_data)
            self._data_lines[0].setData(x_data, y_data)
            self._update_flag = False




app = QtWidgets.QApplication(sys.argv)
plotter = Plotter(2)
plotter.add_plot("id1", xlabel="time", ylabel="units")
plotter.add_plot("id2", xlabel="time", ylabel="units")
plotter.add_plot("id3", xlabel="time", ylabel="units")
plotter.add_plot("id4", xlabel="time", ylabel="units")
plotter.add_plot("id5", xlabel="time", ylabel="units")
plotter.show()
for i in range(10):
    plotter.update_plot_data("id1", 3, 2)
sys.exit(app.exec())