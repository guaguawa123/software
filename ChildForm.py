# -*- coding: utf-8 -*-

"""
Module implementing ChildForm.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget #重要

from Ui_ChildForm import Ui_Form


class ChildForm(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ChildForm, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = ChildForm() #改成class 后面的名字，第13行
    ui.show()
    sys.exit(app.exec_())