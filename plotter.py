from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys  # We need sys so that we can pass argv to QApplication
import numpy as np
import os
import random
import time

class Plotter():
    def __init__(self, plots_per_row):
        self._app = pg.QtWidgets.QApplication([])
        self._window = pg.QtWidgets.QMainWindow()
        self._layout = pg.QtWidgets.QGridLayout()
        self._plots_per_row = plots_per_row
        if self._plots_per_row < 1:
            self._plots_per_row = 1
        self._num_plots = 0
        self._plot_dict = {}
        self._xdata_list = []
        self._ydata_list = []
        self._data_lines_list = []
        self._pen_list = []
        widget = QtWidgets.QWidget()
        widget.setLayout(self._layout)
        self._window.setCentralWidget(widget)
        self._window.show()
        # self._pen = pg.mkPen(color=(255, 0, 0))
        
    def add_plot(self, plot_id="", xlabel="x_label", ylabel="y_label", legend = True, bacground_color=(255,0,0)): #fix backgournd color stuff
        row = self._num_plots//self._plots_per_row
        col = self._num_plots%self._plots_per_row
        plot_widget = pg.PlotWidget()
        plot_widget.setLabel('left', ylabel)
        plot_widget.setLabel('bottom', xlabel)
        self._layout.addWidget(pg.PlotWidget(),row,col)
        if plot_id == "":
            plot_id = str(self._num_plots)
        self._plot_dict[plot_id] = self._num_plots
        self._xdata_list.append(np.array([]))
        self._ydata_list.append(np.array([]))
        pen = pg.mkPen(color=data_color)
        if legend == True:
            self._layout.itemAt(self._num_plots).widget().addLegend()
        # data_line = self._layout.itemAt(self._num_plots).widget().plot(np.array([]), np.array([]),
        #     name=data_label,symbol='+', pen=pen)
        self._data_lines_list.append([data_line]) ### add data line in data line function, not here, that way can ask line thicnkess too
        self._num_plots += 1

    def add_data_line(self, plot_id, data_label, data_color, data_thickness): #add func to change line thickenss
        plot_index = self._plot_dict[plot_id]
        pen = pg.mkPen(color=line_color)
        data_line = self._layout.itemAt(plot_index).widget().plot(np.array([]), np.array([]),
            name=line_label, pen=pen)
        self._data_lines_list[plot_index].append(data_line)

    def update_plot_data(self, plot_id, xvalue, yvalue, line_number = 0):
        index = self._plot_dict[plot_id]
        self._xdata_list[index] = np.append(self._xdata_list[index], xvalue)
        self._ydata_list[index] = np.append(self._ydata_list[index], yvalue)
        print("printed:" , self._data_lines_list[index][line_number])
        self._data_lines_list[index][line_number].setData(self._xdata_list[index], self._ydata_list[index])

    def update_window(self, sleep_time = 0):
        self._app.processEvents()
        time.sleep(sleep_time)

p = Plotter(3)
p.add_plot(plot_id="foo", xlabel="xXx", ylabel="yYy", data_label="lab", data_color=(0,255,0))
p.add_plot(plot_id="fi", xlabel="xs", ylabel="ys", data_label="labelz", data_color=(0,0,255))
for i in range(10):
    p.update_plot_data("foo",i,random.randint(0,20))
    p.update_plot_data("fi",i,random.randint(0,20))
    p.update_window(2)
