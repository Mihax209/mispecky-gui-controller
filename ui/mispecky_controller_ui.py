# Form implementation generated from reading ui file 'c:\Users\Michael M\Documents\Arduino\projects\mispecky_gui_controller\ui\mispecky_controller.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(257, 320)
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 19, 221, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ledEffectLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ledEffectLabel.sizePolicy().hasHeightForWidth())
        self.ledEffectLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ledEffectLabel.setFont(font)
        self.ledEffectLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.ledEffectLabel.setLineWidth(0)
        self.ledEffectLabel.setObjectName("ledEffectLabel")
        self.verticalLayout.addWidget(self.ledEffectLabel)
        self.ledEffectSlider = QtWidgets.QSlider(parent=self.verticalLayoutWidget)
        self.ledEffectSlider.setAutoFillBackground(False)
        self.ledEffectSlider.setMaximum(3)
        self.ledEffectSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.ledEffectSlider.setObjectName("ledEffectSlider")
        self.verticalLayout.addWidget(self.ledEffectSlider)
        self.brightnessLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightnessLabel.sizePolicy().hasHeightForWidth())
        self.brightnessLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.brightnessLabel.setFont(font)
        self.brightnessLabel.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.brightnessLabel.setLineWidth(0)
        self.brightnessLabel.setObjectName("brightnessLabel")
        self.verticalLayout.addWidget(self.brightnessLabel)
        self.brightnessSlider = QtWidgets.QSlider(parent=self.verticalLayoutWidget)
        self.brightnessSlider.setMaximum(100)
        self.brightnessSlider.setSingleStep(10)
        self.brightnessSlider.setPageStep(20)
        self.brightnessSlider.setSliderPosition(1)
        self.brightnessSlider.setTracking(True)
        self.brightnessSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.brightnessSlider.setObjectName("brightnessSlider")
        self.verticalLayout.addWidget(self.brightnessSlider)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 257, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ledEffectLabel.setText(_translate("MainWindow", "LED Effect"))
        self.brightnessLabel.setText(_translate("MainWindow", "Brightness"))
