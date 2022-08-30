from PyQt5 import QtCore, QtGui, QtWidgets


class PersonaEntry(QtWidgets.QGroupBox):
    def __init__(self, scrollarea, cuit, nombre, provincia):
        super().__init__(scrollarea)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(0, 100))
        self.setMaximumSize(QtCore.QSize(16777215, 100))
        self.setStyleSheet(
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
            "    background: rgb(39, 39, 46);\n"
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
            "}"
        )
        self.setTitle("")
        self.setObjectName("nombreEntry_groupBox")
        self.pro2NombreyApe_output_lineEdit = QtWidgets.QLineEdit(self)
        self.pro2NombreyApe_output_lineEdit.setGeometry(
            QtCore.QRect(190, 50, 211, 22)
        )
        self.pro2NombreyApe_output_lineEdit.setText(nombre)
        self.pro2NombreyApe_output_lineEdit.setReadOnly(True)
        self.pro2NombreyApe_output_lineEdit.setObjectName(
            "pro2NombreyApe_output_lineEdit"
        )
        self.nombreyApe_label = QtWidgets.QLabel(self)
        self.nombreyApe_label.setText("Nombre y apellido")
        self.nombreyApe_label.setGeometry(QtCore.QRect(190, 30, 111, 16))
        self.nombreyApe_label.setObjectName("nombreyApe_label")
        self.cuit_label = QtWidgets.QLabel(self)
        self.cuit_label.setText("CUIT")
        self.cuit_label.setGeometry(QtCore.QRect(40, 30, 91, 16))
        self.cuit_label.setObjectName("cuit_label")
        self.pro2cuit_output_lineEdit = QtWidgets.QLineEdit(self)
        self.pro2cuit_output_lineEdit.setGeometry(
            QtCore.QRect(40, 50, 121, 22)
        )
        self.pro2cuit_output_lineEdit.setText(cuit)
        self.pro2cuit_output_lineEdit.setReadOnly(True)
        self.pro2cuit_output_lineEdit.setObjectName("pro2cuit_output_lineEdit")
        self.pro2provincia_output_lineEdit = QtWidgets.QLineEdit(self)
        self.pro2provincia_output_lineEdit.setGeometry(
            QtCore.QRect(430, 50, 171, 22)
        )
        self.pro2provincia_output_lineEdit.setText(provincia)
        self.pro2provincia_output_lineEdit.setReadOnly(True)
        self.pro2provincia_output_lineEdit.setObjectName(
            "pro2provincia_output_lineEdit"
        )
        self.provinciaEntry_label = QtWidgets.QLabel(self)
        self.provinciaEntry_label.setText("Provincia")
        self.provinciaEntry_label.setGeometry(QtCore.QRect(430, 30, 51, 16))
        self.provinciaEntry_label.setObjectName("provinciaEntry_label")

        # self.verticalLayout_2.addWidget(self)
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # self.verticalLayout.addWidget(self.scrollArea)
