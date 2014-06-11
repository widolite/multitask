# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindowrelay.ui'
#
# Created: Sat Apr 26 23:02:11 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindowRelay(object):
    def setupUi(self, MainWindowRelay):
        MainWindowRelay.setObjectName("MainWindowRelay")
        MainWindowRelay.resize(215, 246)
        self.central_widget = QtGui.QWidget(MainWindowRelay)
        self.central_widget.setObjectName("central_widget")
        self.gridLayout_3 = QtGui.QGridLayout(self.central_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setObjectName("grid_layout")
        self.grid_layout_0 = QtGui.QGridLayout()
        self.grid_layout_0.setObjectName("grid_layout_0")
        self.horizontal_layout_0 = QtGui.QHBoxLayout()
        self.horizontal_layout_0.setObjectName("horizontal_layout_0")
        self.time_label = QtGui.QLabel(self.central_widget)
        self.time_label.setObjectName("time_label")
        self.horizontal_layout_0.addWidget(self.time_label)
        self.temp_double_spin_box = QtGui.QDoubleSpinBox(self.central_widget)
        self.temp_double_spin_box.setDecimals(1)
        self.temp_double_spin_box.setMaximum(300.0)
        self.temp_double_spin_box.setSingleStep(0.5)
        self.temp_double_spin_box.setObjectName("temp_double_spin_box")
        self.horizontal_layout_0.addWidget(self.temp_double_spin_box)
        self.temp_dial = QtGui.QDial(self.central_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.temp_dial.sizePolicy().hasHeightForWidth())
        self.temp_dial.setSizePolicy(sizePolicy)
        self.temp_dial.setMinimumSize(QtCore.QSize(50, 0))
        self.temp_dial.setMaximumSize(QtCore.QSize(55, 16777215))
        self.temp_dial.setMaximum(300)
        self.temp_dial.setObjectName("temp_dial")
        self.horizontal_layout_0.addWidget(self.temp_dial)
        self.grid_layout_0.addLayout(self.horizontal_layout_0, 2, 0, 1, 1)
        self.relay_button = QtGui.QPushButton(self.central_widget)
        self.relay_button.setStyleSheet("color: rgb(85, 170, 0);")
        self.relay_button.setObjectName("relay_button")
        self.grid_layout_0.addWidget(self.relay_button, 1, 0, 1, 1)
        self.horizontal_layout = QtGui.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.relays_label = QtGui.QLabel(self.central_widget)
        self.relays_label.setObjectName("relays_label")
        self.horizontal_layout.addWidget(self.relays_label)
        self.relays_combo_box = QtGui.QComboBox(self.central_widget)
        self.relays_combo_box.setObjectName("relays_combo_box")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.relays_combo_box.addItem("")
        self.horizontal_layout.addWidget(self.relays_combo_box)
        self.grid_layout_0.addLayout(self.horizontal_layout, 0, 0, 1, 1)
        self.grid_layout.addLayout(self.grid_layout_0, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.grid_layout, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 1, 1, 1)
        MainWindowRelay.setCentralWidget(self.central_widget)
        self.menu_bar = QtGui.QMenuBar(MainWindowRelay)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 215, 21))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_edit = QtGui.QMenu(self.menu_bar)
        self.menu_edit.setObjectName("menu_edit")
        MainWindowRelay.setMenuBar(self.menu_bar)
        self.main_tool_bar = QtGui.QToolBar(MainWindowRelay)
        self.main_tool_bar.setObjectName("main_tool_bar")
        MainWindowRelay.addToolBar(QtCore.Qt.TopToolBarArea, self.main_tool_bar)
        self.status_bar = QtGui.QStatusBar(MainWindowRelay)
        self.status_bar.setObjectName("status_bar")
        MainWindowRelay.setStatusBar(self.status_bar)
        self.action_conection = QtGui.QAction(MainWindowRelay)
        self.action_conection.setObjectName("action_conection")
        self.action_relays = QtGui.QAction(MainWindowRelay)
        self.action_relays.setObjectName("action_relays")
        self.action_close = QtGui.QAction(MainWindowRelay)
        self.action_close.setObjectName("action_close")
        self.menu_edit.addAction(self.action_conection)
        self.menu_edit.addAction(self.action_relays)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_close)
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.time_label.setBuddy(self.temp_double_spin_box)
        self.relays_label.setBuddy(self.relays_combo_box)

        self.retranslateUi(MainWindowRelay)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRelay)

    def retranslateUi(self, MainWindowRelay):
        MainWindowRelay.setWindowTitle(QtGui.QApplication.translate("MainWindowRelay", "MainWindowRelay", None, QtGui.QApplication.UnicodeUTF8))
        self.time_label.setText(QtGui.QApplication.translate("MainWindowRelay", "&Temporizador", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_double_spin_box.setSuffix(QtGui.QApplication.translate("MainWindowRelay", " seg", None, QtGui.QApplication.UnicodeUTF8))
        self.relay_button.setText(QtGui.QApplication.translate("MainWindowRelay", "E&ncender", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_label.setText(QtGui.QApplication.translate("MainWindowRelay", "Co&mpuertas:", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(0, QtGui.QApplication.translate("MainWindowRelay", "Relay 1", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(1, QtGui.QApplication.translate("MainWindowRelay", "Relay 2", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(2, QtGui.QApplication.translate("MainWindowRelay", "Relay 3", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(3, QtGui.QApplication.translate("MainWindowRelay", "Relay 4", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(4, QtGui.QApplication.translate("MainWindowRelay", "Relay 5", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(5, QtGui.QApplication.translate("MainWindowRelay", "Relay 6", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(6, QtGui.QApplication.translate("MainWindowRelay", "Relay 7", None, QtGui.QApplication.UnicodeUTF8))
        self.relays_combo_box.setItemText(7, QtGui.QApplication.translate("MainWindowRelay", "Relay 8", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_edit.setTitle(QtGui.QApplication.translate("MainWindowRelay", "&Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_conection.setText(QtGui.QApplication.translate("MainWindowRelay", "&Conexion", None, QtGui.QApplication.UnicodeUTF8))
        self.action_relays.setText(QtGui.QApplication.translate("MainWindowRelay", "C&ompuertas", None, QtGui.QApplication.UnicodeUTF8))
        self.action_close.setText(QtGui.QApplication.translate("MainWindowRelay", "C&errar", None, QtGui.QApplication.UnicodeUTF8))

