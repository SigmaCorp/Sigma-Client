# -*- coding: utf-8 -*-

import asyncio
from . import resources_rc
from .utils import retrieve_data
from PyQt5 import QtCore, QtGui, QtWidgets


class PeruResolver(QtWidgets.QDialog):
    def __init__(self, client_parent):
        self.client_parent = client_parent
        super().__init__(self.client_parent.mainwindow)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PeruResolver")
        self.resize(754, 296)
        self.setMinimumSize(QtCore.QSize(754, 296))
        self.setMaximumSize(QtCore.QSize(754, 296))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icon/sigma.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.setWindowIcon(icon)
        self.setStyleSheet("background-image: url(:/back/back.png);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.freeperuDashboard_groupBox = QtWidgets.QGroupBox(
            self.centralwidget
        )
        self.freeperuDashboard_groupBox.setGeometry(
            QtCore.QRect(330, 30, 401, 241)
        )
        self.freeperuDashboard_groupBox.setStyleSheet(
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
        self.freeperuDashboard_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.freeperuDashboard_groupBox.setFlat(False)
        self.freeperuDashboard_groupBox.setObjectName(
            "freeperuDashboard_groupBox"
        )
        self.fperubuscar_label = QtWidgets.QLabel(
            self.freeperuDashboard_groupBox
        )
        self.fperubuscar_label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.fperubuscar_label.setObjectName("fperubuscar_label")
        self.fperuCelDoc_lineEdit = QtWidgets.QLineEdit(
            self.freeperuDashboard_groupBox
        )
        self.fperuCelDoc_lineEdit.setGeometry(QtCore.QRect(20, 60, 141, 22))
        self.fperuCelDoc_lineEdit.setText("")
        self.fperuCelDoc_lineEdit.setReadOnly(False)
        self.fperuCelDoc_lineEdit.setObjectName("fperuCelDoc_lineEdit")
        self.fperubuscardatos_pushButton = QtWidgets.QPushButton(
            self.freeperuDashboard_groupBox
        )
        self.fperubuscardatos_pushButton.setGeometry(
            QtCore.QRect(190, 60, 91, 24)
        )
        self.fperubuscardatos_pushButton.setObjectName(
            "fperubuscardatos_pushButton"
        )
        self.freePeruConsole_textBrowser = QtWidgets.QTextBrowser(
            self.freeperuDashboard_groupBox
        )
        self.freePeruConsole_textBrowser.setGeometry(
            QtCore.QRect(20, 130, 361, 91)
        )
        self.freePeruConsole_textBrowser.setObjectName(
            "freePeruConsole_textBrowser"
        )
        self.fperubackend_label = QtWidgets.QLabel(
            self.freeperuDashboard_groupBox
        )
        self.fperubackend_label.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.fperubackend_label.setObjectName("fperubackend_label")
        self.peruflag_pushButton = QtWidgets.QPushButton(
            self.freeperuDashboard_groupBox
        )
        self.peruflag_pushButton.setGeometry(QtCore.QRect(310, 30, 71, 71))
        self.peruflag_pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/flags/country_flags/peru.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.peruflag_pushButton.setIcon(icon1)
        self.peruflag_pushButton.setIconSize(QtCore.QSize(67, 67))
        self.peruflag_pushButton.setAutoRepeat(False)
        self.peruflag_pushButton.setObjectName("peruflag_pushButton")
        self.panelPeru_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.panelPeru_groupBox.setGeometry(QtCore.QRect(20, 20, 291, 261))
        self.panelPeru_groupBox.setStyleSheet(
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
        self.panelPeru_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.panelPeru_groupBox.setFlat(False)
        self.panelPeru_groupBox.setObjectName("panelPeru_groupBox")
        self.fperunumeros_tableWidget = QtWidgets.QTableWidget(
            self.panelPeru_groupBox
        )
        self.fperunumeros_tableWidget.setGeometry(
            QtCore.QRect(20, 70, 251, 171)
        )
        self.fperunumeros_tableWidget.setStyleSheet(
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
        self.fperunumeros_tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.fperunumeros_tableWidget.setLineWidth(1)
        self.fperunumeros_tableWidget.setMidLineWidth(0)
        self.fperunumeros_tableWidget.setObjectName("fperunumeros_tableWidget")
        self.fperunumeros_tableWidget.setColumnCount(2)
        self.fperunumeros_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.fperunumeros_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fperunumeros_tableWidget.setHorizontalHeaderItem(1, item)
        self.fperunumeros_label = QtWidgets.QLabel(self.panelPeru_groupBox)
        self.fperunumeros_label.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.fperunumeros_label.setObjectName("fperunumeros_label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.__connect_signals()

    def __connect_signals(self):
        self.fperubuscardatos_pushButton.clicked.connect(
            self.buscar_peru_datos
        )

    async def async_buscar_peru_datos(self):
        dato_str = self.fperuCelDoc_lineEdit.text().strip()

        self.client_parent.mostrar_mensaje(
            self.freePeruConsole_textBrowser,
            f"Buscando datos relacionados a {dato_str} en peru ...",
        )

        response = await self.client_parent.sdk.api_controller(
            "peru", "dato", dato_str, "free"
        )

        if "error" in response:
            self.client_parent.mostrar_mensaje(
                self.freePeruConsole_textBrowser, response.get("error")
            )
        else:
            output = response.get("sigma_db")
            self.client_parent.mostrar_mensaje(
                self.freePeruConsole_textBrowser,
                f"Se encontraron {len(output)} resultados. Cargando ...",
            )

            for resultado in output:
                rowPosition = self.fperunumeros_tableWidget.rowCount()
                self.fperunumeros_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "documento",
                        "numero",
                    ]
                ):
                    self.fperunumeros_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(resultado, campo)
                        ),
                    )

    def buscar_peru_datos(self):
        while self.fperunumeros_tableWidget.rowCount() > 0:
            self.fperunumeros_tableWidget.removeRow(0)
        if self.fperuCelDoc_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_peru_datos())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("PeruResolver", "Sigma Client - Peru"))
        self.freeperuDashboard_groupBox.setTitle(
            _translate("PeruResolver", "Dashboard")
        )
        self.fperubuscar_label.setText(
            _translate("PeruResolver", "Celular o Documento")
        )
        self.fperubuscardatos_pushButton.setText(
            _translate("PeruResolver", "Buscar datos")
        )
        self.freePeruConsole_textBrowser.setHtml(
            _translate(
                "PeruResolver",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                '<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p></body></html>',
            )
        )
        self.fperubackend_label.setText(
            _translate("PeruResolver", "Backend output")
        )
        self.panelPeru_groupBox.setTitle(
            _translate("PeruResolver", "Panel de datos Peru")
        )
        item = self.fperunumeros_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("PeruResolver", "Documento"))
        item = self.fperunumeros_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("PeruResolver", "Numero"))
        self.fperunumeros_label.setText(
            _translate("PeruResolver", "Numeros de telefono")
        )
