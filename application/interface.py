# -*- coding: utf-8 -*-

from . import resources_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1161, 662)
        MainWindow.setMinimumSize(QtCore.QSize(1161, 662))
        MainWindow.setMaximumSize(QtCore.QSize(1161, 662))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icon/sigma_bear.ico"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-image: url(:/back/back.png);\n" 'font: 9pt "Segoe UI";'
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1141, 641))
        self.tabWidget.setStyleSheet(
            "QTabWidget {\n"
            "    background-color: #14040B;\n"
            "}\n"
            "\n"
            "QTabBar::tab {\n"
            "    background-color: #14040B;\n"
            "    color: rgb(119, 133, 255);\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-bottom-color: rgb(119, 133, 255); \n"
            "    border-top-left-radius: 2px;\n"
            "    border-top-right-radius: 2px;\n"
            "    padding: 3px;\n"
            "}\n"
            "\n"
            "QTabBar::tab::disabled {\n"
            "    background-color: gray;\n"
            "    color: rgb(119, 133, 255);\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-bottom-color: rgb(119, 133, 255); \n"
            "    border-top-left-radius: 2px;\n"
            "    border-top-right-radius: 2px;\n"
            "    padding: 3px;\n"
            "}\n"
            "\n"
            "QTabWidget::tab-bar {\n"
            "    alignment: center;\n"
            "}\n"
            "\n"
            "QTabBar::tab:selected {\n"
            "    background-color: rgb(119, 133, 255);\n"
            "    border: 1px solid #14040B;\n"
            "    color: #14040B;\n"
            "}\n"
            "\n"
            "QTabWidget::pane {\n"
            "    border-top: 2px solid rgb(119, 133, 255);\n"
            "    position: absolute;\n"
            "    top: -0.5em;\n"
            "}"
        )
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.maindash_groupBox = QtWidgets.QGroupBox(self.tab_main)
        self.maindash_groupBox.setGeometry(QtCore.QRect(0, 10, 471, 601))
        self.maindash_groupBox.setStyleSheet(
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background-image: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.maindash_groupBox.setTitle("")
        self.maindash_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.maindash_groupBox.setFlat(False)
        self.maindash_groupBox.setObjectName("maindash_groupBox")
        self.mconsole_textBrowser = QtWidgets.QTextBrowser(
            self.maindash_groupBox
        )
        self.mconsole_textBrowser.setGeometry(QtCore.QRect(10, 495, 451, 91))
        self.mconsole_textBrowser.setObjectName("mconsole_textBrowser")
        self.mbackout_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.mbackout_label.setGeometry(QtCore.QRect(160, 470, 151, 21))
        self.mbackout_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mbackout_label.setObjectName("mbackout_label")
        self.validarLogin_pushButton = QtWidgets.QPushButton(
            self.maindash_groupBox
        )
        self.validarLogin_pushButton.setEnabled(True)
        self.validarLogin_pushButton.setGeometry(QtCore.QRect(10, 70, 451, 24))
        self.validarLogin_pushButton.setObjectName("validarLogin_pushButton")
        self.usuario_lineEdit = QtWidgets.QLineEdit(self.maindash_groupBox)
        self.usuario_lineEdit.setGeometry(QtCore.QRect(10, 30, 211, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush
        )
        self.usuario_lineEdit.setPalette(palette)
        self.usuario_lineEdit.setText("")
        self.usuario_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.usuario_lineEdit.setReadOnly(False)
        self.usuario_lineEdit.setObjectName("usuario_lineEdit")
        self.logo_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.logo_label.setGeometry(QtCore.QRect(10, 110, 451, 351))
        self.logo_label.setStyleSheet("background: none;")
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/other/sigmaicon_clean.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.maindash_groupBox)
        self.password_lineEdit.setGeometry(QtCore.QRect(250, 30, 211, 22))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 39, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush
        )
        brush = QtGui.QBrush(QtGui.QColor(255, 183, 122))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(
            QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush
        )
        self.password_lineEdit.setPalette(palette)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setReadOnly(False)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.sigma_version_label = QtWidgets.QLabel(self.maindash_groupBox)
        self.sigma_version_label.setGeometry(QtCore.QRect(73, 410, 313, 51))
        self.sigma_version_label.setStyleSheet(
            'font: 25pt "Segoe UI";\n' "color: white;"
        )
        self.sigma_version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sigma_version_label.setObjectName("sigma_version_label")
        self.informacion_groupBox = QtWidgets.QGroupBox(self.tab_main)
        self.informacion_groupBox.setGeometry(QtCore.QRect(480, 10, 661, 601))
        self.informacion_groupBox.setStyleSheet(
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
        self.informacion_groupBox.setTitle("")
        self.informacion_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.informacion_groupBox.setFlat(False)
        self.informacion_groupBox.setObjectName("informacion_groupBox")
        self.informacion_textEdit = QtWidgets.QTextEdit(
            self.informacion_groupBox
        )
        self.informacion_textEdit.setGeometry(QtCore.QRect(10, 10, 641, 581))
        self.informacion_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.informacion_textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.informacion_textEdit.setReadOnly(True)
        self.informacion_textEdit.setObjectName("informacion_textEdit")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_standard = QtWidgets.QWidget()
        self.tab_standard.setEnabled(True)
        self.tab_standard.setStyleSheet(
            "QWidget {\n" "    background-color: #14040B;\n" "}"
        )
        self.tab_standard.setObjectName("tab_standard")
        self.panelDNI_groupBox = QtWidgets.QGroupBox(self.tab_standard)
        self.panelDNI_groupBox.setGeometry(QtCore.QRect(30, 20, 601, 591))
        self.panelDNI_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.panelDNI_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelDNI_groupBox.setFlat(False)
        self.panelDNI_groupBox.setObjectName("panelDNI_groupBox")
        self.pddni_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pddni_output_lineEdit.setGeometry(QtCore.QRect(20, 60, 221, 22))
        self.pddni_output_lineEdit.setText("")
        self.pddni_output_lineEdit.setReadOnly(True)
        self.pddni_output_lineEdit.setObjectName("pddni_output_lineEdit")
        self.pddni_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pddni_label.setGeometry(QtCore.QRect(20, 40, 49, 16))
        self.pddni_label.setObjectName("pddni_label")
        self.pdapellido_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdapellido_output_lineEdit.setGeometry(
            QtCore.QRect(20, 120, 221, 22)
        )
        self.pdapellido_output_lineEdit.setText("")
        self.pdapellido_output_lineEdit.setReadOnly(True)
        self.pdapellido_output_lineEdit.setObjectName(
            "pdapellido_output_lineEdit"
        )
        self.pdappelido_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdappelido_label.setGeometry(QtCore.QRect(20, 100, 49, 16))
        self.pdappelido_label.setObjectName("pdappelido_label")
        self.pdnombres_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdnombres_output_lineEdit.setGeometry(
            QtCore.QRect(270, 120, 221, 22)
        )
        self.pdnombres_output_lineEdit.setText("")
        self.pdnombres_output_lineEdit.setReadOnly(True)
        self.pdnombres_output_lineEdit.setObjectName(
            "pdnombres_output_lineEdit"
        )
        self.pdnombres_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdnombres_label.setGeometry(QtCore.QRect(270, 100, 61, 16))
        self.pdnombres_label.setObjectName("pdnombres_label")
        self.pdcalle_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdcalle_output_lineEdit.setGeometry(
            QtCore.QRect(20, 190, 221, 22)
        )
        self.pdcalle_output_lineEdit.setText("")
        self.pdcalle_output_lineEdit.setReadOnly(True)
        self.pdcalle_output_lineEdit.setObjectName("pdcalle_output_lineEdit")
        self.pdcalle_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdcalle_label.setGeometry(QtCore.QRect(20, 170, 61, 16))
        self.pdcalle_label.setObjectName("pdcalle_label")
        self.pdseccion_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdseccion_output_lineEdit.setGeometry(
            QtCore.QRect(270, 190, 221, 22)
        )
        self.pdseccion_output_lineEdit.setText("")
        self.pdseccion_output_lineEdit.setReadOnly(True)
        self.pdseccion_output_lineEdit.setObjectName(
            "pdseccion_output_lineEdit"
        )
        self.pdseccion_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdseccion_label.setGeometry(QtCore.QRect(270, 170, 61, 16))
        self.pdseccion_label.setObjectName("pdseccion_label")
        self.pdcircuito_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdcircuito_output_lineEdit.setGeometry(
            QtCore.QRect(20, 260, 221, 22)
        )
        self.pdcircuito_output_lineEdit.setText("")
        self.pdcircuito_output_lineEdit.setReadOnly(True)
        self.pdcircuito_output_lineEdit.setObjectName(
            "pdcircuito_output_lineEdit"
        )
        self.pdcircuito_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdcircuito_label.setGeometry(QtCore.QRect(20, 240, 61, 16))
        self.pdcircuito_label.setObjectName("pdcircuito_label")
        self.pdlocalidad_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdlocalidad_output_lineEdit.setGeometry(
            QtCore.QRect(270, 260, 221, 22)
        )
        self.pdlocalidad_output_lineEdit.setText("")
        self.pdlocalidad_output_lineEdit.setReadOnly(True)
        self.pdlocalidad_output_lineEdit.setObjectName(
            "pdlocalidad_output_lineEdit"
        )
        self.pdlocalidad_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdlocalidad_label.setGeometry(QtCore.QRect(270, 240, 101, 16))
        self.pdlocalidad_label.setObjectName("pdlocalidad_label")
        self.pdtipodoc_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdtipodoc_output_lineEdit.setGeometry(
            QtCore.QRect(270, 60, 221, 22)
        )
        self.pdtipodoc_output_lineEdit.setText("")
        self.pdtipodoc_output_lineEdit.setReadOnly(True)
        self.pdtipodoc_output_lineEdit.setObjectName(
            "pdtipodoc_output_lineEdit"
        )
        self.pdtipodoc_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdtipodoc_label.setGeometry(QtCore.QRect(270, 40, 101, 16))
        self.pdtipodoc_label.setObjectName("pdtipodoc_label")
        self.pdprovincia_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdprovincia_label.setGeometry(QtCore.QRect(20, 300, 101, 16))
        self.pdprovincia_label.setObjectName("pdprovincia_label")
        self.pdprovincia_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdprovincia_output_lineEdit.setGeometry(
            QtCore.QRect(20, 320, 221, 22)
        )
        self.pdprovincia_output_lineEdit.setText("")
        self.pdprovincia_output_lineEdit.setReadOnly(True)
        self.pdprovincia_output_lineEdit.setObjectName(
            "pdprovincia_output_lineEdit"
        )
        self.pdcodigopost_output_lineEdit = QtWidgets.QLineEdit(
            self.panelDNI_groupBox
        )
        self.pdcodigopost_output_lineEdit.setGeometry(
            QtCore.QRect(270, 320, 221, 22)
        )
        self.pdcodigopost_output_lineEdit.setText("")
        self.pdcodigopost_output_lineEdit.setReadOnly(True)
        self.pdcodigopost_output_lineEdit.setObjectName(
            "pdcodigopost_output_lineEdit"
        )
        self.pdcodigopostal_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdcodigopostal_label.setGeometry(QtCore.QRect(270, 300, 101, 16))
        self.pdcodigopostal_label.setObjectName("pdcodigopostal_label")
        self.snumeros_tableWidget = QtWidgets.QTableWidget(
            self.panelDNI_groupBox
        )
        self.snumeros_tableWidget.setGeometry(QtCore.QRect(20, 390, 561, 181))
        self.snumeros_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  rgb(119, 133, 255);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: rgb(119, 133, 255);\n"
            "}"
        )
        self.snumeros_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.snumeros_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.snumeros_tableWidget.setObjectName("snumeros_tableWidget")
        self.snumeros_tableWidget.setColumnCount(7)
        self.snumeros_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.snumeros_tableWidget.setHorizontalHeaderItem(6, item)
        self.snumeros_tableWidget.horizontalHeader().setDefaultSectionSize(75)
        self.snumeros_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.pdnumeros_label = QtWidgets.QLabel(self.panelDNI_groupBox)
        self.pdnumeros_label.setGeometry(QtCore.QRect(20, 360, 161, 16))
        self.pdnumeros_label.setObjectName("pdnumeros_label")
        self.standardDashboard_groupBox = QtWidgets.QGroupBox(
            self.tab_standard
        )
        self.standardDashboard_groupBox.setGeometry(
            QtCore.QRect(650, 280, 471, 331)
        )
        self.standardDashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.standardDashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.standardDashboard_groupBox.setFlat(False)
        self.standardDashboard_groupBox.setObjectName(
            "standardDashboard_groupBox"
        )
        self.dnibuscar_label = QtWidgets.QLabel(
            self.standardDashboard_groupBox
        )
        self.dnibuscar_label.setGeometry(QtCore.QRect(30, 75, 141, 21))
        self.dnibuscar_label.setObjectName("dnibuscar_label")
        self.standarddni_lineEdit = QtWidgets.QLineEdit(
            self.standardDashboard_groupBox
        )
        self.standarddni_lineEdit.setGeometry(QtCore.QRect(30, 100, 141, 22))
        self.standarddni_lineEdit.setText("")
        self.standarddni_lineEdit.setReadOnly(False)
        self.standarddni_lineEdit.setObjectName("standarddni_lineEdit")
        self.sbuscardatos_pushButton = QtWidgets.QPushButton(
            self.standardDashboard_groupBox
        )
        self.sbuscardatos_pushButton.setEnabled(True)
        self.sbuscardatos_pushButton.setGeometry(
            QtCore.QRect(210, 100, 91, 24)
        )
        self.sbuscardatos_pushButton.setObjectName("sbuscardatos_pushButton")
        self.standardConsole_textBrowser = QtWidgets.QTextBrowser(
            self.standardDashboard_groupBox
        )
        self.standardConsole_textBrowser.setGeometry(
            QtCore.QRect(10, 190, 451, 131)
        )
        self.standardConsole_textBrowser.setObjectName(
            "standardConsole_textBrowser"
        )
        self.sdbackend_label = QtWidgets.QLabel(
            self.standardDashboard_groupBox
        )
        self.sdbackend_label.setGeometry(QtCore.QRect(10, 165, 161, 21))
        self.sdbackend_label.setObjectName("sdbackend_label")
        self.sbuscartelefono_pushButton = QtWidgets.QPushButton(
            self.standardDashboard_groupBox
        )
        self.sbuscartelefono_pushButton.setGeometry(
            QtCore.QRect(320, 100, 101, 24)
        )
        self.sbuscartelefono_pushButton.setObjectName(
            "sbuscartelefono_pushButton"
        )
        self.barbeta_label = QtWidgets.QLabel(self.tab_standard)
        self.barbeta_label.setGeometry(QtCore.QRect(760, 40, 241, 251))
        self.barbeta_label.setStyleSheet("background: none;")
        self.barbeta_label.setText("")
        self.barbeta_label.setPixmap(QtGui.QPixmap(":/people/bill-pay.png"))
        self.barbeta_label.setScaledContents(True)
        self.barbeta_label.setObjectName("barbeta_label")
        self.barbeta_label.raise_()
        self.panelDNI_groupBox.raise_()
        self.standardDashboard_groupBox.raise_()
        self.tabWidget.addTab(self.tab_standard, "")
        self.tab_medium = QtWidgets.QWidget()
        self.tab_medium.setStyleSheet(
            "QWidget {\n" "    background-color: #14040B;\n" "}"
        )
        self.tab_medium.setObjectName("tab_medium")
        self.panel_patentes_groupBox = QtWidgets.QGroupBox(self.tab_medium)
        self.panel_patentes_groupBox.setGeometry(
            QtCore.QRect(20, 20, 1101, 241)
        )
        self.panel_patentes_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "    padding: center;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.panel_patentes_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panel_patentes_groupBox.setFlat(False)
        self.panel_patentes_groupBox.setObjectName("panel_patentes_groupBox")
        self.patentes_tableWidget = QtWidgets.QTableWidget(
            self.panel_patentes_groupBox
        )
        self.patentes_tableWidget.setGeometry(QtCore.QRect(10, 30, 1081, 201))
        self.patentes_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  rgb(119, 133, 255);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: rgb(119, 133, 255);\n"
            "}"
        )
        self.patentes_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.patentes_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.patentes_tableWidget.setObjectName("patentes_tableWidget")
        self.patentes_tableWidget.setColumnCount(14)
        self.patentes_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.patentes_tableWidget.setHorizontalHeaderItem(13, item)
        self.patentes_tableWidget.horizontalHeader().setDefaultSectionSize(74)
        self.patentes_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.mdashboard_groupBox = QtWidgets.QGroupBox(self.tab_medium)
        self.mdashboard_groupBox.setGeometry(QtCore.QRect(750, 270, 371, 311))
        self.mdashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.mdashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mdashboard_groupBox.setFlat(False)
        self.mdashboard_groupBox.setObjectName("mdashboard_groupBox")
        self.patenteBuscar_label = QtWidgets.QLabel(self.mdashboard_groupBox)
        self.patenteBuscar_label.setGeometry(QtCore.QRect(30, 26, 141, 20))
        self.patenteBuscar_label.setObjectName("patenteBuscar_label")
        self.patenteBuscar_lineEdit = QtWidgets.QLineEdit(
            self.mdashboard_groupBox
        )
        self.patenteBuscar_lineEdit.setGeometry(QtCore.QRect(30, 50, 141, 22))
        self.patenteBuscar_lineEdit.setText("")
        self.patenteBuscar_lineEdit.setReadOnly(False)
        self.patenteBuscar_lineEdit.setObjectName("patenteBuscar_lineEdit")
        self.buscarPatente_pushButton = QtWidgets.QPushButton(
            self.mdashboard_groupBox
        )
        self.buscarPatente_pushButton.setGeometry(
            QtCore.QRect(210, 50, 121, 24)
        )
        self.buscarPatente_pushButton.setObjectName("buscarPatente_pushButton")
        self.mconsoleback_textBrowser = QtWidgets.QTextBrowser(
            self.mdashboard_groupBox
        )
        self.mconsoleback_textBrowser.setGeometry(
            QtCore.QRect(10, 170, 351, 131)
        )
        self.mconsoleback_textBrowser.setObjectName("mconsoleback_textBrowser")
        self.mbackoutput_label = QtWidgets.QLabel(self.mdashboard_groupBox)
        self.mbackoutput_label.setGeometry(QtCore.QRect(10, 145, 161, 21))
        self.mbackoutput_label.setObjectName("mbackoutput_label")
        self.mdnibuscar_label = QtWidgets.QLabel(self.mdashboard_groupBox)
        self.mdnibuscar_label.setGeometry(QtCore.QRect(30, 85, 141, 21))
        self.mdnibuscar_label.setObjectName("mdnibuscar_label")
        self.mdnibuscar_lineEdit = QtWidgets.QLineEdit(
            self.mdashboard_groupBox
        )
        self.mdnibuscar_lineEdit.setGeometry(QtCore.QRect(30, 110, 141, 22))
        self.mdnibuscar_lineEdit.setText("")
        self.mdnibuscar_lineEdit.setReadOnly(False)
        self.mdnibuscar_lineEdit.setObjectName("mdnibuscar_lineEdit")
        self.buscarPatentDNI_pushButton = QtWidgets.QPushButton(
            self.mdashboard_groupBox
        )
        self.buscarPatentDNI_pushButton.setGeometry(
            QtCore.QRect(210, 110, 121, 24)
        )
        self.buscarPatentDNI_pushButton.setObjectName(
            "buscarPatentDNI_pushButton"
        )
        self.mujer_label = QtWidgets.QLabel(self.tab_medium)
        self.mujer_label.setGeometry(QtCore.QRect(0, 310, 321, 321))
        self.mujer_label.setStyleSheet("background: none;")
        self.mujer_label.setText("")
        self.mujer_label.setPixmap(
            QtGui.QPixmap(":/people/laptop-poses_2.png")
        )
        self.mujer_label.setScaledContents(True)
        self.mujer_label.setObjectName("mujer_label")
        self.mdatabreach_groupBox = QtWidgets.QGroupBox(self.tab_medium)
        self.mdatabreach_groupBox.setGeometry(QtCore.QRect(340, 270, 391, 311))
        self.mdatabreach_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.mdatabreach_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.mdatabreach_groupBox.setFlat(False)
        self.mdatabreach_groupBox.setObjectName("mdatabreach_groupBox")
        self.querybreach_label = QtWidgets.QLabel(self.mdatabreach_groupBox)
        self.querybreach_label.setGeometry(QtCore.QRect(20, 26, 71, 20))
        self.querybreach_label.setObjectName("querybreach_label")
        self.queryBreach_lineEdit = QtWidgets.QLineEdit(
            self.mdatabreach_groupBox
        )
        self.queryBreach_lineEdit.setGeometry(QtCore.QRect(20, 50, 201, 22))
        self.queryBreach_lineEdit.setText("")
        self.queryBreach_lineEdit.setReadOnly(False)
        self.queryBreach_lineEdit.setObjectName("queryBreach_lineEdit")
        self.buscarLeaks_pushButton = QtWidgets.QPushButton(
            self.mdatabreach_groupBox
        )
        self.buscarLeaks_pushButton.setGeometry(QtCore.QRect(240, 50, 131, 24))
        self.buscarLeaks_pushButton.setObjectName("buscarLeaks_pushButton")
        self.dataBreachResults_tableWidget = QtWidgets.QTableWidget(
            self.mdatabreach_groupBox
        )
        self.dataBreachResults_tableWidget.setGeometry(
            QtCore.QRect(20, 90, 351, 201)
        )
        self.dataBreachResults_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  rgb(119, 133, 255);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: rgb(119, 133, 255);\n"
            "}"
        )
        self.dataBreachResults_tableWidget.setFrameShape(
            QtWidgets.QFrame.NoFrame
        )
        self.dataBreachResults_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.dataBreachResults_tableWidget.setObjectName(
            "dataBreachResults_tableWidget"
        )
        self.dataBreachResults_tableWidget.setColumnCount(2)
        self.dataBreachResults_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.dataBreachResults_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dataBreachResults_tableWidget.setHorizontalHeaderItem(1, item)
        self.dataBreachResults_tableWidget.horizontalHeader().setDefaultSectionSize(
            155
        )
        self.dataBreachResults_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.tabWidget.addTab(self.tab_medium, "")
        self.tab_profesional = QtWidgets.QWidget()
        self.tab_profesional.setStyleSheet(
            "QWidget {\n" "    background-color: #14040B;\n" "}"
        )
        self.tab_profesional.setObjectName("tab_profesional")
        self.prodashboard_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.prodashboard_groupBox.setGeometry(QtCore.QRect(0, 280, 371, 311))
        self.prodashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QComboBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}"
        )
        self.prodashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.prodashboard_groupBox.setFlat(False)
        self.prodashboard_groupBox.setObjectName("prodashboard_groupBox")
        self.pronumbusc_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.pronumbusc_label.setGeometry(QtCore.QRect(30, 25, 141, 21))
        self.pronumbusc_label.setObjectName("pronumbusc_label")
        self.proNumeroBuscar_lineEdit = QtWidgets.QLineEdit(
            self.prodashboard_groupBox
        )
        self.proNumeroBuscar_lineEdit.setGeometry(
            QtCore.QRect(30, 50, 141, 22)
        )
        self.proNumeroBuscar_lineEdit.setText("")
        self.proNumeroBuscar_lineEdit.setReadOnly(False)
        self.proNumeroBuscar_lineEdit.setObjectName("proNumeroBuscar_lineEdit")
        self.proBuscarNum_pushButton = QtWidgets.QPushButton(
            self.prodashboard_groupBox
        )
        self.proBuscarNum_pushButton.setGeometry(
            QtCore.QRect(210, 50, 121, 24)
        )
        self.proBuscarNum_pushButton.setObjectName("proBuscarNum_pushButton")
        self.proConsole_textBrowser = QtWidgets.QTextBrowser(
            self.prodashboard_groupBox
        )
        self.proConsole_textBrowser.setGeometry(QtCore.QRect(10, 220, 351, 81))
        self.proConsole_textBrowser.setObjectName("proConsole_textBrowser")
        self.probackend_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.probackend_label.setGeometry(QtCore.QRect(10, 190, 171, 21))
        self.probackend_label.setObjectName("probackend_label")
        self.dnibuscarpro_label = QtWidgets.QLabel(self.prodashboard_groupBox)
        self.dnibuscarpro_label.setGeometry(QtCore.QRect(30, 86, 141, 20))
        self.dnibuscarpro_label.setObjectName("dnibuscarpro_label")
        self.proDniBuscar_lineEdit = QtWidgets.QLineEdit(
            self.prodashboard_groupBox
        )
        self.proDniBuscar_lineEdit.setGeometry(QtCore.QRect(30, 110, 141, 22))
        self.proDniBuscar_lineEdit.setText("")
        self.proDniBuscar_lineEdit.setReadOnly(False)
        self.proDniBuscar_lineEdit.setObjectName("proDniBuscar_lineEdit")
        self.proBuscarDni_pushButton = QtWidgets.QPushButton(
            self.prodashboard_groupBox
        )
        self.proBuscarDni_pushButton.setGeometry(
            QtCore.QRect(30, 150, 301, 24)
        )
        self.proBuscarDni_pushButton.setObjectName("proBuscarDni_pushButton")
        self.proGenero_comboBox = QtWidgets.QComboBox(
            self.prodashboard_groupBox
        )
        self.proGenero_comboBox.setGeometry(QtCore.QRect(210, 110, 121, 22))
        self.proGenero_comboBox.setObjectName("proGenero_comboBox")
        self.proGenero_comboBox.addItem("")
        self.proGenero_comboBox.addItem("")
        self.dnibuscarpro_label_2 = QtWidgets.QLabel(
            self.prodashboard_groupBox
        )
        self.dnibuscarpro_label_2.setGeometry(QtCore.QRect(210, 86, 121, 20))
        self.dnibuscarpro_label_2.setObjectName("dnibuscarpro_label_2")
        self.promovistar_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.promovistar_groupBox.setGeometry(QtCore.QRect(390, 480, 731, 111))
        self.promovistar_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.promovistar_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.promovistar_groupBox.setFlat(False)
        self.promovistar_groupBox.setObjectName("promovistar_groupBox")
        self.pronum_output_lineEdit = QtWidgets.QLineEdit(
            self.promovistar_groupBox
        )
        self.pronum_output_lineEdit.setGeometry(QtCore.QRect(20, 70, 181, 22))
        self.pronum_output_lineEdit.setText("")
        self.pronum_output_lineEdit.setReadOnly(True)
        self.pronum_output_lineEdit.setObjectName("pronum_output_lineEdit")
        self.pronumero_label = QtWidgets.QLabel(self.promovistar_groupBox)
        self.pronumero_label.setGeometry(QtCore.QRect(20, 50, 91, 16))
        self.pronumero_label.setObjectName("pronumero_label")
        self.proEmail_label = QtWidgets.QLabel(self.promovistar_groupBox)
        self.proEmail_label.setGeometry(QtCore.QRect(220, 50, 81, 16))
        self.proEmail_label.setObjectName("proEmail_label")
        self.proemail_output_lineEdit = QtWidgets.QLineEdit(
            self.promovistar_groupBox
        )
        self.proemail_output_lineEdit.setGeometry(
            QtCore.QRect(220, 70, 201, 22)
        )
        self.proemail_output_lineEdit.setText("")
        self.proemail_output_lineEdit.setReadOnly(True)
        self.proemail_output_lineEdit.setObjectName("proemail_output_lineEdit")
        self.proBuscarEmail_pushButton = QtWidgets.QPushButton(
            self.promovistar_groupBox
        )
        self.proBuscarEmail_pushButton.setEnabled(True)
        self.proBuscarEmail_pushButton.setGeometry(
            QtCore.QRect(620, 70, 91, 24)
        )
        self.proBuscarEmail_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.proBuscarEmail_pushButton.setObjectName(
            "proBuscarEmail_pushButton"
        )
        self.pronum_buscar_lineEdit = QtWidgets.QLineEdit(
            self.promovistar_groupBox
        )
        self.pronum_buscar_lineEdit.setGeometry(QtCore.QRect(440, 70, 171, 22))
        self.pronum_buscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.pronum_buscar_lineEdit.setText("")
        self.pronum_buscar_lineEdit.setReadOnly(False)
        self.pronum_buscar_lineEdit.setObjectName("pronum_buscar_lineEdit")
        self.pronumeroABuscar_label = QtWidgets.QLabel(
            self.promovistar_groupBox
        )
        self.pronumeroABuscar_label.setGeometry(QtCore.QRect(440, 50, 121, 16))
        self.pronumeroABuscar_label.setObjectName("pronumeroABuscar_label")
        self.panelNumeros_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.panelNumeros_groupBox.setGeometry(QtCore.QRect(390, 10, 731, 201))
        self.panelNumeros_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.panelNumeros_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelNumeros_groupBox.setFlat(False)
        self.panelNumeros_groupBox.setObjectName("panelNumeros_groupBox")
        self.proNumeros_tableWidget = QtWidgets.QTableWidget(
            self.panelNumeros_groupBox
        )
        self.proNumeros_tableWidget.setGeometry(QtCore.QRect(10, 30, 711, 161))
        self.proNumeros_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  rgb(119, 133, 255);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: rgb(119, 133, 255);\n"
            "}"
        )
        self.proNumeros_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.proNumeros_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.proNumeros_tableWidget.setObjectName("proNumeros_tableWidget")
        self.proNumeros_tableWidget.setColumnCount(8)
        self.proNumeros_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.proNumeros_tableWidget.setHorizontalHeaderItem(7, item)
        self.proNumeros_tableWidget.horizontalHeader().setDefaultSectionSize(
            84
        )
        self.proNumeros_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.proPersonas_groupBox = QtWidgets.QGroupBox(self.tab_profesional)
        self.proPersonas_groupBox.setGeometry(QtCore.QRect(390, 220, 731, 251))
        self.proPersonas_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}"
        )
        self.proPersonas_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.proPersonas_groupBox.setFlat(False)
        self.proPersonas_groupBox.setObjectName("proPersonas_groupBox")
        self.proEmision_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proEmision_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 111, 22)
        )
        self.proEmision_output_lineEdit.setText("")
        self.proEmision_output_lineEdit.setReadOnly(True)
        self.proEmision_output_lineEdit.setObjectName(
            "proEmision_output_lineEdit"
        )
        self.emision_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.emision_label.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.emision_label.setObjectName("emision_label")
        self.nroDocumento_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.nroDocumento_label.setGeometry(QtCore.QRect(150, 40, 91, 16))
        self.nroDocumento_label.setObjectName("nroDocumento_label")
        self.proNroDoc_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proNroDoc_output_lineEdit.setGeometry(
            QtCore.QRect(150, 60, 111, 22)
        )
        self.proNroDoc_output_lineEdit.setText("")
        self.proNroDoc_output_lineEdit.setReadOnly(True)
        self.proNroDoc_output_lineEdit.setObjectName(
            "proNroDoc_output_lineEdit"
        )
        self.proApellido_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proApellido_output_lineEdit.setGeometry(
            QtCore.QRect(280, 60, 111, 22)
        )
        self.proApellido_output_lineEdit.setText("")
        self.proApellido_output_lineEdit.setReadOnly(True)
        self.proApellido_output_lineEdit.setObjectName(
            "proApellido_output_lineEdit"
        )
        self.proApellido_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.proApellido_label.setGeometry(QtCore.QRect(280, 40, 91, 16))
        self.proApellido_label.setObjectName("proApellido_label")
        self.proNombre_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.proNombre_label.setGeometry(QtCore.QRect(410, 40, 91, 16))
        self.proNombre_label.setObjectName("proNombre_label")
        self.proNombre_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proNombre_output_lineEdit.setGeometry(
            QtCore.QRect(410, 60, 161, 22)
        )
        self.proNombre_output_lineEdit.setText("")
        self.proNombre_output_lineEdit.setReadOnly(True)
        self.proNombre_output_lineEdit.setObjectName(
            "proNombre_output_lineEdit"
        )
        self.cuil_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.cuil_label.setGeometry(QtCore.QRect(590, 40, 61, 16))
        self.cuil_label.setObjectName("cuil_label")
        self.proCUIL_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCUIL_output_lineEdit.setGeometry(
            QtCore.QRect(590, 60, 111, 22)
        )
        self.proCUIL_output_lineEdit.setText("")
        self.proCUIL_output_lineEdit.setReadOnly(True)
        self.proCUIL_output_lineEdit.setObjectName("proCUIL_output_lineEdit")
        self.barrio_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.barrio_label.setGeometry(QtCore.QRect(20, 90, 101, 16))
        self.barrio_label.setObjectName("barrio_label")
        self.proBarrio_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proBarrio_output_lineEdit.setGeometry(
            QtCore.QRect(20, 110, 111, 22)
        )
        self.proBarrio_output_lineEdit.setText("")
        self.proBarrio_output_lineEdit.setReadOnly(True)
        self.proBarrio_output_lineEdit.setObjectName(
            "proBarrio_output_lineEdit"
        )
        self.calle_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.calle_label.setGeometry(QtCore.QRect(150, 90, 71, 16))
        self.calle_label.setObjectName("calle_label")
        self.proCalle_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCalle_output_lineEdit.setGeometry(
            QtCore.QRect(150, 110, 111, 22)
        )
        self.proCalle_output_lineEdit.setText("")
        self.proCalle_output_lineEdit.setReadOnly(True)
        self.proCalle_output_lineEdit.setObjectName("proCalle_output_lineEdit")
        self.altura_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.altura_label.setGeometry(QtCore.QRect(280, 90, 81, 16))
        self.altura_label.setObjectName("altura_label")
        self.proAltura_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proAltura_output_lineEdit.setGeometry(
            QtCore.QRect(280, 110, 111, 22)
        )
        self.proAltura_output_lineEdit.setText("")
        self.proAltura_output_lineEdit.setReadOnly(True)
        self.proAltura_output_lineEdit.setObjectName(
            "proAltura_output_lineEdit"
        )
        self.piso_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.piso_label.setGeometry(QtCore.QRect(590, 90, 101, 16))
        self.piso_label.setObjectName("piso_label")
        self.proDepartamento_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proDepartamento_output_lineEdit.setGeometry(
            QtCore.QRect(410, 110, 161, 22)
        )
        self.proDepartamento_output_lineEdit.setText("")
        self.proDepartamento_output_lineEdit.setReadOnly(True)
        self.proDepartamento_output_lineEdit.setObjectName(
            "proDepartamento_output_lineEdit"
        )
        self.departamento_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.departamento_label.setGeometry(QtCore.QRect(410, 90, 111, 16))
        self.departamento_label.setObjectName("departamento_label")
        self.proPiso_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proPiso_output_lineEdit.setGeometry(
            QtCore.QRect(590, 110, 111, 22)
        )
        self.proPiso_output_lineEdit.setText("")
        self.proPiso_output_lineEdit.setReadOnly(True)
        self.proPiso_output_lineEdit.setObjectName("proPiso_output_lineEdit")
        self.provincia_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.provincia_label.setGeometry(QtCore.QRect(410, 140, 101, 16))
        self.provincia_label.setObjectName("provincia_label")
        self.proProvincia_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proProvincia_output_lineEdit.setGeometry(
            QtCore.QRect(410, 160, 161, 22)
        )
        self.proProvincia_output_lineEdit.setText("")
        self.proProvincia_output_lineEdit.setReadOnly(True)
        self.proProvincia_output_lineEdit.setObjectName(
            "proProvincia_output_lineEdit"
        )
        self.pais_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.pais_label.setGeometry(QtCore.QRect(590, 140, 81, 16))
        self.pais_label.setObjectName("pais_label")
        self.proPais_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proPais_output_lineEdit.setGeometry(
            QtCore.QRect(590, 160, 111, 22)
        )
        self.proPais_output_lineEdit.setText("")
        self.proPais_output_lineEdit.setReadOnly(True)
        self.proPais_output_lineEdit.setObjectName("proPais_output_lineEdit")
        self.monoblock_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.monoblock_label.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.monoblock_label.setObjectName("monoblock_label")
        self.proMonoblock_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proMonoblock_output_lineEdit.setGeometry(
            QtCore.QRect(20, 160, 111, 22)
        )
        self.proMonoblock_output_lineEdit.setText("")
        self.proMonoblock_output_lineEdit.setReadOnly(True)
        self.proMonoblock_output_lineEdit.setObjectName(
            "proMonoblock_output_lineEdit"
        )
        self.ciudad_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.ciudad_label.setGeometry(QtCore.QRect(150, 140, 101, 16))
        self.ciudad_label.setObjectName("ciudad_label")
        self.proCiudad_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proCiudad_output_lineEdit.setGeometry(
            QtCore.QRect(150, 160, 111, 22)
        )
        self.proCiudad_output_lineEdit.setText("")
        self.proCiudad_output_lineEdit.setReadOnly(True)
        self.proCiudad_output_lineEdit.setObjectName(
            "proCiudad_output_lineEdit"
        )
        self.municipio_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.municipio_label.setGeometry(QtCore.QRect(280, 140, 101, 16))
        self.municipio_label.setObjectName("municipio_label")
        self.proMunicipio_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proMunicipio_output_lineEdit.setGeometry(
            QtCore.QRect(280, 160, 111, 22)
        )
        self.proMunicipio_output_lineEdit.setText("")
        self.proMunicipio_output_lineEdit.setReadOnly(True)
        self.proMunicipio_output_lineEdit.setObjectName(
            "proMunicipio_output_lineEdit"
        )
        self.fechanac_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.fechanac_label.setGeometry(QtCore.QRect(20, 190, 111, 16))
        self.fechanac_label.setObjectName("fechanac_label")
        self.proFechaNacimiento_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proFechaNacimiento_output_lineEdit.setGeometry(
            QtCore.QRect(20, 210, 111, 22)
        )
        self.proFechaNacimiento_output_lineEdit.setText("")
        self.proFechaNacimiento_output_lineEdit.setReadOnly(True)
        self.proFechaNacimiento_output_lineEdit.setObjectName(
            "proFechaNacimiento_output_lineEdit"
        )
        self.proFallecido_output_lineEdit = QtWidgets.QLineEdit(
            self.proPersonas_groupBox
        )
        self.proFallecido_output_lineEdit.setGeometry(
            QtCore.QRect(150, 210, 111, 22)
        )
        self.proFallecido_output_lineEdit.setText("")
        self.proFallecido_output_lineEdit.setReadOnly(True)
        self.proFallecido_output_lineEdit.setObjectName(
            "proFallecido_output_lineEdit"
        )
        self.fallecido_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.fallecido_label.setGeometry(QtCore.QRect(150, 190, 111, 16))
        self.fallecido_label.setObjectName("fallecido_label")
        self.obraSocial_output_comboBox = QtWidgets.QComboBox(
            self.proPersonas_groupBox
        )
        self.obraSocial_output_comboBox.setGeometry(
            QtCore.QRect(280, 210, 421, 22)
        )
        self.obraSocial_output_comboBox.setObjectName(
            "obraSocial_output_comboBox"
        )
        self.obrassociales_label = QtWidgets.QLabel(self.proPersonas_groupBox)
        self.obrassociales_label.setGeometry(QtCore.QRect(280, 190, 121, 16))
        self.obrassociales_label.setObjectName("obrassociales_label")
        self.mujerlaptop_label = QtWidgets.QLabel(self.tab_profesional)
        self.mujerlaptop_label.setGeometry(QtCore.QRect(50, 30, 281, 261))
        self.mujerlaptop_label.setStyleSheet("background: none;")
        self.mujerlaptop_label.setText("")
        self.mujerlaptop_label.setPixmap(
            QtGui.QPixmap(":/people/laptop-poses.png")
        )
        self.mujerlaptop_label.setScaledContents(True)
        self.mujerlaptop_label.setObjectName("mujerlaptop_label")
        self.mujerlaptop_label.raise_()
        self.prodashboard_groupBox.raise_()
        self.promovistar_groupBox.raise_()
        self.panelNumeros_groupBox.raise_()
        self.proPersonas_groupBox.raise_()
        self.tabWidget.addTab(self.tab_profesional, "")
        self.tab_profesional_2 = QtWidgets.QWidget()
        self.tab_profesional_2.setObjectName("tab_profesional_2")
        self.pro2dashboard_groupBox = QtWidgets.QGroupBox(
            self.tab_profesional_2
        )
        self.pro2dashboard_groupBox.setGeometry(QtCore.QRect(0, 280, 371, 311))
        self.pro2dashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QComboBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QSpinBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QSpinBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.pro2dashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pro2dashboard_groupBox.setFlat(False)
        self.pro2dashboard_groupBox.setObjectName("pro2dashboard_groupBox")
        self.proNombrebusc_label = QtWidgets.QLabel(
            self.pro2dashboard_groupBox
        )
        self.proNombrebusc_label.setGeometry(QtCore.QRect(30, 25, 141, 21))
        self.proNombrebusc_label.setObjectName("proNombrebusc_label")
        self.proNombreBuscar_lineEdit = QtWidgets.QLineEdit(
            self.pro2dashboard_groupBox
        )
        self.proNombreBuscar_lineEdit.setGeometry(
            QtCore.QRect(30, 50, 141, 22)
        )
        self.proNombreBuscar_lineEdit.setText("")
        self.proNombreBuscar_lineEdit.setReadOnly(False)
        self.proNombreBuscar_lineEdit.setObjectName("proNombreBuscar_lineEdit")
        self.proBuscarNombre_pushButton = QtWidgets.QPushButton(
            self.pro2dashboard_groupBox
        )
        self.proBuscarNombre_pushButton.setGeometry(
            QtCore.QRect(30, 160, 301, 24)
        )
        self.proBuscarNombre_pushButton.setObjectName(
            "proBuscarNombre_pushButton"
        )
        self.pro2Console_textBrowser = QtWidgets.QTextBrowser(
            self.pro2dashboard_groupBox
        )
        self.pro2Console_textBrowser.setGeometry(
            QtCore.QRect(10, 230, 351, 71)
        )
        self.pro2Console_textBrowser.setObjectName("pro2Console_textBrowser")
        self.pro2backend_label = QtWidgets.QLabel(self.pro2dashboard_groupBox)
        self.pro2backend_label.setGeometry(QtCore.QRect(10, 200, 181, 21))
        self.pro2backend_label.setObjectName("pro2backend_label")
        self.proProvinciabusc_label = QtWidgets.QLabel(
            self.pro2dashboard_groupBox
        )
        self.proProvinciabusc_label.setGeometry(QtCore.QRect(190, 25, 151, 21))
        self.proProvinciabusc_label.setObjectName("proProvinciabusc_label")
        self.proLocalidadbusc_label = QtWidgets.QLabel(
            self.pro2dashboard_groupBox
        )
        self.proLocalidadbusc_label.setGeometry(QtCore.QRect(30, 90, 141, 21))
        self.proLocalidadbusc_label.setObjectName("proLocalidadbusc_label")
        self.proLocalidadBuscar_lineEdit = QtWidgets.QLineEdit(
            self.pro2dashboard_groupBox
        )
        self.proLocalidadBuscar_lineEdit.setGeometry(
            QtCore.QRect(30, 120, 141, 22)
        )
        self.proLocalidadBuscar_lineEdit.setText("")
        self.proLocalidadBuscar_lineEdit.setReadOnly(False)
        self.proLocalidadBuscar_lineEdit.setObjectName(
            "proLocalidadBuscar_lineEdit"
        )
        self.proProvincia_comboBox = QtWidgets.QComboBox(
            self.pro2dashboard_groupBox
        )
        self.proProvincia_comboBox.setGeometry(QtCore.QRect(190, 50, 141, 22))
        self.proProvincia_comboBox.setObjectName("proProvincia_comboBox")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.setItemText(0, "")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proProvincia_comboBox.addItem("")
        self.proEdadMin_spinBox = QtWidgets.QSpinBox(
            self.pro2dashboard_groupBox
        )
        self.proEdadMin_spinBox.setGeometry(QtCore.QRect(190, 120, 61, 22))
        self.proEdadMin_spinBox.setMinimum(0)
        self.proEdadMin_spinBox.setMaximum(99)
        self.proEdadMin_spinBox.setProperty("value", 0)
        self.proEdadMin_spinBox.setObjectName("proEdadMin_spinBox")
        self.proEdadbusc_label = QtWidgets.QLabel(self.pro2dashboard_groupBox)
        self.proEdadbusc_label.setGeometry(QtCore.QRect(190, 90, 171, 21))
        self.proEdadbusc_label.setObjectName("proEdadbusc_label")
        self.proEdadMax_spinBox = QtWidgets.QSpinBox(
            self.pro2dashboard_groupBox
        )
        self.proEdadMax_spinBox.setGeometry(QtCore.QRect(270, 120, 61, 22))
        self.proEdadMax_spinBox.setMinimum(0)
        self.proEdadMax_spinBox.setMaximum(99)
        self.proEdadMax_spinBox.setProperty("value", 0)
        self.proEdadMax_spinBox.setObjectName("proEdadMax_spinBox")
        self.panelPersonas_groupBox = QtWidgets.QGroupBox(
            self.tab_profesional_2
        )
        self.panelPersonas_groupBox.setGeometry(
            QtCore.QRect(390, 10, 731, 271)
        )
        self.panelPersonas_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.panelPersonas_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelPersonas_groupBox.setFlat(False)
        self.panelPersonas_groupBox.setObjectName("panelPersonas_groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.panelPersonas_groupBox
        )
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.panelPersonas_groupBox)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 709, 246))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents
        )
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.panelNumeros_groupBox_3 = QtWidgets.QGroupBox(
            self.tab_profesional_2
        )
        self.panelNumeros_groupBox_3.setGeometry(
            QtCore.QRect(390, 290, 731, 301)
        )
        self.panelNumeros_groupBox_3.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.panelNumeros_groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.panelNumeros_groupBox_3.setFlat(False)
        self.panelNumeros_groupBox_3.setObjectName("panelNumeros_groupBox_3")
        self.proVecinos_tableWidget = QtWidgets.QTableWidget(
            self.panelNumeros_groupBox_3
        )
        self.proVecinos_tableWidget.setGeometry(QtCore.QRect(10, 80, 711, 211))
        self.proVecinos_tableWidget.setStyleSheet(
            "QTableWidget {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTableView QTableCornerButton::section  {\n"
            "    background:  rgb(119, 133, 255);\n"
            "}\n"
            "\n"
            "QHeaderView::section {\n"
            "    color: black;\n"
            "    background-color: rgb(119, 133, 255);\n"
            "}"
        )
        self.proVecinos_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.proVecinos_tableWidget.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded
        )
        self.proVecinos_tableWidget.setObjectName("proVecinos_tableWidget")
        self.proVecinos_tableWidget.setColumnCount(8)
        self.proVecinos_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.proVecinos_tableWidget.setHorizontalHeaderItem(7, item)
        self.proVecinos_tableWidget.horizontalHeader().setVisible(True)
        self.proVecinos_tableWidget.horizontalHeader().setCascadingSectionResizes(
            False
        )
        self.proVecinos_tableWidget.horizontalHeader().setDefaultSectionSize(
            82
        )
        self.proVecinos_tableWidget.horizontalHeader().setStretchLastSection(
            True
        )
        self.proVecinos_tableWidget.verticalHeader().setVisible(False)
        self.proVecinos_tableWidget.verticalHeader().setCascadingSectionResizes(
            False
        )
        self.proVecinos_tableWidget.verticalHeader().setStretchLastSection(
            False
        )
        self.proBuscarVecinos_pushButton = QtWidgets.QPushButton(
            self.panelNumeros_groupBox_3
        )
        self.proBuscarVecinos_pushButton.setGeometry(
            QtCore.QRect(510, 40, 141, 24)
        )
        self.proBuscarVecinos_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.proBuscarVecinos_pushButton.setObjectName(
            "proBuscarVecinos_pushButton"
        )
        self.proDireccionBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelNumeros_groupBox_3
        )
        self.proDireccionBuscar_lineEdit.setGeometry(
            QtCore.QRect(80, 40, 401, 22)
        )
        self.proDireccionBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.proDireccionBuscar_lineEdit.setText("")
        self.proDireccionBuscar_lineEdit.setReadOnly(False)
        self.proDireccionBuscar_lineEdit.setObjectName(
            "proDireccionBuscar_lineEdit"
        )
        self.direccionbuscarpro_label = QtWidgets.QLabel(
            self.panelNumeros_groupBox_3
        )
        self.direccionbuscarpro_label.setGeometry(
            QtCore.QRect(80, 20, 151, 21)
        )
        self.direccionbuscarpro_label.setObjectName("direccionbuscarpro_label")
        self.mujerlaptop_label_2 = QtWidgets.QLabel(self.tab_profesional_2)
        self.mujerlaptop_label_2.setGeometry(QtCore.QRect(50, 30, 281, 261))
        self.mujerlaptop_label_2.setStyleSheet("background: none;")
        self.mujerlaptop_label_2.setText("")
        self.mujerlaptop_label_2.setPixmap(
            QtGui.QPixmap(":/people/laptop-poses.png")
        )
        self.mujerlaptop_label_2.setScaledContents(True)
        self.mujerlaptop_label_2.setObjectName("mujerlaptop_label_2")
        self.mujerlaptop_label_2.raise_()
        self.pro2dashboard_groupBox.raise_()
        self.panelPersonas_groupBox.raise_()
        self.panelNumeros_groupBox_3.raise_()
        self.tabWidget.addTab(self.tab_profesional_2, "")
        self.tab_profesional_5 = QtWidgets.QWidget()
        self.tab_profesional_5.setObjectName("tab_profesional_5")
        self.pro3dashboard_groupBox = QtWidgets.QGroupBox(
            self.tab_profesional_5
        )
        self.pro3dashboard_groupBox.setGeometry(
            QtCore.QRect(30, 240, 521, 181)
        )
        self.pro3dashboard_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.pro3dashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pro3dashboard_groupBox.setFlat(False)
        self.pro3dashboard_groupBox.setObjectName("pro3dashboard_groupBox")
        self.pro3Console_textBrowser = QtWidgets.QTextBrowser(
            self.pro3dashboard_groupBox
        )
        self.pro3Console_textBrowser.setGeometry(
            QtCore.QRect(10, 50, 501, 121)
        )
        self.pro3Console_textBrowser.setObjectName("pro3Console_textBrowser")
        self.pro3backend_label = QtWidgets.QLabel(self.pro3dashboard_groupBox)
        self.pro3backend_label.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.pro3backend_label.setObjectName("pro3backend_label")
        self.p3panelcvu_groupBox = QtWidgets.QGroupBox(self.tab_profesional_5)
        self.p3panelcvu_groupBox.setGeometry(QtCore.QRect(570, 90, 521, 271))
        self.p3panelcvu_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.p3panelcvu_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p3panelcvu_groupBox.setFlat(False)
        self.p3panelcvu_groupBox.setObjectName("p3panelcvu_groupBox")
        self.p3titular_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3titular_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 221, 22)
        )
        self.p3titular_output_lineEdit.setText("")
        self.p3titular_output_lineEdit.setReadOnly(True)
        self.p3titular_output_lineEdit.setObjectName(
            "p3titular_output_lineEdit"
        )
        self.titular_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.titular_label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.titular_label.setObjectName("titular_label")
        self.p3banco_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3banco_output_lineEdit.setGeometry(
            QtCore.QRect(20, 120, 221, 22)
        )
        self.p3banco_output_lineEdit.setText("")
        self.p3banco_output_lineEdit.setReadOnly(True)
        self.p3banco_output_lineEdit.setObjectName("p3banco_output_lineEdit")
        self.banco_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.banco_label.setGeometry(QtCore.QRect(20, 100, 49, 16))
        self.banco_label.setObjectName("banco_label")
        self.p3cbucvu_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cbucvu_output_lineEdit.setGeometry(
            QtCore.QRect(20, 170, 471, 22)
        )
        self.p3cbucvu_output_lineEdit.setText("")
        self.p3cbucvu_output_lineEdit.setReadOnly(True)
        self.p3cbucvu_output_lineEdit.setObjectName("p3cbucvu_output_lineEdit")
        self.cbucvu_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cbucvu_label.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.cbucvu_label.setObjectName("cbucvu_label")
        self.p3cuit_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cuit_output_lineEdit.setGeometry(QtCore.QRect(270, 60, 221, 22))
        self.p3cuit_output_lineEdit.setText("")
        self.p3cuit_output_lineEdit.setReadOnly(True)
        self.p3cuit_output_lineEdit.setObjectName("p3cuit_output_lineEdit")
        self.cuit_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cuit_label.setGeometry(QtCore.QRect(270, 40, 51, 16))
        self.cuit_label.setObjectName("cuit_label")
        self.p3tipocuenta_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3tipocuenta_output_lineEdit.setGeometry(
            QtCore.QRect(270, 120, 221, 22)
        )
        self.p3tipocuenta_output_lineEdit.setText("")
        self.p3tipocuenta_output_lineEdit.setReadOnly(True)
        self.p3tipocuenta_output_lineEdit.setObjectName(
            "p3tipocuenta_output_lineEdit"
        )
        self.tipoCuenta_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.tipoCuenta_label.setGeometry(QtCore.QRect(270, 100, 81, 16))
        self.tipoCuenta_label.setObjectName("tipoCuenta_label")
        self.cbvucvubuscar_label = QtWidgets.QLabel(self.p3panelcvu_groupBox)
        self.cbvucvubuscar_label.setGeometry(QtCore.QRect(20, 210, 171, 16))
        self.cbvucvubuscar_label.setObjectName("cbvucvubuscar_label")
        self.p3buscarcvuTitular_pushButton = QtWidgets.QPushButton(
            self.p3panelcvu_groupBox
        )
        self.p3buscarcvuTitular_pushButton.setEnabled(True)
        self.p3buscarcvuTitular_pushButton.setGeometry(
            QtCore.QRect(350, 230, 141, 24)
        )
        self.p3buscarcvuTitular_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3buscarcvuTitular_pushButton.setObjectName(
            "p3buscarcvuTitular_pushButton"
        )
        self.p3cbvubuscar_lineEdit = QtWidgets.QLineEdit(
            self.p3panelcvu_groupBox
        )
        self.p3cbvubuscar_lineEdit.setGeometry(QtCore.QRect(20, 230, 301, 22))
        self.p3cbvubuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3cbvubuscar_lineEdit.setText("")
        self.p3cbvubuscar_lineEdit.setReadOnly(False)
        self.p3cbvubuscar_lineEdit.setObjectName("p3cbvubuscar_lineEdit")
        self.p3panelnumeor_groupBox = QtWidgets.QGroupBox(
            self.tab_profesional_5
        )
        self.p3panelnumeor_groupBox.setGeometry(
            QtCore.QRect(570, 370, 521, 221)
        )
        self.p3panelnumeor_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.p3panelnumeor_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.p3panelnumeor_groupBox.setFlat(False)
        self.p3panelnumeor_groupBox.setObjectName("p3panelnumeor_groupBox")
        self.p3nombres2_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3nombres2_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 221, 22)
        )
        self.p3nombres2_output_lineEdit.setText("")
        self.p3nombres2_output_lineEdit.setReadOnly(True)
        self.p3nombres2_output_lineEdit.setObjectName(
            "p3nombres2_output_lineEdit"
        )
        self.nombres_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.nombres_label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.nombres_label.setObjectName("nombres_label")
        self.p3email_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3email_output_lineEdit.setGeometry(
            QtCore.QRect(20, 120, 221, 22)
        )
        self.p3email_output_lineEdit.setText("")
        self.p3email_output_lineEdit.setReadOnly(True)
        self.p3email_output_lineEdit.setObjectName("p3email_output_lineEdit")
        self.email_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.email_label.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.email_label.setObjectName("email_label")
        self.p3numero_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3numero_output_lineEdit.setGeometry(
            QtCore.QRect(270, 120, 221, 22)
        )
        self.p3numero_output_lineEdit.setText("")
        self.p3numero_output_lineEdit.setReadOnly(True)
        self.p3numero_output_lineEdit.setObjectName("p3numero_output_lineEdit")
        self.numer_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.numer_label.setGeometry(QtCore.QRect(270, 100, 61, 16))
        self.numer_label.setObjectName("numer_label")
        self.p3apellidos2_output_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3apellidos2_output_lineEdit.setGeometry(
            QtCore.QRect(270, 60, 221, 22)
        )
        self.p3apellidos2_output_lineEdit.setText("")
        self.p3apellidos2_output_lineEdit.setReadOnly(True)
        self.p3apellidos2_output_lineEdit.setObjectName(
            "p3apellidos2_output_lineEdit"
        )
        self.apellido_label = QtWidgets.QLabel(self.p3panelnumeor_groupBox)
        self.apellido_label.setGeometry(QtCore.QRect(270, 40, 71, 16))
        self.apellido_label.setObjectName("apellido_label")
        self.numberoabuscar_label = QtWidgets.QLabel(
            self.p3panelnumeor_groupBox
        )
        self.numberoabuscar_label.setGeometry(QtCore.QRect(20, 160, 171, 16))
        self.numberoabuscar_label.setObjectName("numberoabuscar_label")
        self.p3numeroBuscar_lineEdit = QtWidgets.QLineEdit(
            self.p3panelnumeor_groupBox
        )
        self.p3numeroBuscar_lineEdit.setGeometry(
            QtCore.QRect(20, 180, 301, 22)
        )
        self.p3numeroBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3numeroBuscar_lineEdit.setText("")
        self.p3numeroBuscar_lineEdit.setReadOnly(False)
        self.p3numeroBuscar_lineEdit.setObjectName("p3numeroBuscar_lineEdit")
        self.p3buscarDato_pushButton = QtWidgets.QPushButton(
            self.p3panelnumeor_groupBox
        )
        self.p3buscarDato_pushButton.setEnabled(True)
        self.p3buscarDato_pushButton.setGeometry(
            QtCore.QRect(350, 180, 141, 24)
        )
        self.p3buscarDato_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3buscarDato_pushButton.setObjectName("p3buscarDato_pushButton")
        self.panelEmail_groupBox = QtWidgets.QGroupBox(self.tab_profesional_5)
        self.panelEmail_groupBox.setGeometry(QtCore.QRect(30, 430, 521, 161))
        self.panelEmail_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.panelEmail_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelEmail_groupBox.setFlat(False)
        self.panelEmail_groupBox.setObjectName("panelEmail_groupBox")
        self.p3nombres_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3nombres_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 221, 22)
        )
        self.p3nombres_output_lineEdit.setText("")
        self.p3nombres_output_lineEdit.setReadOnly(True)
        self.p3nombres_output_lineEdit.setObjectName(
            "p3nombres_output_lineEdit"
        )
        self.p3nombres_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3nombres_label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.p3nombres_label.setObjectName("p3nombres_label")
        self.p3apellido_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3apellido_output_lineEdit.setGeometry(
            QtCore.QRect(270, 60, 221, 22)
        )
        self.p3apellido_output_lineEdit.setText("")
        self.p3apellido_output_lineEdit.setReadOnly(True)
        self.p3apellido_output_lineEdit.setObjectName(
            "p3apellido_output_lineEdit"
        )
        self.p3apellido_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3apellido_label.setGeometry(QtCore.QRect(270, 40, 101, 16))
        self.p3apellido_label.setObjectName("p3apellido_label")
        self.p3emailBuscar_label = QtWidgets.QLabel(self.panelEmail_groupBox)
        self.p3emailBuscar_label.setGeometry(QtCore.QRect(20, 100, 171, 16))
        self.p3emailBuscar_label.setObjectName("p3emailBuscar_label")
        self.p3emailBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox
        )
        self.p3emailBuscar_lineEdit.setGeometry(QtCore.QRect(20, 120, 301, 22))
        self.p3emailBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3emailBuscar_lineEdit.setText("")
        self.p3emailBuscar_lineEdit.setReadOnly(False)
        self.p3emailBuscar_lineEdit.setObjectName("p3emailBuscar_lineEdit")
        self.p3emailBuscar_pushButton = QtWidgets.QPushButton(
            self.panelEmail_groupBox
        )
        self.p3emailBuscar_pushButton.setEnabled(True)
        self.p3emailBuscar_pushButton.setGeometry(
            QtCore.QRect(350, 120, 141, 24)
        )
        self.p3emailBuscar_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.p3emailBuscar_pushButton.setObjectName("p3emailBuscar_pushButton")
        self.mujer_label_3 = QtWidgets.QLabel(self.tab_profesional_5)
        self.mujer_label_3.setGeometry(QtCore.QRect(150, 40, 321, 321))
        self.mujer_label_3.setStyleSheet("background: none;")
        self.mujer_label_3.setText("")
        self.mujer_label_3.setPixmap(
            QtGui.QPixmap(":/people/laptop-poses_2.png")
        )
        self.mujer_label_3.setScaledContents(True)
        self.mujer_label_3.setObjectName("mujer_label_3")
        self.mujer_label_3.raise_()
        self.pro3dashboard_groupBox.raise_()
        self.p3panelcvu_groupBox.raise_()
        self.p3panelnumeor_groupBox.raise_()
        self.panelEmail_groupBox.raise_()
        self.tabWidget.addTab(self.tab_profesional_5, "")
        self.tab_international = QtWidgets.QWidget()
        self.tab_international.setEnabled(True)
        self.tab_international.setObjectName("tab_international")
        self.argentina_pushButton = QtWidgets.QPushButton(
            self.tab_international
        )
        self.argentina_pushButton.setGeometry(QtCore.QRect(410, 110, 71, 71))
        self.argentina_pushButton.setStyleSheet("")
        self.argentina_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/argentina.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.argentina_pushButton.setIcon(icon1)
        self.argentina_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.argentina_pushButton.setAutoRepeat(False)
        self.argentina_pushButton.setObjectName("argentina_pushButton")
        self.bolivia_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.bolivia_pushButton.setEnabled(False)
        self.bolivia_pushButton.setGeometry(QtCore.QRect(520, 110, 71, 71))
        self.bolivia_pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/bolivia.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.bolivia_pushButton.setIcon(icon2)
        self.bolivia_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.bolivia_pushButton.setAutoRepeat(False)
        self.bolivia_pushButton.setObjectName("bolivia_pushButton")
        self.brazil_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.brazil_pushButton.setEnabled(False)
        self.brazil_pushButton.setGeometry(QtCore.QRect(630, 110, 71, 71))
        self.brazil_pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/brazil.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.brazil_pushButton.setIcon(icon3)
        self.brazil_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.brazil_pushButton.setAutoRepeat(False)
        self.brazil_pushButton.setObjectName("brazil_pushButton")
        self.chile_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.chile_pushButton.setEnabled(False)
        self.chile_pushButton.setGeometry(QtCore.QRect(410, 220, 71, 71))
        self.chile_pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/chile.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.chile_pushButton.setIcon(icon4)
        self.chile_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.chile_pushButton.setAutoRepeat(False)
        self.chile_pushButton.setObjectName("chile_pushButton")
        self.ecuador_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.ecuador_pushButton.setEnabled(False)
        self.ecuador_pushButton.setGeometry(QtCore.QRect(630, 220, 71, 71))
        self.ecuador_pushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/ecuador.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.ecuador_pushButton.setIcon(icon5)
        self.ecuador_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.ecuador_pushButton.setAutoRepeat(False)
        self.ecuador_pushButton.setObjectName("ecuador_pushButton")
        self.colombia_pushButton = QtWidgets.QPushButton(
            self.tab_international
        )
        self.colombia_pushButton.setEnabled(False)
        self.colombia_pushButton.setGeometry(QtCore.QRect(520, 220, 71, 71))
        self.colombia_pushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/colombia.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.colombia_pushButton.setIcon(icon6)
        self.colombia_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.colombia_pushButton.setAutoRepeat(False)
        self.colombia_pushButton.setObjectName("colombia_pushButton")
        self.mexico_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.mexico_pushButton.setEnabled(False)
        self.mexico_pushButton.setGeometry(QtCore.QRect(410, 330, 71, 71))
        self.mexico_pushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/mexico.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.mexico_pushButton.setIcon(icon7)
        self.mexico_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.mexico_pushButton.setAutoRepeat(False)
        self.mexico_pushButton.setObjectName("mexico_pushButton")
        self.paraguay_pushButton = QtWidgets.QPushButton(
            self.tab_international
        )
        self.paraguay_pushButton.setEnabled(False)
        self.paraguay_pushButton.setGeometry(QtCore.QRect(520, 330, 71, 71))
        self.paraguay_pushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/paraguay.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.paraguay_pushButton.setIcon(icon8)
        self.paraguay_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.paraguay_pushButton.setAutoRepeat(False)
        self.paraguay_pushButton.setObjectName("paraguay_pushButton")
        self.peru_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.peru_pushButton.setGeometry(QtCore.QRect(630, 330, 71, 71))
        self.peru_pushButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/peru.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.peru_pushButton.setIcon(icon9)
        self.peru_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.peru_pushButton.setAutoRepeat(False)
        self.peru_pushButton.setObjectName("peru_pushButton")
        self.uruguay_pushButton = QtWidgets.QPushButton(self.tab_international)
        self.uruguay_pushButton.setEnabled(False)
        self.uruguay_pushButton.setGeometry(QtCore.QRect(410, 440, 71, 71))
        self.uruguay_pushButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/uruguay.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.uruguay_pushButton.setIcon(icon10)
        self.uruguay_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.uruguay_pushButton.setAutoRepeat(False)
        self.uruguay_pushButton.setObjectName("uruguay_pushButton")
        self.venezuela_pushButton = QtWidgets.QPushButton(
            self.tab_international
        )
        self.venezuela_pushButton.setEnabled(False)
        self.venezuela_pushButton.setGeometry(QtCore.QRect(520, 440, 71, 71))
        self.venezuela_pushButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/venezuela.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.venezuela_pushButton.setIcon(icon11)
        self.venezuela_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.venezuela_pushButton.setAutoRepeat(False)
        self.venezuela_pushButton.setObjectName("venezuela_pushButton")
        self.salvador_pushButton = QtWidgets.QPushButton(
            self.tab_international
        )
        self.salvador_pushButton.setEnabled(False)
        self.salvador_pushButton.setGeometry(QtCore.QRect(630, 440, 71, 71))
        self.salvador_pushButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/salvador.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.salvador_pushButton.setIcon(icon12)
        self.salvador_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.salvador_pushButton.setAutoRepeat(False)
        self.salvador_pushButton.setObjectName("salvador_pushButton")
        self.proximamente_label = QtWidgets.QLabel(self.tab_international)
        self.proximamente_label.setGeometry(QtCore.QRect(480, 50, 161, 21))
        self.proximamente_label.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background: none;\n"
            'font: 18pt "Segoe UI";'
        )
        self.proximamente_label.setAlignment(QtCore.Qt.AlignCenter)
        self.proximamente_label.setObjectName("proximamente_label")
        self.tabWidget.addTab(self.tab_international, "")
        self.tab_community = QtWidgets.QWidget()
        self.tab_community.setObjectName("tab_community")
        self.CMpanelnumeor_groupBox = QtWidgets.QGroupBox(self.tab_community)
        self.CMpanelnumeor_groupBox.setGeometry(QtCore.QRect(40, 30, 521, 221))
        self.CMpanelnumeor_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.CMpanelnumeor_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CMpanelnumeor_groupBox.setFlat(False)
        self.CMpanelnumeor_groupBox.setObjectName("CMpanelnumeor_groupBox")
        self.CMnombres2_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelnumeor_groupBox
        )
        self.CMnombres2_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 221, 22)
        )
        self.CMnombres2_output_lineEdit.setText("")
        self.CMnombres2_output_lineEdit.setReadOnly(True)
        self.CMnombres2_output_lineEdit.setObjectName(
            "CMnombres2_output_lineEdit"
        )
        self.nombres_label_2 = QtWidgets.QLabel(self.CMpanelnumeor_groupBox)
        self.nombres_label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.nombres_label_2.setObjectName("nombres_label_2")
        self.CMemail_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelnumeor_groupBox
        )
        self.CMemail_output_lineEdit.setGeometry(
            QtCore.QRect(20, 120, 221, 22)
        )
        self.CMemail_output_lineEdit.setText("")
        self.CMemail_output_lineEdit.setReadOnly(True)
        self.CMemail_output_lineEdit.setObjectName("CMemail_output_lineEdit")
        self.email_label_2 = QtWidgets.QLabel(self.CMpanelnumeor_groupBox)
        self.email_label_2.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.email_label_2.setObjectName("email_label_2")
        self.CMnumero_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelnumeor_groupBox
        )
        self.CMnumero_output_lineEdit.setGeometry(
            QtCore.QRect(270, 120, 221, 22)
        )
        self.CMnumero_output_lineEdit.setText("")
        self.CMnumero_output_lineEdit.setReadOnly(True)
        self.CMnumero_output_lineEdit.setObjectName("CMnumero_output_lineEdit")
        self.numer_label_2 = QtWidgets.QLabel(self.CMpanelnumeor_groupBox)
        self.numer_label_2.setGeometry(QtCore.QRect(270, 100, 61, 16))
        self.numer_label_2.setObjectName("numer_label_2")
        self.CMapellidos2_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelnumeor_groupBox
        )
        self.CMapellidos2_output_lineEdit.setGeometry(
            QtCore.QRect(270, 60, 221, 22)
        )
        self.CMapellidos2_output_lineEdit.setText("")
        self.CMapellidos2_output_lineEdit.setReadOnly(True)
        self.CMapellidos2_output_lineEdit.setObjectName(
            "CMapellidos2_output_lineEdit"
        )
        self.apellido_label_2 = QtWidgets.QLabel(self.CMpanelnumeor_groupBox)
        self.apellido_label_2.setGeometry(QtCore.QRect(270, 40, 71, 16))
        self.apellido_label_2.setObjectName("apellido_label_2")
        self.numberoabuscar_label_2 = QtWidgets.QLabel(
            self.CMpanelnumeor_groupBox
        )
        self.numberoabuscar_label_2.setGeometry(QtCore.QRect(20, 160, 171, 16))
        self.numberoabuscar_label_2.setObjectName("numberoabuscar_label_2")
        self.CMnumeroBuscar_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelnumeor_groupBox
        )
        self.CMnumeroBuscar_lineEdit.setGeometry(
            QtCore.QRect(20, 180, 301, 22)
        )
        self.CMnumeroBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMnumeroBuscar_lineEdit.setText("")
        self.CMnumeroBuscar_lineEdit.setReadOnly(False)
        self.CMnumeroBuscar_lineEdit.setObjectName("CMnumeroBuscar_lineEdit")
        self.CMbuscarDato_pushButton = QtWidgets.QPushButton(
            self.CMpanelnumeor_groupBox
        )
        self.CMbuscarDato_pushButton.setEnabled(True)
        self.CMbuscarDato_pushButton.setGeometry(
            QtCore.QRect(350, 180, 141, 24)
        )
        self.CMbuscarDato_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMbuscarDato_pushButton.setObjectName("CMbuscarDato_pushButton")
        self.CMpanelNumeros_groupBox = QtWidgets.QGroupBox(self.tab_community)
        self.CMpanelNumeros_groupBox.setGeometry(
            QtCore.QRect(40, 270, 521, 331)
        )
        self.CMpanelNumeros_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "}"
        )
        self.CMpanelNumeros_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CMpanelNumeros_groupBox.setFlat(False)
        self.CMpanelNumeros_groupBox.setObjectName("CMpanelNumeros_groupBox")
        self.CMnumeroBuscar_lineEdit_2 = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMnumeroBuscar_lineEdit_2.setGeometry(
            QtCore.QRect(20, 290, 301, 22)
        )
        self.CMnumeroBuscar_lineEdit_2.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMnumeroBuscar_lineEdit_2.setText("")
        self.CMnumeroBuscar_lineEdit_2.setReadOnly(False)
        self.CMnumeroBuscar_lineEdit_2.setObjectName(
            "CMnumeroBuscar_lineEdit_2"
        )
        self.numberoabuscar_label_3 = QtWidgets.QLabel(
            self.CMpanelNumeros_groupBox
        )
        self.numberoabuscar_label_3.setGeometry(QtCore.QRect(20, 270, 171, 16))
        self.numberoabuscar_label_3.setObjectName("numberoabuscar_label_3")
        self.CMbuscarDato_pushButton_2 = QtWidgets.QPushButton(
            self.CMpanelNumeros_groupBox
        )
        self.CMbuscarDato_pushButton_2.setEnabled(True)
        self.CMbuscarDato_pushButton_2.setGeometry(
            QtCore.QRect(350, 290, 141, 24)
        )
        self.CMbuscarDato_pushButton_2.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMbuscarDato_pushButton_2.setObjectName(
            "CMbuscarDato_pushButton_2"
        )
        self.CMnombre_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMnombre_output_lineEdit.setGeometry(
            QtCore.QRect(270, 50, 221, 22)
        )
        self.CMnombre_output_lineEdit.setText("")
        self.CMnombre_output_lineEdit.setReadOnly(True)
        self.CMnombre_output_lineEdit.setObjectName("CMnombre_output_lineEdit")
        self.email_label_3 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.email_label_3.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.email_label_3.setObjectName("email_label_3")
        self.apellido_label_3 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.apellido_label_3.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.apellido_label_3.setObjectName("apellido_label_3")
        self.numer_label_3 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.numer_label_3.setGeometry(QtCore.QRect(270, 30, 61, 16))
        self.numer_label_3.setObjectName("numer_label_3")
        self.CMdireccion_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMdireccion_output_lineEdit.setGeometry(
            QtCore.QRect(20, 110, 221, 22)
        )
        self.CMdireccion_output_lineEdit.setText("")
        self.CMdireccion_output_lineEdit.setReadOnly(True)
        self.CMdireccion_output_lineEdit.setObjectName(
            "CMdireccion_output_lineEdit"
        )
        self.CMdocumento_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMdocumento_output_lineEdit.setGeometry(
            QtCore.QRect(20, 50, 221, 22)
        )
        self.CMdocumento_output_lineEdit.setText("")
        self.CMdocumento_output_lineEdit.setReadOnly(True)
        self.CMdocumento_output_lineEdit.setObjectName(
            "CMdocumento_output_lineEdit"
        )
        self.email_label_4 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.email_label_4.setGeometry(QtCore.QRect(270, 90, 81, 16))
        self.email_label_4.setObjectName("email_label_4")
        self.CMlocalidad_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMlocalidad_output_lineEdit.setGeometry(
            QtCore.QRect(270, 110, 221, 22)
        )
        self.CMlocalidad_output_lineEdit.setText("")
        self.CMlocalidad_output_lineEdit.setReadOnly(True)
        self.CMlocalidad_output_lineEdit.setObjectName(
            "CMlocalidad_output_lineEdit"
        )
        self.CMprovincia_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMprovincia_output_lineEdit.setGeometry(
            QtCore.QRect(20, 170, 221, 22)
        )
        self.CMprovincia_output_lineEdit.setText("")
        self.CMprovincia_output_lineEdit.setReadOnly(True)
        self.CMprovincia_output_lineEdit.setObjectName(
            "CMprovincia_output_lineEdit"
        )
        self.email_label_5 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.email_label_5.setGeometry(QtCore.QRect(20, 150, 81, 16))
        self.email_label_5.setObjectName("email_label_5")
        self.CMcodigopostal_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMcodigopostal_output_lineEdit.setGeometry(
            QtCore.QRect(270, 170, 221, 22)
        )
        self.CMcodigopostal_output_lineEdit.setText("")
        self.CMcodigopostal_output_lineEdit.setReadOnly(True)
        self.CMcodigopostal_output_lineEdit.setObjectName(
            "CMcodigopostal_output_lineEdit"
        )
        self.email_label_6 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.email_label_6.setGeometry(QtCore.QRect(270, 150, 81, 16))
        self.email_label_6.setObjectName("email_label_6")
        self.email_label_7 = QtWidgets.QLabel(self.CMpanelNumeros_groupBox)
        self.email_label_7.setGeometry(QtCore.QRect(20, 210, 81, 16))
        self.email_label_7.setObjectName("email_label_7")
        self.CMempresa_output_lineEdit = QtWidgets.QLineEdit(
            self.CMpanelNumeros_groupBox
        )
        self.CMempresa_output_lineEdit.setGeometry(
            QtCore.QRect(20, 230, 471, 22)
        )
        self.CMempresa_output_lineEdit.setText("")
        self.CMempresa_output_lineEdit.setReadOnly(True)
        self.CMempresa_output_lineEdit.setObjectName(
            "CMempresa_output_lineEdit"
        )
        self.panelEmail_groupBox_2 = QtWidgets.QGroupBox(self.tab_community)
        self.panelEmail_groupBox_2.setGeometry(
            QtCore.QRect(580, 440, 521, 161)
        )
        self.panelEmail_groupBox_2.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
            "    border-radius: 5px;\n"
            "    margin-top: 1ex; /* leave space at the top for the title */\n"
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
            "QLineEdit {\n"
            "    color: white;\n"
            "    border: 1px solid rgb(119, 133, 255);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}"
        )
        self.panelEmail_groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.panelEmail_groupBox_2.setFlat(False)
        self.panelEmail_groupBox_2.setObjectName("panelEmail_groupBox_2")
        self.CMnombres_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox_2
        )
        self.CMnombres_output_lineEdit.setGeometry(
            QtCore.QRect(20, 60, 221, 22)
        )
        self.CMnombres_output_lineEdit.setText("")
        self.CMnombres_output_lineEdit.setReadOnly(True)
        self.CMnombres_output_lineEdit.setObjectName(
            "CMnombres_output_lineEdit"
        )
        self.p3nombres_label_2 = QtWidgets.QLabel(self.panelEmail_groupBox_2)
        self.p3nombres_label_2.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.p3nombres_label_2.setObjectName("p3nombres_label_2")
        self.CMapellido_output_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox_2
        )
        self.CMapellido_output_lineEdit.setGeometry(
            QtCore.QRect(270, 60, 221, 22)
        )
        self.CMapellido_output_lineEdit.setText("")
        self.CMapellido_output_lineEdit.setReadOnly(True)
        self.CMapellido_output_lineEdit.setObjectName(
            "CMapellido_output_lineEdit"
        )
        self.p3apellido_label_2 = QtWidgets.QLabel(self.panelEmail_groupBox_2)
        self.p3apellido_label_2.setGeometry(QtCore.QRect(270, 40, 101, 16))
        self.p3apellido_label_2.setObjectName("p3apellido_label_2")
        self.p3emailBuscar_label_2 = QtWidgets.QLabel(
            self.panelEmail_groupBox_2
        )
        self.p3emailBuscar_label_2.setGeometry(QtCore.QRect(20, 100, 171, 16))
        self.p3emailBuscar_label_2.setObjectName("p3emailBuscar_label_2")
        self.CMemailBuscar_lineEdit = QtWidgets.QLineEdit(
            self.panelEmail_groupBox_2
        )
        self.CMemailBuscar_lineEdit.setGeometry(QtCore.QRect(20, 120, 301, 22))
        self.CMemailBuscar_lineEdit.setStyleSheet(
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMemailBuscar_lineEdit.setText("")
        self.CMemailBuscar_lineEdit.setReadOnly(False)
        self.CMemailBuscar_lineEdit.setObjectName("CMemailBuscar_lineEdit")
        self.CMemailBuscar_pushButton = QtWidgets.QPushButton(
            self.panelEmail_groupBox_2
        )
        self.CMemailBuscar_pushButton.setEnabled(True)
        self.CMemailBuscar_pushButton.setGeometry(
            QtCore.QRect(350, 120, 141, 24)
        )
        self.CMemailBuscar_pushButton.setStyleSheet(
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.CMemailBuscar_pushButton.setObjectName("CMemailBuscar_pushButton")
        self.CMinformacion_groupBox = QtWidgets.QGroupBox(self.tab_community)
        self.CMinformacion_groupBox.setGeometry(
            QtCore.QRect(580, 30, 521, 241)
        )
        self.CMinformacion_groupBox.setStyleSheet(
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
        self.CMinformacion_groupBox.setTitle("")
        self.CMinformacion_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CMinformacion_groupBox.setFlat(False)
        self.CMinformacion_groupBox.setObjectName("CMinformacion_groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.CMinformacion_groupBox
        )
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CMInfo_textEdit = QtWidgets.QTextEdit(self.CMinformacion_groupBox)
        self.CMInfo_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CMInfo_textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CMInfo_textEdit.setReadOnly(True)
        self.CMInfo_textEdit.setObjectName("CMInfo_textEdit")
        self.verticalLayout_3.addWidget(self.CMInfo_textEdit)
        self.CMConsole_textBrowser = QtWidgets.QTextBrowser(self.tab_community)
        self.CMConsole_textBrowser.setGeometry(
            QtCore.QRect(580, 290, 521, 131)
        )
        self.CMConsole_textBrowser.setStyleSheet(
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.CMConsole_textBrowser.setObjectName("CMConsole_textBrowser")
        self.tabWidget.addTab(self.tab_community, "")
        self.tab_reports = QtWidgets.QWidget()
        self.tab_reports.setObjectName("tab_reports")
        self.reportes_groupBox = QtWidgets.QGroupBox(self.tab_reports)
        self.reportes_groupBox.setGeometry(QtCore.QRect(10, 20, 711, 591))
        self.reportes_groupBox.setStyleSheet(
            "QGroupBox {\n"
            "    color: rgb(255, 255, 255);\n"
            "    border: 2px solid rgb(119, 133, 255);\n"
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
            "QLineEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLineEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QLabel {\n"
            "    color: gray;\n"
            "    background: none;\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::disabled {\n"
            "    color: gray;\n"
            "    border: 1px solid gray;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    color: rgb(255, 133, 65);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 183, 122);\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}\n"
            "\n"
            "QComboBox {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QComboBox::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QListView {\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QPlainTextEdit {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background-color: rgb(39, 39, 46);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}\n"
            "\n"
            "QPlainTextEdit::hover {\n"
            "    color: rgb(255, 183, 122);\n"
            "    background: none;\n"
            "    background-color: rgb(54, 54, 54);\n"
            "    border: 1px solid rgb(255, 133, 65);\n"
            "    border-top: 0px;\n"
            "    border-right: 0px;\n"
            "    border-left: 0px;\n"
            "    border-radius: 2px;\n"
            "}"
        )
        self.reportes_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.reportes_groupBox.setFlat(False)
        self.reportes_groupBox.setObjectName("reportes_groupBox")
        self.tipoVulnerabilidad_comboBox = QtWidgets.QComboBox(
            self.reportes_groupBox
        )
        self.tipoVulnerabilidad_comboBox.setGeometry(
            QtCore.QRect(160, 60, 241, 22)
        )
        self.tipoVulnerabilidad_comboBox.setObjectName(
            "tipoVulnerabilidad_comboBox"
        )
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.setItemText(0, "")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipoVulnerabilidad_comboBox.addItem("")
        self.tipovuln_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.tipovuln_label.setGeometry(QtCore.QRect(160, 36, 141, 20))
        self.tipovuln_label.setObjectName("tipovuln_label")
        self.recurso_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.recurso_label.setGeometry(QtCore.QRect(420, 36, 61, 20))
        self.recurso_label.setObjectName("recurso_label")
        self.recurso_comboBox = QtWidgets.QComboBox(self.reportes_groupBox)
        self.recurso_comboBox.setGeometry(QtCore.QRect(420, 60, 161, 22))
        self.recurso_comboBox.setObjectName("recurso_comboBox")
        self.recurso_comboBox.addItem("")
        self.recurso_comboBox.setItemText(0, "")
        self.recurso_comboBox.addItem("")
        self.recurso_comboBox.addItem("")
        self.nivelImpacto_comboBox = QtWidgets.QComboBox(
            self.reportes_groupBox
        )
        self.nivelImpacto_comboBox.setGeometry(QtCore.QRect(600, 60, 91, 22))
        self.nivelImpacto_comboBox.setObjectName("nivelImpacto_comboBox")
        self.nivelImpacto_comboBox.addItem("")
        self.nivelImpacto_comboBox.setItemText(0, "")
        self.nivelImpacto_comboBox.addItem("")
        self.nivelImpacto_comboBox.addItem("")
        self.nivelImpacto_comboBox.addItem("")
        self.nivelImpacto_comboBox.addItem("")
        self.nivelimpact_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.nivelimpact_label.setGeometry(QtCore.QRect(600, 36, 101, 20))
        self.nivelimpact_label.setObjectName("nivelimpact_label")
        self.discordid_lineEdit = QtWidgets.QLineEdit(self.reportes_groupBox)
        self.discordid_lineEdit.setGeometry(QtCore.QRect(20, 60, 121, 22))
        self.discordid_lineEdit.setText("")
        self.discordid_lineEdit.setReadOnly(False)
        self.discordid_lineEdit.setObjectName("discordid_lineEdit")
        self.discord_id_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.discord_id_label.setGeometry(QtCore.QRect(20, 36, 141, 21))
        self.discord_id_label.setObjectName("discord_id_label")
        self.tituloreporte_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.tituloreporte_label.setGeometry(QtCore.QRect(20, 110, 61, 21))
        self.tituloreporte_label.setObjectName("tituloreporte_label")
        self.tituloreporte_lineEdit = QtWidgets.QLineEdit(
            self.reportes_groupBox
        )
        self.tituloreporte_lineEdit.setGeometry(QtCore.QRect(20, 130, 671, 22))
        self.tituloreporte_lineEdit.setText("")
        self.tituloreporte_lineEdit.setReadOnly(False)
        self.tituloreporte_lineEdit.setObjectName("tituloreporte_lineEdit")
        self.descripcionreporte_label = QtWidgets.QLabel(
            self.reportes_groupBox
        )
        self.descripcionreporte_label.setGeometry(
            QtCore.QRect(20, 170, 101, 21)
        )
        self.descripcionreporte_label.setObjectName("descripcionreporte_label")
        self.descripcionreporte_plainTextEdit = QtWidgets.QPlainTextEdit(
            self.reportes_groupBox
        )
        self.descripcionreporte_plainTextEdit.setGeometry(
            QtCore.QRect(20, 200, 671, 221)
        )
        self.descripcionreporte_plainTextEdit.setObjectName(
            "descripcionreporte_plainTextEdit"
        )
        self.impactoreporte_label = QtWidgets.QLabel(self.reportes_groupBox)
        self.impactoreporte_label.setGeometry(QtCore.QRect(20, 430, 81, 21))
        self.impactoreporte_label.setObjectName("impactoreporte_label")
        self.impactoreporte_plainTextEdit = QtWidgets.QPlainTextEdit(
            self.reportes_groupBox
        )
        self.impactoreporte_plainTextEdit.setGeometry(
            QtCore.QRect(20, 460, 671, 71)
        )
        self.impactoreporte_plainTextEdit.setObjectName(
            "impactoreporte_plainTextEdit"
        )
        self.enviarReporte_pushButton = QtWidgets.QPushButton(
            self.reportes_groupBox
        )
        self.enviarReporte_pushButton.setEnabled(True)
        self.enviarReporte_pushButton.setGeometry(
            QtCore.QRect(20, 550, 671, 24)
        )
        self.enviarReporte_pushButton.setObjectName("enviarReporte_pushButton")
        self.reporteDisclosure_groupBox = QtWidgets.QGroupBox(self.tab_reports)
        self.reporteDisclosure_groupBox.setGeometry(
            QtCore.QRect(730, 20, 401, 281)
        )
        self.reporteDisclosure_groupBox.setStyleSheet(
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
        self.reporteDisclosure_groupBox.setTitle("")
        self.reporteDisclosure_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.reporteDisclosure_groupBox.setFlat(False)
        self.reporteDisclosure_groupBox.setObjectName(
            "reporteDisclosure_groupBox"
        )
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(
            self.reporteDisclosure_groupBox
        )
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.reporteDisclosure_textEdit = QtWidgets.QTextEdit(
            self.reporteDisclosure_groupBox
        )
        self.reporteDisclosure_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.reporteDisclosure_textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.reporteDisclosure_textEdit.setReadOnly(True)
        self.reporteDisclosure_textEdit.setObjectName(
            "reporteDisclosure_textEdit"
        )
        self.verticalLayout_4.addWidget(self.reporteDisclosure_textEdit)
        self.halloffame_groupBox = QtWidgets.QGroupBox(self.tab_reports)
        self.halloffame_groupBox.setGeometry(QtCore.QRect(730, 310, 401, 171))
        self.halloffame_groupBox.setStyleSheet(
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
        self.halloffame_groupBox.setTitle("")
        self.halloffame_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.halloffame_groupBox.setFlat(False)
        self.halloffame_groupBox.setObjectName("halloffame_groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.halloffame_groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.halloffame_textEdit = QtWidgets.QTextEdit(
            self.halloffame_groupBox
        )
        self.halloffame_textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.halloffame_textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.halloffame_textEdit.setReadOnly(True)
        self.halloffame_textEdit.setObjectName("halloffame_textEdit")
        self.verticalLayout_5.addWidget(self.halloffame_textEdit)
        self.reports_textBrowser = QtWidgets.QTextBrowser(self.tab_reports)
        self.reports_textBrowser.setGeometry(QtCore.QRect(730, 490, 401, 121))
        self.reports_textBrowser.setStyleSheet(
            "QTextBrowser {\n"
            "    color: white;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "}"
        )
        self.reports_textBrowser.setObjectName("reports_textBrowser")
        self.tabWidget.addTab(self.tab_reports, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sigma Client"))
        self.mconsole_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.mbackout_label.setText(_translate("MainWindow", "Backend output"))
        self.validarLogin_pushButton.setText(_translate("MainWindow", "Login"))
        self.usuario_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Usuario")
        )
        self.password_lineEdit.setPlaceholderText(
            _translate("MainWindow", "Contraseña")
        )
        self.sigma_version_label.setText(
            _translate("MainWindow", "Sigma Client")
        )
        self.informacion_textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:700;">Terminos de acuerdo</span></p>\n'
                '<p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">El motor de búsqueda que usa &quot;Sigma&quot; es un programa informático que encuentra información en Internet especializado en inteligencia de código abierto (Open Source Intelligence). Sigma proporcionará servicio con una funcionalidad limitada de forma gratuita, y en una funcionalidad como la descrita a continuación en este Acuerdo con suscripciones mensuales o anuales. </span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">El presente Acuerdo es válido y vinculante para ambas partes si (i) se celebra un contrato por escrito entre Sigma y el Cliente, y/o (ii) el Cliente acepta los términos y condiciones del presente Acuerdo en el formulario electrónico al registrarse, y/o (iii) al utilizar la versión gratuita de Sigma. Sigma no está obligada a proporcionar al Cliente el servicio Sigma antes de que el Cliente pague la tarifa correspondiente.</span></p>\n'
                '<p align="center" style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:700;">Tutorial de uso</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700;">International</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Los endpoints en la pestaña international no requieren plan.</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700;">Standard</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Los usuarios que posean el plan standard o superior pueden utilizar los endpoints para buscar información OSINT a través de DNI. Los resultados también incluyen numeros de teléfono y sus respectivas empresas.</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700;">Medium</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Los usuarios que posean el plan medium o superior pueden utilizar los endpoints que les permitan obtener información via OSINT sobre vehiculos y matriculas, junto con sus titulares, además de acceso a DB leaks premium de Sigma.</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700;">Profesional</span></p>\n'
                '<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Los usuarios que posean el plan profesional pueden utilizar los endpoints de recopilación de información avanzada de DNI, busqueda de numeros y también emails de numeros Movistar.</span></p></body></html>',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_main),
            _translate("MainWindow", "Main Menu"),
        )
        self.panelDNI_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por DNI")
        )
        self.pddni_label.setText(_translate("MainWindow", "DNI"))
        self.pdappelido_label.setText(_translate("MainWindow", "Apellido"))
        self.pdnombres_label.setText(_translate("MainWindow", "Nombres"))
        self.pdcalle_label.setText(_translate("MainWindow", "Calle"))
        self.pdseccion_label.setText(_translate("MainWindow", "Seccion"))
        self.pdcircuito_label.setText(_translate("MainWindow", "Circuito"))
        self.pdlocalidad_label.setText(_translate("MainWindow", "Localidad"))
        self.pdtipodoc_label.setText(
            _translate("MainWindow", "Tipo Documento")
        )
        self.pdprovincia_label.setText(_translate("MainWindow", "Provincia"))
        self.pdcodigopostal_label.setText(
            _translate("MainWindow", "Codigo Postal")
        )
        item = self.snumeros_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Celular"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Empresa"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.snumeros_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "C. Postal"))
        self.pdnumeros_label.setText(
            _translate("MainWindow", "Numeros de telefono por DNI")
        )
        self.standardDashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.dnibuscar_label.setText(_translate("MainWindow", "DNI a buscar"))
        self.sbuscardatos_pushButton.setText(
            _translate("MainWindow", "Buscar datos")
        )
        self.standardConsole_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.sdbackend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.sbuscartelefono_pushButton.setText(
            _translate("MainWindow", "Buscar telefonos")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_standard),
            _translate("MainWindow", "Standard"),
        )
        self.panel_patentes_groupBox.setTitle(
            _translate("MainWindow", "Panel de patentes")
        )
        item = self.patentes_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patente"))
        item = self.patentes_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.patentes_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vehiculo"))
        item = self.patentes_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.patentes_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Año"))
        item = self.patentes_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Titular"))
        item = self.patentes_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "%"))
        item = self.patentes_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Calle"))
        item = self.patentes_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Altura"))
        item = self.patentes_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Piso"))
        item = self.patentes_tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Depto"))
        item = self.patentes_tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "C. Postal"))
        item = self.patentes_tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.patentes_tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Tramite"))
        self.mdashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.patenteBuscar_label.setText(
            _translate("MainWindow", "Patente a buscar")
        )
        self.buscarPatente_pushButton.setText(
            _translate("MainWindow", "Buscar por patente")
        )
        self.mconsoleback_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.mbackoutput_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.mdnibuscar_label.setText(_translate("MainWindow", "DNI a buscar"))
        self.buscarPatentDNI_pushButton.setText(
            _translate("MainWindow", "Buscar por DNI")
        )
        self.mdatabreach_groupBox.setTitle(
            _translate("MainWindow", "Data breach")
        )
        self.querybreach_label.setText(_translate("MainWindow", "Query"))
        self.buscarLeaks_pushButton.setText(
            _translate("MainWindow", "Buscar leaks")
        )
        item = self.dataBreachResults_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Email"))
        item = self.dataBreachResults_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Password"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_medium),
            _translate("MainWindow", "Medium"),
        )
        self.prodashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.pronumbusc_label.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.proBuscarNum_pushButton.setText(
            _translate("MainWindow", "Buscar por numero")
        )
        self.proConsole_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.probackend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.dnibuscarpro_label.setText(
            _translate("MainWindow", "DNI a buscar")
        )
        self.proBuscarDni_pushButton.setText(
            _translate("MainWindow", "Buscar por DNI")
        )
        self.proGenero_comboBox.setItemText(
            0, _translate("MainWindow", "Masculino")
        )
        self.proGenero_comboBox.setItemText(
            1, _translate("MainWindow", "Femenino")
        )
        self.dnibuscarpro_label_2.setText(
            _translate("MainWindow", "Genero DNI")
        )
        self.promovistar_groupBox.setTitle(
            _translate("MainWindow", "Panel de Movistar")
        )
        self.pronumero_label.setText(_translate("MainWindow", "Numero"))
        self.proEmail_label.setText(_translate("MainWindow", "Email"))
        self.proBuscarEmail_pushButton.setText(
            _translate("MainWindow", "Buscar email")
        )
        self.pronumeroABuscar_label.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.panelNumeros_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por numero")
        )
        self.proNumeros_tableWidget.setWhatsThis(
            _translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        item = self.proNumeros_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Celular"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "C. Postal"))
        item = self.proNumeros_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Empresa"))
        self.proPersonas_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por DNI")
        )
        self.emision_label.setText(_translate("MainWindow", "Emision"))
        self.nroDocumento_label.setText(
            _translate("MainWindow", "Nro. Documento")
        )
        self.proApellido_label.setText(_translate("MainWindow", "Apellido"))
        self.proNombre_label.setText(_translate("MainWindow", "Nombres"))
        self.cuil_label.setText(_translate("MainWindow", "CUIL"))
        self.barrio_label.setText(_translate("MainWindow", "Barrio"))
        self.calle_label.setText(_translate("MainWindow", "Calle"))
        self.altura_label.setText(_translate("MainWindow", "Altura"))
        self.piso_label.setText(_translate("MainWindow", "Piso"))
        self.departamento_label.setText(
            _translate("MainWindow", "Departamento")
        )
        self.provincia_label.setText(_translate("MainWindow", "Provincia"))
        self.pais_label.setText(_translate("MainWindow", "Pais"))
        self.monoblock_label.setText(_translate("MainWindow", "Monoblock"))
        self.ciudad_label.setText(_translate("MainWindow", "Ciudad"))
        self.municipio_label.setText(_translate("MainWindow", "Municipio"))
        self.fechanac_label.setText(
            _translate("MainWindow", "Fecha Nacimiento")
        )
        self.fallecido_label.setText(_translate("MainWindow", "Fallecido"))
        self.obrassociales_label.setText(
            _translate("MainWindow", "Obras sociales")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_profesional),
            _translate("MainWindow", "Profesional"),
        )
        self.pro2dashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.proNombrebusc_label.setText(
            _translate("MainWindow", "Nombre/DNI a buscar")
        )
        self.proBuscarNombre_pushButton.setText(
            _translate("MainWindow", "Buscar por nombre")
        )
        self.pro2Console_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.pro2backend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.proProvinciabusc_label.setText(
            _translate("MainWindow", "Provincia (Opcional)")
        )
        self.proLocalidadbusc_label.setText(
            _translate("MainWindow", "Localidad (Opcional)")
        )
        self.proProvincia_comboBox.setItemText(
            1, _translate("MainWindow", "capital_federal")
        )
        self.proProvincia_comboBox.setItemText(
            2, _translate("MainWindow", "buenos_aires")
        )
        self.proProvincia_comboBox.setItemText(
            3, _translate("MainWindow", "catamarca")
        )
        self.proProvincia_comboBox.setItemText(
            4, _translate("MainWindow", "chaco")
        )
        self.proProvincia_comboBox.setItemText(
            5, _translate("MainWindow", "chubut")
        )
        self.proProvincia_comboBox.setItemText(
            6, _translate("MainWindow", "cordoba")
        )
        self.proProvincia_comboBox.setItemText(
            7, _translate("MainWindow", "corrientes")
        )
        self.proProvincia_comboBox.setItemText(
            8, _translate("MainWindow", "entre_rios")
        )
        self.proProvincia_comboBox.setItemText(
            9, _translate("MainWindow", "formosa")
        )
        self.proProvincia_comboBox.setItemText(
            10, _translate("MainWindow", "jujuy")
        )
        self.proProvincia_comboBox.setItemText(
            11, _translate("MainWindow", "la_pampa")
        )
        self.proProvincia_comboBox.setItemText(
            12, _translate("MainWindow", "la_rioja")
        )
        self.proProvincia_comboBox.setItemText(
            13, _translate("MainWindow", "mendoza")
        )
        self.proProvincia_comboBox.setItemText(
            14, _translate("MainWindow", "misiones")
        )
        self.proProvincia_comboBox.setItemText(
            15, _translate("MainWindow", "neuquen")
        )
        self.proProvincia_comboBox.setItemText(
            16, _translate("MainWindow", "rio_negro")
        )
        self.proProvincia_comboBox.setItemText(
            17, _translate("MainWindow", "salta")
        )
        self.proProvincia_comboBox.setItemText(
            18, _translate("MainWindow", "san_juan")
        )
        self.proProvincia_comboBox.setItemText(
            19, _translate("MainWindow", "san_luis")
        )
        self.proProvincia_comboBox.setItemText(
            20, _translate("MainWindow", "santa_cruz")
        )
        self.proProvincia_comboBox.setItemText(
            21, _translate("MainWindow", "santa_fe")
        )
        self.proProvincia_comboBox.setItemText(
            22, _translate("MainWindow", "santiago_del_estero")
        )
        self.proProvincia_comboBox.setItemText(
            23, _translate("MainWindow", "tierra_del_fuego")
        )
        self.proProvincia_comboBox.setItemText(
            24, _translate("MainWindow", "tucuman")
        )
        self.proEdadbusc_label.setText(
            _translate("MainWindow", "Edad desde - hasta (Opcional)")
        )
        self.panelPersonas_groupBox.setTitle(
            _translate("MainWindow", "Panel de personas")
        )
        self.panelNumeros_groupBox_3.setTitle(
            _translate("MainWindow", "Panel de vecinos")
        )
        self.proVecinos_tableWidget.setWhatsThis(
            _translate(
                "MainWindow", "<html><head/><body><p><br/></p></body></html>"
            )
        )
        item = self.proVecinos_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Documento"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Empresa"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Localidad"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Provincia"))
        item = self.proVecinos_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "C. Postal"))
        self.proBuscarVecinos_pushButton.setText(
            _translate("MainWindow", "Buscar vecinos")
        )
        self.direccionbuscarpro_label.setText(
            _translate("MainWindow", "Direccion a buscar")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_profesional_2),
            _translate("MainWindow", "Profesional II"),
        )
        self.pro3dashboard_groupBox.setTitle(
            _translate("MainWindow", "Dashboard")
        )
        self.pro3Console_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.pro3backend_label.setText(
            _translate("MainWindow", "Backend output")
        )
        self.p3panelcvu_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por CBU/CVU")
        )
        self.titular_label.setText(_translate("MainWindow", "Titular"))
        self.banco_label.setText(_translate("MainWindow", "Banco"))
        self.cbucvu_label.setText(_translate("MainWindow", "CBU/CVU"))
        self.cuit_label.setText(_translate("MainWindow", "Cuit"))
        self.tipoCuenta_label.setText(
            _translate("MainWindow", "Tipo de cuenta")
        )
        self.cbvucvubuscar_label.setText(
            _translate("MainWindow", "CBU/CVU o alias a buscar")
        )
        self.p3buscarcvuTitular_pushButton.setText(
            _translate("MainWindow", "Buscar titular")
        )
        self.p3panelnumeor_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por numero II")
        )
        self.nombres_label.setText(_translate("MainWindow", "Nombres"))
        self.email_label.setText(_translate("MainWindow", "Email"))
        self.numer_label.setText(_translate("MainWindow", "Numero"))
        self.apellido_label.setText(_translate("MainWindow", "Apellido"))
        self.numberoabuscar_label.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.p3buscarDato_pushButton.setText(
            _translate("MainWindow", "Buscar datos")
        )
        self.panelEmail_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por email")
        )
        self.p3nombres_label.setText(_translate("MainWindow", "Nombres"))
        self.p3apellido_label.setText(_translate("MainWindow", "Apellido"))
        self.p3emailBuscar_label.setText(
            _translate("MainWindow", "Email a buscar")
        )
        self.p3emailBuscar_pushButton.setText(
            _translate("MainWindow", "Buscar por email")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_profesional_5),
            _translate("MainWindow", "Profesional III"),
        )
        self.proximamente_label.setText(
            _translate("MainWindow", "Proximamente")
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_international),
            _translate("MainWindow", "International"),
        )
        self.CMpanelnumeor_groupBox.setTitle(
            _translate(
                "MainWindow", "Panel de datos por numero II (community)"
            )
        )
        self.nombres_label_2.setText(_translate("MainWindow", "Nombres"))
        self.email_label_2.setText(_translate("MainWindow", "Email"))
        self.numer_label_2.setText(_translate("MainWindow", "Numero"))
        self.apellido_label_2.setText(_translate("MainWindow", "Apellido"))
        self.numberoabuscar_label_2.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.CMbuscarDato_pushButton.setText(
            _translate("MainWindow", "Buscar datos")
        )
        self.CMpanelNumeros_groupBox.setTitle(
            _translate("MainWindow", "Panel de datos por numero (community)")
        )
        self.numberoabuscar_label_3.setText(
            _translate("MainWindow", "Numero a buscar")
        )
        self.CMbuscarDato_pushButton_2.setText(
            _translate("MainWindow", "Buscar datos")
        )
        self.email_label_3.setText(_translate("MainWindow", "Direccion"))
        self.apellido_label_3.setText(_translate("MainWindow", "Documento"))
        self.numer_label_3.setText(_translate("MainWindow", "Nombre"))
        self.email_label_4.setText(_translate("MainWindow", "Localidad"))
        self.email_label_5.setText(_translate("MainWindow", "Provincia"))
        self.email_label_6.setText(_translate("MainWindow", "Codigo Postal"))
        self.email_label_7.setText(_translate("MainWindow", "Empresa"))
        self.panelEmail_groupBox_2.setTitle(
            _translate("MainWindow", "Panel de datos por email (community)")
        )
        self.p3nombres_label_2.setText(_translate("MainWindow", "Nombres"))
        self.p3apellido_label_2.setText(_translate("MainWindow", "Apellido"))
        self.p3emailBuscar_label_2.setText(
            _translate("MainWindow", "Email a buscar")
        )
        self.CMemailBuscar_pushButton.setText(
            _translate("MainWindow", "Buscar por email")
        )
        self.CMInfo_textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:20pt;">Community</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Los endpoints presentados en esta pagina estan disponibles de forma gratuita con uso limitado para aquellos miembros de comunidades amigas que deseen testear y formar parte de nuestro vulnerability disclosure program.</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">Los datos presentados se muestran </span><span style=" font-size:12pt; font-weight:700;">parcialmente</span><span style=" font-size:12pt;">, para informes completos se requiere la compra de un plan en Sigma Search.</span></p></body></html>',
            )
        )
        self.CMConsole_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_community),
            _translate("MainWindow", "Community"),
        )
        self.reportes_groupBox.setTitle(_translate("MainWindow", "Reportes"))
        self.tipoVulnerabilidad_comboBox.setItemText(
            1, _translate("MainWindow", "A01 Broken Access Control")
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            2, _translate("MainWindow", "A02 Cryptographic Failures")
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            3, _translate("MainWindow", "A03 Injection")
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            4, _translate("MainWindow", "A04 Insecure Design")
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            5, _translate("MainWindow", "A05 Security Misconfiguration")
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            6,
            _translate("MainWindow", "A06 Vulnerable and Outdated Components"),
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            7,
            _translate(
                "MainWindow", "A07 Identification and Authentication Failures"
            ),
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            8,
            _translate(
                "MainWindow", "A08 Software and Data Integrity Failures"
            ),
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            9,
            _translate(
                "MainWindow", "A09 Security Logging and Monitoring Failures"
            ),
        )
        self.tipoVulnerabilidad_comboBox.setItemText(
            10,
            _translate("MainWindow", "A10 Server Side Request Forgery (SSRF)"),
        )
        self.tipovuln_label.setText(
            _translate("MainWindow", "Tipo de vunerabilidad *")
        )
        self.recurso_label.setText(_translate("MainWindow", "Recurso *"))
        self.recurso_comboBox.setItemText(
            1, _translate("MainWindow", "Sigma Intelligence WebApp")
        )
        self.recurso_comboBox.setItemText(
            2, _translate("MainWindow", "Sigma Intelligence Client")
        )
        self.nivelImpacto_comboBox.setItemText(
            1, _translate("MainWindow", "Low")
        )
        self.nivelImpacto_comboBox.setItemText(
            2, _translate("MainWindow", "Medium")
        )
        self.nivelImpacto_comboBox.setItemText(
            3, _translate("MainWindow", "High")
        )
        self.nivelImpacto_comboBox.setItemText(
            4, _translate("MainWindow", "Critical")
        )
        self.nivelimpact_label.setText(
            _translate("MainWindow", "Nivel impacto *")
        )
        self.discord_id_label.setText(_translate("MainWindow", "Discord ID *"))
        self.tituloreporte_label.setText(_translate("MainWindow", "Titulo *"))
        self.descripcionreporte_label.setText(
            _translate("MainWindow", "Descripcion *")
        )
        self.impactoreporte_label.setText(
            _translate("MainWindow", "Impacto *")
        )
        self.enviarReporte_pushButton.setText(
            _translate("MainWindow", "Enviar")
        )
        self.reporteDisclosure_textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:20pt;">Vunerability Disclosure Program</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Los investigadores que sean los primeros en informar una vulnerabilidad serán los investigadores reconocidos en los changelogs  y <span style=" font-weight:700;">Hall of Fame</span> una vez que se resuelva la vulnerabilidad. Si hay miembros adicionales del equipo involucrados en la investigación de la vulnerabilidad, proporcione sus nombres y cuál fue su contribución a los hallazgos al enviar este informe.</p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:700;">Out of scope</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Rate-limit bypass, DoS/DDoS y vulnerabilidad sin impacto.</p></body></html>',
            )
        )
        self.halloffame_textEdit.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt;">Hall of Fame</span></p>\n'
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.reports_textBrowser.setHtml(
            _translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_reports),
            _translate("MainWindow", "Reports"),
        )
