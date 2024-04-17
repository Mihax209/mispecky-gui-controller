import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt

from serial_controller import MispeckySerialController

class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('ui/mispecky_controller.ui', self)

        self.serial_controller = MispeckySerialController()

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


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec()
