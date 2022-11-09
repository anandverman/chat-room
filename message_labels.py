from PySide6 import QtWidgets, QtCore


class send_msgbox:
    def __init__(self, parentWidget):
        self.scrollAreaWidgetContents = parentWidget
        self.sendmsg_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sendmsg_label.sizePolicy().hasHeightForWidth())
        self.sendmsg_label.setSizePolicy(sizePolicy)
        self.sendmsg_label.setMinimumSize(QtCore.QSize(0, 60))
        self.sendmsg_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                        QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.sendmsg_label.setWordWrap(True)
        self.sendmsg_label.setObjectName("sendmsg_label")


class recv_msgbox:
    def __init__(self, parentWidget):
        self.scrollAreaWidgetContents = parentWidget
        self.recvmsg_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.recvmsg_label.sizePolicy().hasHeightForWidth())
        self.recvmsg_label.setSizePolicy(sizePolicy)
        self.recvmsg_label.setMinimumSize(QtCore.QSize(0, 60))
        self.recvmsg_label.setWordWrap(True)
        self.recvmsg_label.setObjectName("recvmsg_label")
