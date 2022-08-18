# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Changelog(QtWidgets.QDialog):
    def __init__(self, client_parent, changelog_msg):
        self.client_parent = client_parent
        self.changelog_msg = changelog_msg
        super().__init__(self.client_parent.mainwindow)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Changelog")
        self.resize(846, 682)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icon/sigma.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet(
            "background-image: url(:/back/back.png);\n" 'font: 9pt "Segoe UI";'
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changelog_groupBox = QtWidgets.QGroupBox(self)
        self.changelog_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    background: None;\n"
            "    border: 2px solid rgb(119, 133, 255);;\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex;\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "    subcontrol-origin: margin;\n"
            "    subcontrol-position: top center;\n"
            "    padding: 0px;\n"
            "    border-top: 1px solid rgb(119, 133, 255);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextEdit {\n"
            "    background: transparent;\n"
            "    color: white;\n"
            "}"
        )
        self.changelog_groupBox.setTitle("")
        self.changelog_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.changelog_groupBox.setFlat(False)
        self.changelog_groupBox.setObjectName("changelog_groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.changelog_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.changelog_textEdit = QtWidgets.QTextEdit(self.changelog_groupBox)
        self.changelog_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.changelog_textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.changelog_textEdit.setReadOnly(True)
        self.changelog_textEdit.setMarkdown(self.changelog_msg)
        self.changelog_textEdit.setObjectName("changelog_textEdit")
        self.verticalLayout_2.addWidget(self.changelog_textEdit)
        self.verticalLayout.addWidget(self.changelog_groupBox)
        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Changelog", "Changelog"))
