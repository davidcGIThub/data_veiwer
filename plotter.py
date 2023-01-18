from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys  # We need sys so that we can pass argv to QApplication
import numpy as np
import random
import time

class Plotter():
    def __init__(self, plots_per_row, window_width=1280, window_height=800):
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
        self._widget = QtWidgets.QWidget()
        self._widget.setLayout(self._layout)
        self._window.setCentralWidget(self._widget)
        self._window.resize(window_width,window_height)
        self._window.show()
        
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
        self._xdata_list.append([])
        self._ydata_list.append([])
        if legend == True:
            self._layout.itemAt(self._num_plots).widget().addLegend()
        self._data_lines_list.append([])
        self._num_plots += 1

    def add_data_line(self, plot_id, data_label, data_color=(255,0,0), data_thickness=15): #add func to change line thickenss
        plot_index = self._plot_dict[plot_id]
        pen = pg.mkPen(color=data_color)
        data_line = self._layout.itemAt(plot_index).widget().plot([],[],
            name = data_label, width=data_thickness, pen=pen)
        self._data_lines_list[plot_index].append(data_line)
        self._xdata_list[plot_index].append([])
        self._ydata_list[plot_index].append([])

    def add_plot_data_point(self, plot_id, dataset_number, xvalue, yvalue):
        index = self._plot_dict[plot_id]
        self._xdata_list[index][dataset_number].append(xvalue)
        self._ydata_list[index][dataset_number].append(yvalue)
        self._data_lines_list[index][dataset_number].setData(self._xdata_list[index][dataset_number],
            self._ydata_list[index][dataset_number])
    
    def update_window(self, sleep_time = 0):
        self._app.processEvents()
        time.sleep(sleep_time)

    def save_image(self,image_name="plotter_image.png"):
        self._widget.grab().save(image_name)

p = Plotter(3)
p.add_plot(plot_id="foo", xlabel="xXx", ylabel="yYy")
p.add_plot(plot_id="", xlabel="xXx", ylabel="yYy")
p.add_plot(plot_id="", xlabel="xXx", ylabel="yYy")
p.add_data_line(plot_id="foo",data_label="truth",data_color=(0,255,0),data_thickness=20)
p.add_plot(plot_id="fi", xlabel="xs", ylabel="ys")
p.add_data_line(plot_id="fi",data_label="estimate",data_color=(0,0,255),data_thickness=10)
p.add_data_line(plot_id="fi",data_label="truth",data_color=(255,0,0),data_thickness=10)
for i in range(10):
    p.add_plot_data_point("foo",0,i,random.randint(0,20))
    p.add_plot_data_point("fi",0,i,random.randint(0,20))
    p.add_plot_data_point("fi",1,i,random.randint(0,20))
    p.update_window(1)
    if i == 9:
        p.save_image()
