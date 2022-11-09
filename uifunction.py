
from chatui import Ui_MainWindow
from PySide6 import QtWidgets, QtCore
from message_labels import send_msgbox, recv_msgbox
from net_ui_interface import *


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    #Signal Creation for thread's function in self.submit_button_click_handler()
    # to update UI by MainThread when message is received.
    signal_recv_msg = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendmsgList = []   
        self.recvmsgList = []
        self.recvQ = []
        self.recvQLock = threading.Lock()
        self.ip = None
        self.port = None
        self.recvthread = None
        self.disconnectedFlag = False

        #Connecting UI Widgets to their intended fuctions.

        # Page 1 Widgets
        self.submit_button.clicked.connect(self.submit_button_click_handler)
        self.name_edit.returnPressed.connect(
            self.username_label.setText(self.name_edit.text()))

        # Page 2 Widgets
        self.back_button.clicked.connect(self.back_button_click_handler)
        self.typemessage_edit.returnPressed.connect(
            self.send_button_click_handler)
        self.send_button.clicked.connect(self.send_button_click_handler)
        #Signal Function
        self.signal_recv_msg.connect(lambda: self.display_recvmsg())

    # Page 1 widget functions

    def submit_button_click_handler(self):
        name = self.name_edit.text()
        self.username_label.setText(name)
        self.getserveraddr()
        if connect_client_socket((self.ip, self.port), name):
            self.result_edit.setText("Connection Successful")
            self.stackedWidget.setCurrentIndex(1)
            self.disconnectedFlag = False
            self.recvthread = threading.Thread(target=self.getmsg, daemon=True)
            self.recvthread.start()
        else:
            self.result_edit.setText("Connection Failed.")
        self.username_label.setText(f"{name} on {self.ip}")

    def getserveraddr(self):
        addr = self.serveraddr_edit.text().split(':')
        self.ip = addr[0]
        try:
            self.port = int(addr[1])
        except:
            print("No port")
        print(f"{self.ip}:{self.port}")

    # Page 2 widget functions

    def widget_delete(self, widget):
        # here you will delete your widget
        parent_layout = widget.parent().layout()
        # remove the widget from its parent layout
        parent_layout.removeWidget(self)
        widget.deleteLater()  # lets Qt knows it needs to delete this widget from the GUI
        del widget

    def back_button_click_handler(self):
        disconnect()
        self.disconnectedFlag = True
        self.clrmessages()
        self.stackedWidget.setCurrentIndex(0)

    def clrmessages(self):
        for msg_box in self.sendmsgList:
            self.widget_delete(msg_box.sendmsg_label)
        for msg_box in self.recvmsgList:
            self.widget_delete(msg_box.recvmsg_label)
        self.sendmsgList = []
        self.recvmsgList = []

    def send_button_click_handler(self):
        msg = self.typemessage_edit.text()
        if msg == "" or msg.isspace():
            return
        send_to_server(msg)
        self.typemessage_edit.setText("")
        self.display_sendmsg(msg)
        self.moveScrollArea()

    def getmsg(self):  # Network dependent function
        while self.disconnectedFlag == False:
            temp = return_msg()
            if temp == "" or temp.isspace():
                continue
            self.recvQLock.acquire()
            self.recvQ.append(temp)
            self.recvQLock.release()
            self.signal_recv_msg.emit()
            print(f"recv in getmsg: {temp}")
        print("thead exiting")

    def display_sendmsg(self, msg):
        self.sendmsgList.append(send_msgbox(self.scrollAreaWidgetContents))
        self.sendmsgList[-1].sendmsg_label.setText(msg)
        self.gridLayout_10.addWidget(self.sendmsgList[-1].sendmsg_label)

        print(f"send: {msg}")

    def display_recvmsg(self):
        while self.recvQ != []:
            self.recvmsgList.append(recv_msgbox(self.scrollAreaWidgetContents))
            self.recvQLock.acquire()
            self.recvmsgList[-1].recvmsg_label.setText(self.recvQ[0])
            self.recvQ.pop(0)
            self.recvQLock.release()
            self.gridLayout_10.addWidget(self.recvmsgList[-1].recvmsg_label)
            self.moveScrollArea()
            print(f"recv: {recvQ}")

    def moveScrollArea(self):
        self.scrollArea.verticalScrollBar().setValue(
            self.scrollArea.verticalScrollBar().maximum())
        print(self.scrollArea.verticalScrollBar().maximum())
        print(self.scrollArea.verticalScrollBar().maximumHeight())
