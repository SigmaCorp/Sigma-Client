import asyncio

from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

from .interface import Ui_MainWindow
from .sdk_python import SigmaSDK
from .international import PeruResolver
from .utils import retrieve_data, is_latest_version, get_changelog
from .entries import PersonaEntry
from .changelog import Changelog

__version__ = "0.6.8"


class SigmaClient(Ui_MainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        self.setupUi(mainwindow)
        self.__connect_signals()
        self.__bloquear_peticiones()
        self.sigma_version_label.setText(f"Sigma Client v{__version__}")
        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Iniciando Sigma Client build v{__version__}",
        )

        self.sdk = None
        self.plan = None
        self.personas_cargadas = []

        self.planes = {
            0: "free",
            1: "profesional",
            2: "medium",
            3: "standard",
            4: "comunidades",
        }

        asyncio.ensure_future(self.checkear_ultima_version())

    def __connect_signals(self):
        self.validarLogin_pushButton.clicked.connect(self.validar_login)
        self.sbuscardatos_pushButton.clicked.connect(
            self.buscar_datos_standard
        )
        self.sbuscartelefono_pushButton.clicked.connect(
            self.buscar_telefonos_standard
        )
        self.buscarPatente_pushButton.clicked.connect(self.buscar_por_patente)
        self.buscarPatentDNI_pushButton.clicked.connect(
            self.buscar_patente_por_dni
        )
        self.proBuscarNum_pushButton.clicked.connect(
            self.buscar_datos_por_numero
        )
        self.proBuscarDni_pushButton.clicked.connect(
            self.buscar_datos_profesional
        )
        self.proBuscarEmail_pushButton.clicked.connect(
            self.buscar_email_movistar
        )
        self.peru_pushButton.clicked.connect(self.cargar_peru_resolver)
        self.argentina_pushButton.clicked.connect(
            self.cargar_argentina_resolver
        )

        self.proBuscarNombre_pushButton.clicked.connect(
            self.buscar_personas_nombre
        )

        self.proBuscarVecinos_pushButton.clicked.connect(
            self.buscar_vecinos_direccion
        )

        self.p3buscarcvuTitular_pushButton.clicked.connect(
            self.buscar_datos_cbu
        )

        self.p3emailBuscar_pushButton.clicked.connect(self.buscar_datos_email)

        self.p3buscarDato_pushButton.clicked.connect(
            self.buscar_datos_numero_p3
        )

        self.CMbuscarDato_pushButton_2.clicked.connect(
            self.community_buscar_num_comun
        )

        self.CMbuscarDato_pushButton.clicked.connect(
            self.community_buscar_num_magic
        )

        self.CMemailBuscar_pushButton.clicked.connect(
            self.community_buscar_email_magic
        )

        self.enviarReporte_pushButton.clicked.connect(self.enviar_reporte)

    def __bloquear_peticiones(self):
        self.sbuscardatos_pushButton.setEnabled(False)
        self.sbuscartelefono_pushButton.setEnabled(False)
        self.buscarPatente_pushButton.setEnabled(False)
        self.buscarPatentDNI_pushButton.setEnabled(False)
        self.proBuscarNum_pushButton.setEnabled(False)
        self.proBuscarDni_pushButton.setEnabled(False)
        self.proBuscarEmail_pushButton.setEnabled(False)
        self.proBuscarNombre_pushButton.setEnabled(False)
        self.proBuscarVecinos_pushButton.setEnabled(False)
        self.argentina_pushButton.setEnabled(False)
        self.peru_pushButton.setEnabled(False)
        self.p3buscarcvuTitular_pushButton.setEnabled(False)
        self.p3emailBuscar_pushButton.setEnabled(False)
        self.p3buscarDato_pushButton.setEnabled(False)
        self.CMbuscarDato_pushButton.setEnabled(False)
        self.CMbuscarDato_pushButton_2.setEnabled(False)
        self.CMemailBuscar_pushButton.setEnabled(False)
        self.enviarReporte_pushButton.setEnabled(False)

    def __habilitar_peticiones_por_plan(self, plan):
        if plan == 4:
            self.CMbuscarDato_pushButton.setEnabled(True)
            self.CMbuscarDato_pushButton_2.setEnabled(True)
            self.CMemailBuscar_pushButton.setEnabled(True)
            self.enviarReporte_pushButton.setEnabled(True)
            return

        self.peru_pushButton.setEnabled(True)
        if plan == 0:
            return

        if plan <= 3:
            self.sbuscardatos_pushButton.setEnabled(True)
            self.sbuscartelefono_pushButton.setEnabled(True)
            self.argentina_pushButton.setEnabled(True)

        if plan <= 2:
            self.buscarPatente_pushButton.setEnabled(True)
            self.buscarPatentDNI_pushButton.setEnabled(True)

        if plan == 1:
            self.proBuscarNum_pushButton.setEnabled(True)
            self.proBuscarDni_pushButton.setEnabled(True)
            self.proBuscarEmail_pushButton.setEnabled(True)
            self.proBuscarNombre_pushButton.setEnabled(True)
            self.proBuscarVecinos_pushButton.setEnabled(True)
            self.p3buscarcvuTitular_pushButton.setEnabled(True)
            self.p3emailBuscar_pushButton.setEnabled(True)
            self.p3buscarDato_pushButton.setEnabled(True)

    def __limpiar_tabla(self, tabla):
        while tabla.rowCount() > 0:
            tabla.removeRow(0)

    def __settear_token(self, token, plan):
        self.sdk = SigmaSDK(token)
        self.plan = plan
        self.__habilitar_peticiones_por_plan(plan)

    def mostrar_mensaje(self, consola, msg: str):
        consola.append(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

    async def checkear_ultima_version(self):
        results = await is_latest_version(__version__)
        if not results[0]:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(
                f"Tu version de Sigma Client es v{__version__} y la version mas reciente es v{results[1]}. Recomendamos que actualices tu cliente para estar al dia con los nuevos resolvers y correciones."
            )
            msg.setWindowTitle("Sigma Client Update")
            msg.buttonClicked.connect(
                lambda: QtGui.QDesktopServices.openUrl(
                    QtCore.QUrl("https://github.com/SigmaCorp/Sigma-Client")
                )
            )
            msg.exec_()

        changelog = await get_changelog()
        self.changelog = Changelog(self, changelog)
        self.changelog.exec_()

    async def async_validar_login(self):
        usuario = self.usuario_lineEdit.text().strip()
        clave = self.password_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.mconsole_textBrowser,
            f"Validando credenciales {usuario}:{clave} ...",
        )
        response = await SigmaSDK.login(usuario, clave)
        if "error" in response:
            self.mostrar_mensaje(
                self.mconsole_textBrowser,
                response.get("mensaje"),
            )
        else:
            self.mostrar_mensaje(
                self.mconsole_textBrowser,
                f"Bienvenido {usuario}! Tu plan es <b>{self.planes[response['plan']]}<b/>",
            )
            self.__settear_token(response["token"], response["plan"])
            self.mostrar_mensaje(
                self.mconsole_textBrowser,
                f"Tu cliente ha sido configurado para utilizar la token {response['token']} y el plan correspondiente.",
            )

    async def async_buscar_datos_standard(self):
        dni_str = self.standarddni_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.standardConsole_textBrowser,
            f"Buscando información del DNI {dni_str} ...",
        )

        endpoint = {
            1: "dni_resolver",
            2: "dni-resolver-medium",
            3: "dni-resolver-standard",
        }[self.plan]

        response = await self.sdk.api_controller(
            endpoint, "dni", dni_str, self.planes[self.plan]
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.standardConsole_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.standardConsole_textBrowser,
                f"Se ha encontrado el DNI {dni_str}, cargando datos ...",
            )

            self.pddni_output_lineEdit.setText(retrieve_data(response, "doc"))
            self.pdtipodoc_output_lineEdit.setText(
                retrieve_data(response, "tipo_doc")
            )
            self.pdapellido_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )
            self.pdnombres_output_lineEdit.setText(
                retrieve_data(response, "nombres")
            )
            self.pdcalle_output_lineEdit.setText(
                retrieve_data(response, "calle")
            )
            self.pdseccion_output_lineEdit.setText(
                retrieve_data(response, "seccion")
            )
            self.pdcircuito_output_lineEdit.setText(
                retrieve_data(response, "circuito")
            )
            self.pdlocalidad_output_lineEdit.setText(
                retrieve_data(response, "localidad")
            )
            self.pdprovincia_output_lineEdit.setText(
                retrieve_data(response, "provincia")
            )
            self.pdcodigopost_output_lineEdit.setText(
                retrieve_data(response, "codigo_postal")
            )

    async def async_buscar_telefonos_standard(self):
        dni_str = self.standarddni_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.standardConsole_textBrowser,
            f"Buscando numeros del DNI {dni_str} ...",
        )

        endpoint = {
            1: "dni_number_resolver",
            2: "dni-number-resolver-medium",
            3: "dni-number-resolver-standard",
        }[self.plan]

        response = await self.sdk.api_controller(
            endpoint, "dni", dni_str, self.planes[self.plan]
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.standardConsole_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.standardConsole_textBrowser,
                f"Se encontraron {len(response)} numeros relacionados al DNI {dni_str}, cargando ...",
            )
            for numero in response:
                rowPosition = self.snumeros_tableWidget.rowCount()
                self.snumeros_tableWidget.insertRow(rowPosition)
                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    0,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "numero")
                    ),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    1,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "empresa")
                    ),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    2,
                    QtWidgets.QTableWidgetItem(retrieve_data(numero, "doc")),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    3,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "nombre")
                    ),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    4,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "localidad")
                    ),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    5,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "provincia")
                    ),
                )

                self.snumeros_tableWidget.setItem(
                    rowPosition,
                    6,
                    QtWidgets.QTableWidgetItem(
                        retrieve_data(numero, "codigo_postal")
                    ),
                )

    async def async_buscar_por_patente(self):
        patente_str = self.patenteBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.mconsoleback_textBrowser,
            f"Buscando registros de la patente {patente_str} ...",
        )

        endpoint = {1: "patente_resolver", 2: "patente-resolver-medium"}[
            self.plan
        ]

        response = await self.sdk.api_controller(
            endpoint, "patente", patente_str, self.planes[self.plan]
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.mconsoleback_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.mconsoleback_textBrowser,
                f"Se encontraron {len(response)} registros relacionados a la patente {patente_str}, cargando ...",
            )
            for registro in response:
                rowPosition = self.patentes_tableWidget.rowCount()
                self.patentes_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "patente",
                        "documento",
                        "vehiculo",
                        "marca",
                        "anio",
                        "titular",
                        "porcentaje",
                        "calle",
                        "altura",
                        "piso",
                        "depto",
                        "codigo_postal",
                        "localidad",
                        "transferencia",
                    ]
                ):
                    self.patentes_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(registro, campo)
                        ),
                    )

    async def async_buscar_patente_por_dni(self):
        dni_str = self.mdnibuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.mconsoleback_textBrowser,
            f"Buscando registros relacionados al DNI {dni_str} ...",
        )

        endpoint = {
            1: "patente_dni_resolver",
            2: "patente-resolver-dni-medium",
        }[self.plan]

        response = await self.sdk.api_controller(
            endpoint, "dni", dni_str, self.planes[self.plan]
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.mconsoleback_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.mconsoleback_textBrowser,
                f"Se encontraron {len(response)} registros relacionados al DNI {dni_str}, cargando ...",
            )
            for registro in response:
                rowPosition = self.patentes_tableWidget.rowCount()
                self.patentes_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "patente",
                        "documento",
                        "vehiculo",
                        "marca",
                        "anio",
                        "titular",
                        "porcentaje",
                        "calle",
                        "altura",
                        "piso",
                        "depto",
                        "codigo_postal",
                        "localidad",
                        "transferencia",
                    ]
                ):
                    self.patentes_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(registro, campo)
                        ),
                    )

    async def async_buscar_datos_por_numero(self):
        numero_str = self.proNumeroBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.proConsole_textBrowser,
            f"Buscando datos relacionados al numero {numero_str} ...",
        )

        response = await self.sdk.api_controller(
            "num_resolver", "num", numero_str, "profesional"
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.proConsole_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.proConsole_textBrowser,
                f"Se encontraron {len(response)} entidades relacionadas al numero {numero_str}, cargando datos ...",
            )

            for entidad in response:
                rowPosition = self.proNumeros_tableWidget.rowCount()
                self.proNumeros_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "celular",
                        "documento",
                        "nombre",
                        "direccion",
                        "localidad",
                        "provincia",
                        "codigo_postal",
                        "empresa",
                    ]
                ):
                    self.proNumeros_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(entidad, campo)
                        ),
                    )

    async def async_buscar_datos_profesional(self):
        dni_str = self.proDniBuscar_lineEdit.text().strip()
        genero_str = self.proGenero_comboBox.currentText()
        self.mostrar_mensaje(
            self.proConsole_textBrowser,
            f"Buscando datos relacionados al dni {dni_str} ...",
        )

        response = await self.sdk.api_controller(
            "dni_resolver_2", "dato", f"{dni_str}:{genero_str}", "profesional"
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.proConsole_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.proConsole_textBrowser,
                f"Se ha encontrado el DNI {dni_str}, cargando datos ...",
            )

            self.proEmision_output_lineEdit.setText(
                retrieve_data(response, "emision")
            )
            self.proNroDoc_output_lineEdit.setText(
                retrieve_data(response, "documento")
            )
            self.proApellido_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )
            self.proNombre_output_lineEdit.setText(
                retrieve_data(response, "nombres")
            )
            self.proCUIL_output_lineEdit.setText(
                retrieve_data(response, "cuil")
            )
            self.proBarrio_output_lineEdit.setText(
                retrieve_data(response, "barrio")
            )
            self.proCalle_output_lineEdit.setText(
                retrieve_data(response, "calle")
            )
            self.proAltura_output_lineEdit.setText(
                retrieve_data(response, "numero")
            )
            self.proDepartamento_output_lineEdit.setText(
                retrieve_data(response, "departamento")
            )
            self.proPiso_output_lineEdit.setText(
                retrieve_data(response, "piso")
            )
            self.proMonoblock_output_lineEdit.setText(
                retrieve_data(response, "monoblock")
            )
            self.proCiudad_output_lineEdit.setText(
                retrieve_data(response, "ciudad")
            )
            self.proMunicipio_output_lineEdit.setText(
                retrieve_data(response, "municipio")
            )
            self.proProvincia_output_lineEdit.setText(
                retrieve_data(response, "provincia")
            )
            self.proPais_output_lineEdit.setText(
                retrieve_data(response, "pais")
            )

            self.proFechaNacimiento_output_lineEdit.setText(
                retrieve_data(response, "fecha_nacimiento")
            )

            fallecimiento = retrieve_data(response, "fallecido")
            if fallecimiento == "Sin Aviso de Fallecimiento":
                fallecimiento = "No"

            self.proFallecido_output_lineEdit.setText(fallecimiento)

            if type(response.get("cobertura")) == list:
                for obrasocial in response.get("cobertura"):
                    self.obraSocial_output_comboBox.addItem(
                        obrasocial["cobertura"]
                    )
            else:
                self.obraSocial_output_comboBox.clear()

    async def async_buscar_email_movistar(self):
        num_str = self.pronum_buscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.proConsole_textBrowser,
            f"Buscando email relacionado al numero {num_str} en movistar ...",
        )

        response = await self.sdk.api_controller(
            "movistar", "num", num_str, "profesional"
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.proConsole_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.proConsole_textBrowser,
                f"Se ha encontrado un email relacionado al numero {num_str}, cargando datos ...",
            )

            self.pronum_output_lineEdit.setText(retrieve_data(response, "num"))
            self.proemail_output_lineEdit.setText(
                retrieve_data(response, "email")
            )

    async def async_buscar_personas_nombre(self):
        nombre_str = self.proNombreBuscar_lineEdit.text().strip()
        provincia_str = self.proProvincia_comboBox.currentText() or None
        localidad_str = self.proLocalidadBuscar_lineEdit.text().strip() or None
        edad_min_str = self.proEdadMin_spinBox.value() or None
        edad_max_str = self.proEdadMax_spinBox.value() or None

        self.mostrar_mensaje(
            self.pro2Console_textBrowser,
            f"Buscando personas con nombre '{nombre_str}' ...",
        )

        response = await self.sdk.buscar_nombre(
            nombre_str,
            provincia_str,
            localidad_str,
            edad_min_str,
            edad_max_str,
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.pro2Console_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.pro2Console_textBrowser,
                f"Se encontraron {len(response)} resultados, cargando ...",
            )

            for persona in response:

                entry = PersonaEntry(
                    self.scrollArea,
                    persona["documento"],
                    persona["nombre"],
                    persona["provincia"],
                )
                self.verticalLayout_2.addWidget(entry)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                self.verticalLayout.addWidget(self.scrollArea)
                self.personas_cargadas.append(entry)

    async def async_buscar_vecinos_direccion(self):
        direccion_str = self.proDireccionBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.pro2Console_textBrowser,
            f"Buscando vecinos en {direccion_str} ...",
        )

        response = await self.sdk.api_controller(
            "buscar_vecinos", "direccion", direccion_str, "profesional"
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.pro2Console_textBrowser, response.get("error")
            )
        else:
            self.mostrar_mensaje(
                self.pro2Console_textBrowser,
                f"Se encontraron {len(response)} vecinos en {direccion_str}, cargando datos ...",
            )

            for vecino in response:
                rowPosition = self.proVecinos_tableWidget.rowCount()
                self.proVecinos_tableWidget.insertRow(rowPosition)
                for indice, campo in enumerate(
                    [
                        "doc",
                        "nombre",
                        "numero",
                        "empresa",
                        "direccion",
                        "localidad",
                        "provincia",
                        "codigo_postal",
                    ]
                ):
                    self.proVecinos_tableWidget.setItem(
                        rowPosition,
                        indice,
                        QtWidgets.QTableWidgetItem(
                            retrieve_data(vecino, campo)
                        ),
                    )

    async def async_buscar_datos_cbu(self):
        cbv_or_alias_str = self.p3cbvubuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.pro3Console_textBrowser,
            f"Buscando datos del titular de {cbv_or_alias_str} ...",
        )

        response = await self.sdk.magic_endpoint(
            cbv_or_alias_str, "buscar_cbu_alias"
        )

        if "error" in response:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser,
                f"Se encontraron datos del titular de {cbv_or_alias_str}, cargando ...",
            )

            self.p3titular_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3cuit_output_lineEdit.setText(
                retrieve_data(response, "cuit")
            )
            self.p3banco_output_lineEdit.setText(
                retrieve_data(response, "banco")
            )
            self.p3tipocuenta_output_lineEdit.setText(
                retrieve_data(response, "cuenta_tipo")
            )
            self.p3cbucvu_output_lineEdit.setText(
                retrieve_data(response, "cbu")
            )

    async def async_buscar_datos_email(self):
        email_str = self.p3emailBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.pro3Console_textBrowser,
            f"Buscando datos de email {email_str} ...",
        )

        response = await self.sdk.magic_endpoint(email_str, "buscar_email")

        if "error" in response:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser,
                f"Se encontraron datos del email {email_str}, cargando ...",
            )

            self.p3nombres_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3apellido_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )

    async def async_buscar_datos_numero_p3(self):
        numero_str = self.p3numeroBuscar_lineEdit.text().strip()
        self.mostrar_mensaje(
            self.pro3Console_textBrowser,
            f"Buscando datos del numero {numero_str} ...",
        )

        response = await self.sdk.magic_endpoint(numero_str, "buscar_celular")

        if "error" in response:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser, response.get("mensaje")
            )
        else:
            self.mostrar_mensaje(
                self.pro3Console_textBrowser,
                f"Se encontraron datos del numero {numero_str}, cargando ...",
            )

            self.p3nombres2_output_lineEdit.setText(
                retrieve_data(response, "nombre")
            )
            self.p3apellidos2_output_lineEdit.setText(
                retrieve_data(response, "apellido")
            )
            self.p3email_output_lineEdit.setText(
                retrieve_data(response, "email")
            )
            self.p3numero_output_lineEdit.setText(
                retrieve_data(response, "numero")
            )

    async def async_community_search(self, data, method):
        endpoint = {
            "num_arg": "/api/sigma/comunidades/hack4u/num_resolver/argentina",
            "magic": "/api/sigma/comunidades/hack4u/magic_resolver/argentina",
        }[method]

        self.mostrar_mensaje(
            self.CMConsole_textBrowser,
            f"Buscando {data} ...",
        )

        response = await self.sdk.hack4u_community(data, endpoint)

        if "error" in response:
            self.mostrar_mensaje(self.CMConsole_textBrowser, response)
        else:
            if method == "num_arg":
                self.CMdocumento_output_lineEdit.setText(
                    retrieve_data(response, "documento")
                )
                self.CMnombre_output_lineEdit.setText(
                    retrieve_data(response, "nombre")
                )
                self.CMdireccion_output_lineEdit.setText(
                    retrieve_data(response, "direccion")
                )
                self.CMlocalidad_output_lineEdit.setText(
                    retrieve_data(response, "localidad")
                )
                self.CMprovincia_output_lineEdit.setText(
                    retrieve_data(response, "provincia")
                )
                self.CMcodigopostal_output_lineEdit.setText(
                    retrieve_data(response, "codigo_postal")
                )
                self.CMempresa_output_lineEdit.setText(
                    retrieve_data(response, "empresa")
                )
            else:
                if data["tipo"] == "buscar_celular":
                    self.CMnombres2_output_lineEdit.setText(
                        retrieve_data(response, "nombre")
                    )
                    self.CMapellidos2_output_lineEdit.setText(
                        retrieve_data(response, "apellido")
                    )
                    self.CMemail_output_lineEdit.setText(
                        retrieve_data(response, "email")
                    )
                    self.CMnumero_output_lineEdit.setText(
                        retrieve_data(response, "numero")
                    )
                else:
                    self.CMnombres_output_lineEdit.setText(
                        retrieve_data(response, "nombre")
                    )
                    self.CMapellido_output_lineEdit.setText(
                        retrieve_data(response, "apellido")
                    )

    async def async_enviar_reporte(self):
        data = {
            "id_discord": self.discordid_lineEdit.text().strip(),
            "tipo_vuln": self.tipoVulnerabilidad_comboBox.currentIndex(),
            "asset": self.recurso_comboBox.currentIndex(),
            "impacto_criticidad": self.nivelImpacto_comboBox.currentIndex(),
            "titulo": self.tituloreporte_lineEdit.text().strip(),
            "reproduce": self.descripcionreporte_plainTextEdit.toPlainText().strip(),
            "impacto": self.impactoreporte_plainTextEdit.toPlainText().strip(),
        }

        response = await self.sdk.hack4u_community(
            data, "/api/sigma/comunidades/bug-bounty"
        )

        if response == 200:
            self.mostrar_mensaje(
                self.reports_textBrowser, "Tu reporte ha sido enviado!"
            )
        elif response == 429:
            self.mostrar_mensaje(
                self.reports_textBrowser,
                "Estas rate limiteado, por favor espera 30 minutos antes de enviar un nuevo reporte.",
            )
        else:
            self.mostrar_mensaje(
                self.reports_textBrowser,
                "No se pudo enviar tu reporte, intentelo mas tarde.",
            )

    def validar_login(self):
        self.__bloquear_peticiones()
        if (
            self.usuario_lineEdit.text().strip()
            and self.password_lineEdit.text().strip()
        ):
            asyncio.ensure_future(self.async_validar_login())

    def buscar_datos_standard(self):
        if self.standarddni_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_standard())

    def buscar_telefonos_standard(self):
        self.__limpiar_tabla(self.snumeros_tableWidget)
        if self.standarddni_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_telefonos_standard())

    def buscar_por_patente(self):
        self.__limpiar_tabla(self.patentes_tableWidget)
        if self.patenteBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_por_patente())

    def buscar_patente_por_dni(self):
        self.__limpiar_tabla(self.patentes_tableWidget)
        if self.mdnibuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_patente_por_dni())

    def buscar_datos_por_numero(self):
        self.__limpiar_tabla(self.proNumeros_tableWidget)
        if self.proNumeroBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_por_numero())

    def buscar_datos_profesional(self):
        if self.proDniBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_profesional())

    def buscar_email_movistar(self):
        if self.pronum_buscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_email_movistar())

    def buscar_personas_nombre(self):
        if self.personas_cargadas:
            while self.verticalLayout_2.count():
                child = self.verticalLayout_2.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
            self.personas_cargadas = []
        if self.proNombreBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_personas_nombre())

    def buscar_vecinos_direccion(self):
        self.__limpiar_tabla(self.proVecinos_tableWidget)
        if self.proDireccionBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_vecinos_direccion())

    def buscar_datos_cbu(self):
        if self.p3cbvubuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_cbu())

    def buscar_datos_email(self):
        if self.p3emailBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_email())

    def buscar_datos_numero_p3(self):
        if self.p3numeroBuscar_lineEdit.text().strip():
            asyncio.ensure_future(self.async_buscar_datos_numero_p3())

    def community_buscar_num_comun(self):
        if self.CMnumeroBuscar_lineEdit_2.text().strip():
            data = {"num": self.CMnumeroBuscar_lineEdit_2.text().strip()}
            asyncio.ensure_future(self.async_community_search(data, "num_arg"))

    def community_buscar_num_magic(self):
        if self.CMnumeroBuscar_lineEdit.text().strip():
            data = {
                "dato": self.CMnumeroBuscar_lineEdit.text().strip(),
                "tipo": "buscar_celular",
            }
            asyncio.ensure_future(self.async_community_search(data, "magic"))

    def community_buscar_email_magic(self):
        if self.CMemailBuscar_lineEdit.text().strip():
            data = {
                "dato": self.CMemailBuscar_lineEdit.text().strip(),
                "tipo": "buscar_email",
            }
            asyncio.ensure_future(self.async_community_search(data, "magic"))

    def enviar_reporte(self):
        if (
            not self.discordid_lineEdit.text().strip()
            or not self.tituloreporte_lineEdit.text().strip()
        ):
            return

        for field in [
            self.descripcionreporte_plainTextEdit,
            self.impactoreporte_plainTextEdit,
        ]:
            if not field.toPlainText().strip():
                return

        for field in [
            self.tipoVulnerabilidad_comboBox,
            self.recurso_comboBox,
            self.nivelImpacto_comboBox,
        ]:
            if field.currentIndex() == 0:
                return

        asyncio.ensure_future(self.async_enviar_reporte())

    def cargar_peru_resolver(self):
        if hasattr(self, "peruResolver"):
            if self.peruResolver is not None:
                self.peruResolver.setFocus(True)
                self.peruResolver.activateWindow()
                self.peruResolver.raise_()
                self.peruResolver.show()
                return
        self.peruResolver = PeruResolver(self)
        self.peruResolver.show()

    def cargar_argentina_resolver(self):
        self.tabWidget.setCurrentIndex(1)
