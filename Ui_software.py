# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\软件设计\software\software.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 749)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setKerning(True)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 791))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        self.verticalLayout_2.addWidget(self.treeWidget_3)
        self.treeWidget_4 = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget_4.setObjectName("treeWidget_4")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_4)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_4)
        self.verticalLayout_2.addWidget(self.treeWidget_4)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.tableWidget_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 856, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setTearOffEnabled(False)
        self.menu.setObjectName("menu")
        self.menu_8 = QtWidgets.QMenu(self.menu)
        self.menu_8.setObjectName("menu_8")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setObjectName("menu_5")
        self.menu_9 = QtWidgets.QMenu(self.menu_5)
        self.menu_9.setObjectName("menu_9")
        self.menu_6 = QtWidgets.QMenu(self.menuBar)
        self.menu_6.setObjectName("menu_6")
        self.menu_7 = QtWidgets.QMenu(self.menuBar)
        self.menu_7.setObjectName("menu_7")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_4.setObjectName("toolBar_4")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        self.action_3 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/newfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_3.setIcon(icon)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.openfile = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/openversionfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openfile.setIcon(icon1)
        self.openfile.setObjectName("openfile")
        self.newfile = QtWidgets.QAction(MainWindow)
        self.newfile.setIcon(icon)
        self.newfile.setObjectName("newfile")
        self.saveproject = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/saveversionfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveproject.setIcon(icon2)
        self.saveproject.setObjectName("saveproject")
        self.撤回操作 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.撤回操作.setIcon(icon3)
        self.撤回操作.setObjectName("撤回操作")
        self.恢复 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/forword.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.恢复.setIcon(icon4)
        self.恢复.setObjectName("恢复")
        self.运行 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/run.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.运行.setIcon(icon5)
        self.运行.setObjectName("运行")
        self.traffic_network = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/3D_Road_network_View.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.traffic_network.setIcon(icon6)
        self.traffic_network.setObjectName("traffic_network")
        self.计算流程序列 = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/Sequence_of_computation_flow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.计算流程序列.setIcon(icon7)
        self.计算流程序列.setObjectName("计算流程序列")
        self.电网图 = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/电网图.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.电网图.setIcon(icon8)
        self.电网图.setObjectName("电网图")
        self.交通时刻表 = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/Timetable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.交通时刻表.setIcon(icon9)
        self.交通时刻表.setObjectName("交通时刻表")
        self.action_3_1_AnsysEM_position_0mm_70_2mm_7_02mm_current_0A_200A_20A_3_1_3_2_3_1_3_2_Simulink_Lookup_Table_Lookup_Table_3_2_A_3_3_A_UA_R_A_xA_v_A_IA_A_FA_2_D_Lookup_Table_u1_u2_flux_flux1_flux2_3_3_A_A_1_3_1_3_2_3_3_3_3_0_1_Lookup_Table_C_0_0001_A_3_3_3_4_UABC_IABC_F_v_x_3_4_Lookup_Table_K_0_001_70_2mm_70_2mm_B_C_A_23_4mm_46_8mm_rem_Lookup_Table_F_3_5_3_5_3_4_3_6_Udc_pulse_IABC_UABC_3_6_3_6_Udc_514V_3_7_A_U_A_pulseA_A_IA_A_UA_3_7_A_3_7_1_A_A_UA_U_A_A_A_UA_U_A_UA_3_5_PC_CCC_PWM_3_5_1_3_8_x_PulseABC_3_8_x_1000_70_2mm_70_2mm_Rem_Simulink_70_2_ABC_3_9_A_3_9_A_3_8_A_0_7mm_23_4mm_24_1mm_A_3_5_2_3_10_3_10_180A_180A_180_3_0_180A_UA_U_177A_1_UA_U_3_5_3_PWM_3_11_PWM_DUTY_Pulseabc_pulse_3_11_PWM_PWM_1_50_s_DUTY_0_1_Pulseabc_DUTY_PWM_DUTY = QtWidgets.QAction(MainWindow)
        self.action_3_1_AnsysEM_position_0mm_70_2mm_7_02mm_current_0A_200A_20A_3_1_3_2_3_1_3_2_Simulink_Lookup_Table_Lookup_Table_3_2_A_3_3_A_UA_R_A_xA_v_A_IA_A_FA_2_D_Lookup_Table_u1_u2_flux_flux1_flux2_3_3_A_A_1_3_1_3_2_3_3_3_3_0_1_Lookup_Table_C_0_0001_A_3_3_3_4_UABC_IABC_F_v_x_3_4_Lookup_Table_K_0_001_70_2mm_70_2mm_B_C_A_23_4mm_46_8mm_rem_Lookup_Table_F_3_5_3_5_3_4_3_6_Udc_pulse_IABC_UABC_3_6_3_6_Udc_514V_3_7_A_U_A_pulseA_A_IA_A_UA_3_7_A_3_7_1_A_A_UA_U_A_A_A_UA_U_A_UA_3_5_PC_CCC_PWM_3_5_1_3_8_x_PulseABC_3_8_x_1000_70_2mm_70_2mm_Rem_Simulink_70_2_ABC_3_9_A_3_9_A_3_8_A_0_7mm_23_4mm_24_1mm_A_3_5_2_3_10_3_10_180A_180A_180_3_0_180A_UA_U_177A_1_UA_U_3_5_3_PWM_3_11_PWM_DUTY_Pulseabc_pulse_3_11_PWM_PWM_1_50_s_DUTY_0_1_Pulseabc_DUTY_PWM_DUTY.setObjectName("action_3_1_AnsysEM_position_0mm_70_2mm_7_02mm_current_0A_200A_20A_3_1_3_2_3_1_3_2_Simulink_Lookup_Table_Lookup_Table_3_2_A_3_3_A_UA_R_A_xA_v_A_IA_A_FA_2_D_Lookup_Table_u1_u2_flux_flux1_flux2_3_3_A_A_1_3_1_3_2_3_3_3_3_0_1_Lookup_Table_C_0_0001_A_3_3_3_4_UABC_IABC_F_v_x_3_4_Lookup_Table_K_0_001_70_2mm_70_2mm_B_C_A_23_4mm_46_8mm_rem_Lookup_Table_F_3_5_3_5_3_4_3_6_Udc_pulse_IABC_UABC_3_6_3_6_Udc_514V_3_7_A_U_A_pulseA_A_IA_A_UA_3_7_A_3_7_1_A_A_UA_U_A_A_A_UA_U_A_UA_3_5_PC_CCC_PWM_3_5_1_3_8_x_PulseABC_3_8_x_1000_70_2mm_70_2mm_Rem_Simulink_70_2_ABC_3_9_A_3_9_A_3_8_A_0_7mm_23_4mm_24_1mm_A_3_5_2_3_10_3_10_180A_180A_180_3_0_180A_UA_U_177A_1_UA_U_3_5_3_PWM_3_11_PWM_DUTY_Pulseabc_pulse_3_11_PWM_PWM_1_50_s_DUTY_0_1_Pulseabc_DUTY_PWM_DUTY")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.action_16 = QtWidgets.QAction(MainWindow)
        self.action_16.setIcon(icon1)
        self.action_16.setObjectName("action_16")
        self.action_17 = QtWidgets.QAction(MainWindow)
        self.action_17.setIcon(icon2)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(MainWindow)
        self.action_18.setObjectName("action_18")
        self.action_19 = QtWidgets.QAction(MainWindow)
        self.action_19.setObjectName("action_19")
        self.action_21 = QtWidgets.QAction(MainWindow)
        self.action_21.setObjectName("action_21")
        self.action_22 = QtWidgets.QAction(MainWindow)
        self.action_22.setObjectName("action_22")
        self.action_23 = QtWidgets.QAction(MainWindow)
        self.action_23.setObjectName("action_23")
        self.action_24 = QtWidgets.QAction(MainWindow)
        self.action_24.setObjectName("action_24")
        self.action_27 = QtWidgets.QAction(MainWindow)
        self.action_27.setObjectName("action_27")
        self.action_28 = QtWidgets.QAction(MainWindow)
        self.action_28.setObjectName("action_28")
        self.action_29 = QtWidgets.QAction(MainWindow)
        self.action_29.setObjectName("action_29")
        self.action_30 = QtWidgets.QAction(MainWindow)
        self.action_30.setIcon(icon6)
        self.action_30.setObjectName("action_30")
        self.action_32 = QtWidgets.QAction(MainWindow)
        self.action_32.setIcon(icon7)
        self.action_32.setObjectName("action_32")
        self.action_34 = QtWidgets.QAction(MainWindow)
        self.action_34.setObjectName("action_34")
        self.action_35 = QtWidgets.QAction(MainWindow)
        self.action_35.setObjectName("action_35")
        self.action_37 = QtWidgets.QAction(MainWindow)
        self.action_37.setObjectName("action_37")
        self.action_41 = QtWidgets.QAction(MainWindow)
        self.action_41.setObjectName("action_41")
        self.action_42 = QtWidgets.QAction(MainWindow)
        self.action_42.setObjectName("action_42")
        self.action_44 = QtWidgets.QAction(MainWindow)
        self.action_44.setObjectName("action_44")
        self.actionOD = QtWidgets.QAction(MainWindow)
        self.actionOD.setObjectName("actionOD")
        self.action_45 = QtWidgets.QAction(MainWindow)
        self.action_45.setObjectName("action_45")
        self.action_46 = QtWidgets.QAction(MainWindow)
        self.action_46.setObjectName("action_46")
        self.action_48 = QtWidgets.QAction(MainWindow)
        self.action_48.setObjectName("action_48")
        self.action_49 = QtWidgets.QAction(MainWindow)
        self.action_49.setIcon(icon5)
        self.action_49.setObjectName("action_49")
        self.action_51 = QtWidgets.QAction(MainWindow)
        self.action_51.setObjectName("action_51")
        self.action_52 = QtWidgets.QAction(MainWindow)
        self.action_52.setObjectName("action_52")
        self.action_53 = QtWidgets.QAction(MainWindow)
        self.action_53.setObjectName("action_53")
        self.action_56 = QtWidgets.QAction(MainWindow)
        self.action_56.setCheckable(True)
        self.action_56.setChecked(True)
        self.action_56.setObjectName("action_56")
        self.action_57 = QtWidgets.QAction(MainWindow)
        self.action_57.setObjectName("action_57")
        self.action_58 = QtWidgets.QAction(MainWindow)
        self.action_58.setObjectName("action_58")
        self.action_59 = QtWidgets.QAction(MainWindow)
        self.action_59.setObjectName("action_59")
        self.action_60 = QtWidgets.QAction(MainWindow)
        self.action_60.setObjectName("action_60")
        self.action_62 = QtWidgets.QAction(MainWindow)
        self.action_62.setObjectName("action_62")
        self.action_31 = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("F:\\软件设计\\software\\picture/home_page.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_31.setIcon(icon10)
        self.action_31.setObjectName("action_31")
        self.menu_8.addAction(self.action_3_1_AnsysEM_position_0mm_70_2mm_7_02mm_current_0A_200A_20A_3_1_3_2_3_1_3_2_Simulink_Lookup_Table_Lookup_Table_3_2_A_3_3_A_UA_R_A_xA_v_A_IA_A_FA_2_D_Lookup_Table_u1_u2_flux_flux1_flux2_3_3_A_A_1_3_1_3_2_3_3_3_3_0_1_Lookup_Table_C_0_0001_A_3_3_3_4_UABC_IABC_F_v_x_3_4_Lookup_Table_K_0_001_70_2mm_70_2mm_B_C_A_23_4mm_46_8mm_rem_Lookup_Table_F_3_5_3_5_3_4_3_6_Udc_pulse_IABC_UABC_3_6_3_6_Udc_514V_3_7_A_U_A_pulseA_A_IA_A_UA_3_7_A_3_7_1_A_A_UA_U_A_A_A_UA_U_A_UA_3_5_PC_CCC_PWM_3_5_1_3_8_x_PulseABC_3_8_x_1000_70_2mm_70_2mm_Rem_Simulink_70_2_ABC_3_9_A_3_9_A_3_8_A_0_7mm_23_4mm_24_1mm_A_3_5_2_3_10_3_10_180A_180A_180_3_0_180A_UA_U_177A_1_UA_U_3_5_3_PWM_3_11_PWM_DUTY_Pulseabc_pulse_3_11_PWM_PWM_1_50_s_DUTY_0_1_Pulseabc_DUTY_PWM_DUTY)
        self.menu_8.addAction(self.action_2)
        self.menu_8.addAction(self.action_6)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_23)
        self.menu.addAction(self.action_16)
        self.menu.addAction(self.menu_8.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.action_17)
        self.menu.addAction(self.action_7)
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_9)
        self.menu.addSeparator()
        self.menu.addAction(self.action_10)
        self.menu.addSeparator()
        self.menu.addAction(self.action_18)
        self.menu.addAction(self.action_19)
        self.menu.addSeparator()
        self.menu.addAction(self.action_21)
        self.menu.addAction(self.action_22)
        self.menu.addAction(self.action_24)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_27)
        self.menu_2.addAction(self.action_28)
        self.menu_2.addAction(self.action_29)
        self.menu_3.addAction(self.action_32)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_30)
        self.menu_3.addAction(self.action_31)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_41)
        self.menu_3.addAction(self.action_42)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_34)
        self.menu_3.addAction(self.action_35)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_59)
        self.menu_3.addAction(self.action_37)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_44)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.action_46)
        self.menu_3.addAction(self.action_48)
        self.menu_4.addAction(self.actionOD)
        self.menu_4.addAction(self.action_45)
        self.menu_9.addAction(self.action_56)
        self.menu_9.addAction(self.action_57)
        self.menu_9.addAction(self.action_58)
        self.menu_5.addAction(self.action_49)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.menu_9.menuAction())
        self.menu_5.addAction(self.action_51)
        self.menu_5.addAction(self.action_52)
        self.menu_5.addAction(self.action_53)
        self.menu_5.addSeparator()
        self.menu_6.addAction(self.action_60)
        self.menu_6.addSeparator()
        self.menu_6.addAction(self.action_62)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.menuBar.addAction(self.menu_6.menuAction())
        self.menuBar.addAction(self.menu_7.menuAction())
        self.toolBar.addAction(self.newfile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.openfile)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.saveproject)
        self.toolBar.addSeparator()
        self.toolBar_2.addAction(self.撤回操作)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.恢复)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.运行)
        self.toolBar_2.addAction(self.计算流程序列)
        self.toolBar_2.addSeparator()
        self.toolBar_3.addAction(self.action_31)
        self.toolBar_3.addAction(self.电网图)
        self.toolBar_3.addAction(self.traffic_network)
        self.toolBar_3.addAction(self.交通时刻表)
        self.toolBar_3.addSeparator()
        self.toolBar_3.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "交通网络数据"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "网络节点"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "网络车辆数"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.treeWidget_4.headerItem().setText(0, _translate("MainWindow", "负荷数据"))
        __sortingEnabled = self.treeWidget_4.isSortingEnabled()
        self.treeWidget_4.setSortingEnabled(False)
        self.treeWidget_4.topLevelItem(0).setText(0, _translate("MainWindow", "电动汽车负荷数据"))
        self.treeWidget_4.topLevelItem(1).setText(0, _translate("MainWindow", "燃料电池汽车负荷数据"))
        self.treeWidget_4.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "电力网络节点电压"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "电力网络节点电流"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "节点有功功率"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "节点无功功率"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_8.setTitle(_translate("MainWindow", "打开工程文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "视图"))
        self.menu_4.setTitle(_translate("MainWindow", "列表"))
        self.menu_5.setTitle(_translate("MainWindow", "计算"))
        self.menu_9.setTitle(_translate("MainWindow", "规划模块"))
        self.menu_6.setTitle(_translate("MainWindow", "路图"))
        self.menu_7.setTitle(_translate("MainWindow", "帮助"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar_4"))
        self.action_3.setText(_translate("MainWindow", "新建工程文件"))
        self.action_4.setText(_translate("MainWindow", "撤销"))
        self.action_5.setText(_translate("MainWindow", "返回"))
        self.openfile.setText(_translate("MainWindow", "openfile"))
        self.openfile.setToolTip(_translate("MainWindow", "打开文件"))
        self.newfile.setText(_translate("MainWindow", "newfile"))
        self.newfile.setToolTip(_translate("MainWindow", "新建"))
        self.saveproject.setText(_translate("MainWindow", "saveproject"))
        self.saveproject.setToolTip(_translate("MainWindow", "保存工程"))
        self.撤回操作.setText(_translate("MainWindow", "back"))
        self.撤回操作.setToolTip(_translate("MainWindow", "撤回操作"))
        self.恢复.setText(_translate("MainWindow", "recover"))
        self.恢复.setToolTip(_translate("MainWindow", "恢复"))
        self.运行.setText(_translate("MainWindow", "run"))
        self.运行.setToolTip(_translate("MainWindow", "运行"))
        self.traffic_network.setText(_translate("MainWindow", "交通网络图"))
        self.traffic_network.setToolTip(_translate("MainWindow", "交通网络图"))
        self.计算流程序列.setText(_translate("MainWindow", "计算流程序列"))
        self.计算流程序列.setToolTip(_translate("MainWindow", "计算流程序列"))
        self.电网图.setText(_translate("MainWindow", "电网图"))
        self.电网图.setToolTip(_translate("MainWindow", "电网图"))
        self.交通时刻表.setText(_translate("MainWindow", "交通时刻表"))
        self.交通时刻表.setToolTip(_translate("MainWindow", "交通时刻表"))
        self.action_3_1_AnsysEM_position_0mm_70_2mm_7_02mm_current_0A_200A_20A_3_1_3_2_3_1_3_2_Simulink_Lookup_Table_Lookup_Table_3_2_A_3_3_A_UA_R_A_xA_v_A_IA_A_FA_2_D_Lookup_Table_u1_u2_flux_flux1_flux2_3_3_A_A_1_3_1_3_2_3_3_3_3_0_1_Lookup_Table_C_0_0001_A_3_3_3_4_UABC_IABC_F_v_x_3_4_Lookup_Table_K_0_001_70_2mm_70_2mm_B_C_A_23_4mm_46_8mm_rem_Lookup_Table_F_3_5_3_5_3_4_3_6_Udc_pulse_IABC_UABC_3_6_3_6_Udc_514V_3_7_A_U_A_pulseA_A_IA_A_UA_3_7_A_3_7_1_A_A_UA_U_A_A_A_UA_U_A_UA_3_5_PC_CCC_PWM_3_5_1_3_8_x_PulseABC_3_8_x_1000_70_2mm_70_2mm_Rem_Simulink_70_2_ABC_3_9_A_3_9_A_3_8_A_0_7mm_23_4mm_24_1mm_A_3_5_2_3_10_3_10_180A_180A_180_3_0_180A_UA_U_177A_1_UA_U_3_5_3_PWM_3_11_PWM_DUTY_Pulseabc_pulse_3_11_PWM_PWM_1_50_s_DUTY_0_1_Pulseabc_DUTY_PWM_DUTY.setText(_translate("MainWindow", "导入交通数据"))
        self.action_2.setText(_translate("MainWindow", "导入电网数据"))
        self.action_6.setText(_translate("MainWindow", "导入充注一体站数据"))
        self.action_7.setText(_translate("MainWindow", "保存工程文件"))
        self.action_8.setText(_translate("MainWindow", "保存交通路图"))
        self.action_9.setText(_translate("MainWindow", "保存一体站布局"))
        self.action_10.setText(_translate("MainWindow", "另存为"))
        self.action_16.setText(_translate("MainWindow", "打开工程"))
        self.action_17.setText(_translate("MainWindow", "保存"))
        self.action_18.setText(_translate("MainWindow", "导出路网图形"))
        self.action_19.setText(_translate("MainWindow", "打印路网图形"))
        self.action_21.setText(_translate("MainWindow", "显示日志文件"))
        self.action_22.setText(_translate("MainWindow", "工程历史版本"))
        self.action_23.setText(_translate("MainWindow", "最近工程文件"))
        self.action_24.setText(_translate("MainWindow", "工程属性"))
        self.action_27.setText(_translate("MainWindow", "复制"))
        self.action_28.setText(_translate("MainWindow", "粘贴"))
        self.action_29.setText(_translate("MainWindow", "重做"))
        self.action_30.setText(_translate("MainWindow", "交通路图编辑器"))
        self.action_32.setText(_translate("MainWindow", "计算过程序列显示"))
        self.action_34.setText(_translate("MainWindow", "电负荷需求显示"))
        self.action_35.setText(_translate("MainWindow", "氢负荷需求显示"))
        self.action_37.setText(_translate("MainWindow", "交通车辆状态显示"))
        self.action_41.setText(_translate("MainWindow", "电力网络编辑器"))
        self.action_42.setText(_translate("MainWindow", "电力网络主界面"))
        self.action_44.setText(_translate("MainWindow", "电氢充注一体站设备数据"))
        self.actionOD.setText(_translate("MainWindow", "OD(出发地/目的地)"))
        self.action_45.setText(_translate("MainWindow", "交通路网的车辆行驶表"))
        self.action_46.setText(_translate("MainWindow", "编辑道路路径模拟阻抗"))
        self.action_48.setText(_translate("MainWindow", "编辑道路节点模拟阻抗"))
        self.action_49.setText(_translate("MainWindow", "运行"))
        self.action_51.setText(_translate("MainWindow", "设计模块"))
        self.action_52.setText(_translate("MainWindow", "运行模拟模块"))
        self.action_53.setText(_translate("MainWindow", "综合评价"))
        self.action_56.setText(_translate("MainWindow", "联合规划模块"))
        self.action_57.setText(_translate("MainWindow", "交互规划模块"))
        self.action_58.setText(_translate("MainWindow", "选址定容模块"))
        self.action_59.setText(_translate("MainWindow", "编辑交通数据"))
        self.action_60.setText(_translate("MainWindow", "路网设置"))
        self.action_62.setText(_translate("MainWindow", "车辆行驶路程定义"))
        self.action_31.setText(_translate("MainWindow", "交通路网主界面"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())