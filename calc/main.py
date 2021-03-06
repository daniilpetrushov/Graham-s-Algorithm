import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from calc_design import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Calculator()
    window.setFixedSize(500, 210)
    window.show()

    sys.exit(app.exec())