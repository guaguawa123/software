# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget

from Ui_software import Ui_MainWindow  #这个是去点Ui_software前面的点
from Ui_ChildForm import  Ui_Form #新加行

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_action_56_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 显示联合规划模块
        ch.show()


    
    @pyqtSlot()
    def on_action_57_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ch.show()
    
    @pyqtSlot()
    def on_action_58_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        ch.show()

#从ChildForm导入class类
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
    #实体化主窗口
    ui = MainWindow()
    #实例化子窗体
    ch = ChildForm()
    ui.show()
    sys.exit(app.exec_())