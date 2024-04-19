import sys, os
from PyQt6 import QtWidgets, QtGui, uic
from serial_controller import MispeckySerialController
from color_select_button import ColorSelectButton
from common import dynamic_file_path

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi(dynamic_file_path('ui/mispecky_controller.ui'), self)
        
        self.setWindowTitle("MiSpecky Controller")

        self.serial_controller = MispeckySerialController()

        self.createSystemTray()

        self.ledEffectSlider = self.findChild(QtWidgets.QSlider, 'ledEffectSlider')
        self.brightnessSlider = self.findChild(QtWidgets.QSlider, 'brightnessSlider')
        self.customColorButton = self.findChild(QtWidgets.QPushButton, 'setCustomColorsButton')

        self.lowColorButton = self.findChild(ColorSelectButton, 'lowColorButton')
        self.midColorButton = self.findChild(ColorSelectButton, 'midColorButton')
        self.highColorButton = self.findChild(ColorSelectButton, 'highColorButton')
        self.lowColorButton.color_dialog.currentColorChanged.connect(self.sendCustomColor)
        self.midColorButton.color_dialog.currentColorChanged.connect(self.sendCustomColor)
        self.highColorButton.color_dialog.currentColorChanged.connect(self.sendCustomColor)

        self.ledEffectSlider.valueChanged.connect(self.effectChanged)
        self.brightnessSlider.valueChanged.connect(self.brightnessChanged)
        self.customColorButton.clicked.connect(self.sendCustomColor)

        self.close()

    def effectChanged(self):
        value = self.ledEffectSlider.value()
        
        try:
            self.serial_controller.send_effect_command(value)
        except TimeoutError:
            print("Timeout error when sending effect command")

    def brightnessChanged(self):
        value = self.brightnessSlider.value()
        
        try:
            self.serial_controller.send_brightness_command(value)
        except TimeoutError:
            print("Timeout error when sending brightness command")

    def sendCustomColor(self):
        low = self.lowColorButton.getColor()
        mid = self.midColorButton.getColor()
        high = self.highColorButton.getColor()
        
        value = ' '.join([low, mid, high])
        
        try:
            self.serial_controller.send_custom_color_command(value)
        except TimeoutError:
            print("Timeout error when sending brightness command")

    def createSystemTray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.activated.connect(self.icon_activated)
        self.tray_icon.setIcon(QtGui.QIcon(dynamic_file_path('icons/system_tray.png')))

        menu = QtWidgets.QMenu(self)
        open_action = QtGui.QAction("Open", self)
        exit_action = QtGui.QAction("Exit", self)
        open_action.triggered.connect(self.show)
        exit_action.triggered.connect(app.exit)  # TODO this feels hacky
        menu.addAction(open_action)
        menu.addAction(exit_action)
        self.tray_icon.setContextMenu(menu)
        
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.show()

    def icon_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick:
            self.showNormal()


app = QtWidgets.QApplication(sys.argv)
window = MainUI()
app.exec()
