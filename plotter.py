from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
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
        widget = QtWidgets.QWidget()
        widget.setLayout(self._layout)
        self.setCentralWidget(widget)

    def add_plot(self, id="", xlabel="x_label", ylabel="y_label"):
        row = self._num_plots//self._plots_per_row
        col = self._num_plots%self._plots_per_row
        plot_widget = pg.PlotWidget()
        plot_widget.setLabel('left', ylabel)
        plot_widget.setLabel('bottom', xlabel)
        self._layout.addWidget(pg.PlotWidget(),row,col)
        if id == "":
            id = str(self._num_plots)
        self._plot_dict[id] = self._num_plots
        self._num_plots += 1


        # self.x1 = list(range(100))  # 100 time points
        # self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        # self.x2 = list(range(100))  # 100 time points
        # self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points
        # self.x3 = list(range(100))  # 100 time points
        # self.y3 = [randint(0,100) for _ in range(100)]  # 100 data points

        # pen = pg.mkPen(color=(255, 0, 0))
        # self.data1_line =  self.layout.itemAt(0).widget().plot(self.x1, self.y1, pen=pen)
        # self.data2_line =  self.layout.itemAt(0).widget().plot(self.x2, self.y2, pen=pen)
        # self.data3_line =  self.layout.itemAt(0).widget().plot(self.x3, self.y3, pen=pen)
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(50)
        # self.timer.timeout.connect(self.update_plot_data)
        # self.timer.start()

    # def update_plot_data(self):

    #     self.x1 = self.x1[1:]  # Remove the first y element.
    #     self.x1.append(self.x1[-1] + 1)  # Add a new value 1 higher than the last.
    #     self.y1 = self.y1[1:]  # Remove the first
    #     self.y1.append( randint(0,100))  # Add a new random value.
    #     self.data1_line.setData(self.x1, self.y1)  # Update the data.

    #     self.x2 = self.x2[1:]  # Remove the first y element.
    #     self.x2.append(self.x2[-1] + 1)  # Add a new value 2 higher than the last.
    #     self.y2 = self.y2[1:]  # Remove the first
    #     self.y2.append( randint(0,100))  # Add a new random value.
    #     self.data2_line.setData(self.x2, self.y2)  # Update the data.

    #     self.x3 = self.x3[1:]  # Remove the first y element.
    #     self.x3.append(self.x3[-1] + 1)  # Add a new value 3 higher than the last.
    #     self.y3 = self.y3[1:]  # Remove the first
    #     self.y3.append( randint(0,100))  # Add a new random value.
    #     self.data3_line.setData(self.x3, self.y3)  # Update the data.


app = QtWidgets.QApplication(sys.argv)
plotter = Plotter(2)
plotter.add_plot("id1", xlabel="time", ylabel="units")
plotter.add_plot("id1", xlabel="time", ylabel="units")
plotter.add_plot("id1", xlabel="time", ylabel="units")
plotter.add_plot("id1", xlabel="time", ylabel="units")
plotter.add_plot("id1", xlabel="time", ylabel="units")

plotter.show()
sys.exit(app.exec())