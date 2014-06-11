# -*- coding: utf-8 -*-
__author__ = 'Ing. Hector Guerrero Landaeta'
__mail__ = 'hectorguerrero1866@gmail.com'

from PySide.QtGui import *
from PySide.QtCore import *

from relaylib import *
from ui_mainwindowrelay import *
import qrc_resources

__app__ = "Web Relay Multitask"


class RenderRelayDataThread(QThread):
    done = Signal(str, str)

    error = Signal(str)

    def __init__(self, rel_num=0, sec=float(0), parent=None):
        super(RenderRelayDataThread, self).__init__(parent)
        self.__rel_num = rel_num
        self.__sec = sec

    def run(self):

        try:
            relay_lib = RelayLib()
            if relay_lib.status[self.__rel_num] == 1:
                relay_lib.toggle(self.__rel_num + 1)
            relay_lib.toggle(self.__rel_num + 1)
            time.sleep(self.__sec)
            relay_lib.toggle(self.__rel_num + 1)
            self.done.emit(str(self.__rel_num + 1), str(self.__sec))

        except BoardConnectionError:

            self.error.emit(str("The connection with the board is lost"))

        except CustomURLError:

            self.error.emit(str("Authentication failed. "))

    @property
    def rel_num(self):
        return self.rel_num

    @rel_num.setter
    def rel_num(self, value):
        self.__rel_num = value

    @property
    def sec(self):
        return self.sec

    @sec.setter
    def sec(self, value):
        self.__sec = value


class EnableAllRelays(QThread):
    done = Signal(str)

    error = Signal(str)

    def __init__(self, parent=None):
        super(EnableAllRelays, self).__init__(parent)

    def run(self):

        relay_lib = RelayLib()

        for relay in RelayLib.relays:

            if relay_lib.status[relay - 1] == 1:
                continue
            relay_lib.toggle(relay)

        self.done.emit("All the relays had been enabled")


class MainWindowRelay(QMainWindow, Ui_MainWindowRelay):
    def __init__(self, parent=None):
        super(MainWindowRelay, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(__app__)
        self.temp_dial.valueChanged.connect(self.temp_double_spin_box.setValue)
        self.temp_double_spin_box.valueChanged.connect(self.temp_dial.setValue)
        self.relay_button.clicked.connect(self.toggle, Qt.UniqueConnection)
        self.relays_combo_box.currentIndexChanged.connect(self.clear_ui)
        q_action_relay_open = QAction(QIcon(":/open.ico"), "All-&Enabled", self)
        q_action_relay_open.setShortcut("Ctrl+L")
        help_text = "Enable all relays"
        q_action_relay_open.setToolTip(help_text)
        q_action_relay_open.setStatusTip(help_text)
        q_action_relay_open.setCheckable(True)
        q_action_relay_open.triggered.connect(self.open_all_relays)

        q_action_relay_close = QAction(QIcon(":/close.ico"), "ALL-&Disabled", self)
        q_action_relay_close.setShortcut("Ctrl+A")
        help_text = "Disable all relays"
        q_action_relay_close.setToolTip(help_text)
        q_action_relay_close.setStatusTip(help_text)
        q_action_relay_close.setCheckable(True)
        q_action_relay_close.triggered.connect(self.close_all_relays)

        relay_action_group = QActionGroup(self)
        relay_action_group.addAction(q_action_relay_open)
        relay_action_group.addAction(q_action_relay_close)
        q_action_relay_close.setChecked(True)
        self.main_tool_bar.addAction(q_action_relay_open)
        self.main_tool_bar.addAction(q_action_relay_close)

        self.working_relay_thread = []
        sec = 0.0
        for thread in RelayLib.relays:
            self.working_relay_thread.append([RenderRelayDataThread(), thread, sec])
            self.working_relay_thread[thread - 1][0].done.connect(self.render_done)
            self.working_relay_thread[thread - 1][0].error.connect(self.display_error)
        self.enable_all_relay_thread = EnableAllRelays()
        self.enable_all_relay_thread.done.connect(self.display_box_message)

    @Slot()
    def open_all_relays(self):

        self.enable_all_relay_thread.start()

        return

    @Slot()
    def close_all_relays(self):

        print "All relays shutdown"

    @Slot()
    def clear_ui(self):

        if not self.working_relay_thread[self.relays_combo_box.currentIndex()][0].isRunning() or \
                self.working_relay_thread[self.relays_combo_box.currentIndex()][0].isFinished():
            self.status_bar.clearMessage()
            self.relay_button.setDisabled(False)
            self.temp_double_spin_box.setDisabled(False)
            self.temp_dial.setDisabled(False)
            self.temp_double_spin_box.setValue(0.0)
            self.relay_button.setFocus()
        else:
            self.relay_button.setDisabled(True)
            self.temp_double_spin_box.setDisabled(True)
            self.temp_dial.setDisabled(True)
            self.relay_button.setFocus()
            self.temp_double_spin_box.setValue(
                self.working_relay_thread[self.relays_combo_box.currentIndex()][2])

    @Slot(str)
    def display_box_message(self, message=""):

        QMessageBox.warning(self, __app__, message)
        return

    @Slot(str)
    def display_error(self, message=""):

        QMessageBox.warning(self, __app__, message)
        self.relay_button.setDisabled(False)
        self.relays_combo_box.setDisabled(False)
        self.temp_double_spin_box.setDisabled(False)
        self.temp_dial.setDisabled(False)
        return

    @Slot(str, str)
    def render_done(self, relay, sec):
        self.relay_button.setDisabled(False)
        self.relays_combo_box.setDisabled(False)
        self.temp_double_spin_box.setDisabled(False)
        self.temp_dial.setDisabled(False)
        self.status_bar.showMessage("Operacion Finalizada [%s] en %s sec" % (relay, sec), 5000)

    @Slot()
    def toggle(self):
        """Method that turn on a relay during a specific seconds"""
        self.relay_button.setDisabled(True)
        self.temp_double_spin_box.setDisabled(True)
        self.temp_dial.setDisabled(True)
        self.working_relay_thread[self.relays_combo_box.currentIndex()][
            0].rel_num = self.relays_combo_box.currentIndex()
        self.working_relay_thread[self.relays_combo_box.currentIndex()][0].sec = self.temp_double_spin_box.value()
        self.working_relay_thread[self.relays_combo_box.currentIndex()][2] = self.temp_double_spin_box.value()
        self.working_relay_thread[self.relays_combo_box.currentIndex()][0].start()