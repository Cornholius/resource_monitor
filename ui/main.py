from random import random, randint

from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # window requirements
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Creating PieChart")
        self.setWindowIcon(QIcon("python.png"))

        # change the color of the window
        self.setStyleSheet('background-color:red')

        # create pieseries
        series = QPieSeries()

        # append some data to the series
        series.append("Apple", 80)
        series.append("Banana", 20)


        colors = [Qt.green, Qt.cyan, Qt.yellow, Qt.black]
        # slice
        my_slice = series.slices()
        # my_slice.setExploded(True)
        for i in my_slice:
            i.setLabelVisible(True)
            # i.setPen(QPen(Qt.yellow, 4))
            i.setBrush(colors[randint(0, 3)])

        # create QChart object
        chart = QChart()
        chart.addSeries(series)
        # chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Fruits Pie Chart")
        # chart.setTheme(QChart.ChartThemeDark)

        # create QChartView object and add chart in thier
        chartview = QChartView(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartview)

        self.setLayout(vbox)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, ):
        super().__init__()
        self.resize(320, 600)
        self.setStyleSheet("background-color: #cccccc")
        self.proc_widget()

    def proc_widget(self):
        processor = QtWidgets.QWidget(self)
        processor.setGeometry(QtCore.QRect(10, 10, 300, 200))
        processor.setToolTipDuration(0)
        processor.setStyleSheet("""
        background-color: #ffffff;
        border-radius: 10px;
        """)
        processor.setObjectName("processor")
        processor.setLayout(self.ololo())

    def ololo(self):

        series = QPieSeries()
        series.setHorizontalPosition(.8)
        series.setHoleSize(.35)
        series.append("Занято", 80)
        series.append("Свободно", 20)
        series.setPieSize(1.0)
        slices = series.slices()
        slices[0].setBrush(Qt.green)
        slices[1].setBrush(Qt.gray)
        # for i in slices:
        #     i.setLabelVisible(True)
        chart = QChart()
        chart.addSeries(series)
        # chart.setTitle("Fruits Pie Chart")
        chart.setTheme(QChart.ChartThemeDark)
        chartview = QChartView(chart)
        vbox = QVBoxLayout()
        vbox.addWidget(chartview)
        return vbox





#     def setupUi(self, mainWindow):
#         mainWindow.setObjectName("mainWindow")
#         mainWindow.resize(320, 600)
#         mainWindow.setWindowOpacity(1.0)
#         mainWindow.setStyleSheet("background-color: #cccccc")
#         self.processor = QtWidgets.QWidget(mainWindow)
#         self.processor.setGeometry(QtCore.QRect(10, 10, 300, 300))
#         self.processor.setToolTipDuration(0)
#         self.processor.setStyleSheet("background-color: #ffffff;\n"
# "border-radius: 10px;")
#         self.processor.setObjectName("processor")
#         self.proc_logo = QtWidgets.QWidget(self.processor)
#         self.proc_logo.setGeometry(QtCore.QRect(10, 10, 64, 64))
#         self.proc_logo.setStyleSheet("background-color: #000000")
#         self.proc_logo.setObjectName("proc_logo")
#
#         self.retranslateUi(mainWindow)
#         QtCore.QMetaObject.connectSlotsByName(mainWindow)
#
#     def retranslateUi(self, mainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         mainWindow.setWindowTitle(_translate("mainWindow", "Form"))
