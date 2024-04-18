import sys
from PyQt6 import QtWidgets, QtGui, uic
from serial_controller import MispeckySerialController

class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi('ui/mispecky_controller.ui', self)

        self.serial_controller = MispeckySerialController()

        self.createSystemTray()

        self.ledEffectSlider = self.findChild(QtWidgets.QSlider, 'ledEffectSlider')
        self.brightnessSlider = self.findChild(QtWidgets.QSlider, 'brightnessSlider')

        self.ledEffectSlider.valueChanged.connect(self.effectChanged)
        self.brightnessSlider.valueChanged.connect(self.brightnessChanged)

        self.show()

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

    def createSystemTray(self):
        self.tray_icon = QtWidgets.QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('icons/system_tray.png'))
        self.tray_icon.activated.connect(self.icon_activated)

        menu = QtWidgets.QMenu(self)
        open_action = QtGui.QAction("Open", self)
        exit_action = QtGui.QAction("Exit", self)
        open_action.triggered.connect(self.show)
        exit_action.triggered.connect(app.exit)
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
