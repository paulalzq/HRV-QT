#HRV Application

import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import wfdb
import matplotlib.pyplot as plt, mpld3
import matplotlib
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve

from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

matplotlib.use('QT5Agg')


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=18, height=3, dpi=2):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi('interfaz.ui',self)
        self.init_window()
        self.showMaximized() 
        

    def init_window(self):
        self.ui = uic.loadUi('interfaz.ui',self)
        self.pushButtonOpen.clicked.connect(self.abrir_archivo)
        self.baseLineCorrection.clicked.connect(self.baseline_correct)
        self.normalGraphic.clicked.connect(self.normal_plot)
        self.ui.showMaximized()

        #self.ruta= QLabel(self)

    def abrir_archivo(self):
        self.file = QFileDialog.getOpenFileName(self, "Selecciona un archivo", "/home/", "PDF Files (*.dat)")[0]

        record = wfdb.rdrecord(self.file[:-4]) 
        signals, fields = wfdb.rdsamp(self.file[:-4], channels=[0])
        record = wfdb.rdrecord(self.file[:-4], channels=[0])
        signal=signals.reshape(record.sig_len)

        
        def baseline_als(y, lam, p, niter=10):
            L = len(y)
            D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
            D = lam * D.dot(D.transpose()) # Precompute this term since it does not depend on `w`
            w = np.ones(L)
            W = sparse.spdiags(w, 0, L, L)
            for i in range(niter):
                W.setdiag(w) # Do not create a new matrix, just update diagonal values
                Z = W + D
                z = spsolve(Z, w*y)
                w = p * (y > z) + (1-p) * (y < z)
            return z 
        
        record = wfdb.rdrecord(self.file[:-4]) 
        signals, fields = wfdb.rdsamp(self.file[:-4], channels=[0])
        record = wfdb.rdrecord(self.file[:-4], channels=[0])
        self.signal=signals.reshape(record.sig_len)
        # signal_bas=baseline_als(self.signal[:int(len(self.signal)/2)],100,0.001)
        # signal_bas_2=baseline_als(self.signal[int(len(self.signal)/2):int(len(self.signal))],100,0.001)
        # sub_1=np.subtract(self.signal[:int(len(self.signal)/2)],signal_bas)
        # sub_2=np.subtract(self.signal[int(len(self.signal)/2):int(len(self.signal))],signal_bas_2)
        # self.signal_com=np.concatenate((sub_1,sub_2),None)
        
        

    def normal_plot(self):
        
        self.sc1 = MplCanvas(self, width=20, height=8, dpi=50)
        self.sc1.axes.plot(self.signal)
        self.sc = MplCanvas(self, width=35, height=2, dpi=50)
        self.sc.axes.plot(self.signal)
        self.toolbar = NavigationToolbar(self.sc, self)
        self.toolbar1 = NavigationToolbar(self.sc1, self)
        self.ui.ventanaGraficas.addWidget(self.toolbar1)
        self.ui.ventanaGraficas.replaceWidget(self.ui.widgetToolbarBig, self.toolbar1)
        self.toolbar1.minimumHeight()
        self.toolbar1.maximumHeight()
        self.ui.ventanaGraficas.replaceWidget(self.ui.widgetBig, self.sc1)
        self.ui.ventanaGraficas.addWidget(self.toolbar)
        self.ui.ventanaGraficas.replaceWidget(self.ui.widgetToolbarSmall, self.toolbar)
        self.ui.toolbar.minimumHeight()
        self.ui.toolbar.maximumHeight()
        self.ui.ventanaGraficas.replaceWidget(self.ui.widgetSmall, self.sc)
        self.sc.minimumHeight()
        self.sc.maximumHeight()
        self.show()
    

        
    def baseline_correct(self):
        self.sc1.axes.plot(self.signal_com)
        self.sc.axes.plot(self.signal_com)
        self.sc.show()

def main():
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = Window()
    win.show()
    sys.exit(app.exec_())
