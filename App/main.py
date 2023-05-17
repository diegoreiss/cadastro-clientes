import sys
from PySide6.QtWidgets import QApplication
from Src.View.main_window import MainWindow


if __name__ == '__main__':
    args = sys.argv
    app = QApplication(args)
    main_window = MainWindow()
    main_window.show()
    app.exec()
