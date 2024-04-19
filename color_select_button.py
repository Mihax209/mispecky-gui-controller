from PyQt6 import QtWidgets, QtGui

class ColorSelectButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super(ColorSelectButton, self).__init__(*args, **kwargs)
        self.color = QtGui.QColor(0x4400ff)

        self.color_dialog = QtWidgets.QColorDialog()
        self.color_dialog.currentColorChanged.connect(self.setColor)
        self.color_dialog.setCurrentColor = self.color
        self.color_dialog.hide()
        
        self.clicked.connect(self.color_dialog.show)
        self.setColor(self.color)

    def getColor(self):
        return self.color.name().lstrip('#')

    def setColor(self, color: QtGui.QColor):
        self.color = color
        print(f"New color is {color.name()}")
        
        self.setStyleSheet(f"background-color: {color.name()}")
