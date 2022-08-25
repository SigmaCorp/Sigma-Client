import uuid
import platform
import aiohttp
import asyncio
import base64

__version__ = "0.6.2"


class SigmaSDK:
    def __init__(self, sigma_token):
        self.sigma_token = sigma_token
        self.map_endpoints = {
            "endpoints": {
                "profesional": {
                    "movistar": {
                        "endpoint": "/api/sigma/profesional/movistar-resolver",
                        "data_post": {"num": None},
                    },
                    "patente_resolver": {
                        "endpoint": "/api/sigma/profesional/patente-resolver",
                        "data_post": {"patente": None},
                    },
                    "patente_dni_resolver": {
                        "endpoint": "/api/sigma/profesional/patente-dni-resolver",
                        "data_post": {"dni": None},
                    },
                    "dni_resolver": {
                        "endpoint": "/api/sigma/profesional/dni-resolver",
                        "data_post": {"dni": None},
                    },
                    "dni_number_resolver": {
                        "endpoint": "/api/sigma/profesional/dni-number-resolver",
                        "data_post": {"dni": None},
                    },
                    "dni_resolver_2": {
                        "endpoint": "/api/sigma/profesional/dni-resolver-2",
                        "data_post": {"dni": None},
                    },
                    "num_resolver": {
                        "endpoint": "/api/sigma/profesional/num_resolver",
                        "data_post": {"num": None},
                    },
                    "buscar_persona": {
                        "endpoint": "/api/sigma/profesional/nombre-resolver",
                        "data_post": {"nombre": None},
                    },
                    "buscar_vecinos": {
                        "endpoint": "/api/sigma/profesional/address-info",
                        "data_post": {"direccion": None},
                    },
                },
                "medium": {
                    "patente-resolver-medium": {
                        "endpoint": "/api/sigma/medium/patente-resolver-medium",
                        "data_post": {"patente": None},
                    },
                    "patente-resolver-dni-medium": {
                        "endpoint": "/api/sigma/medium/patente-resolver-dni-medium",
                        "data_post": {"dni": None},
                    },
                    "dni-number-resolver-medium": {
                        "endpoint": "/api/sigma/medium/dni-number-resolver-medium",
                        "data_post": {"dni": None},
                    },
                    "dni-resolver-medium": {
                        "endpoint": "/api/sigma/medium/dni-resolver-medium",
                        "data_post": {"dni": None},
                    },
                },
                "standard": {
                    "dni-number-resolver-standard": {
                        "endpoint": "/api/sigma/standard/dni-number-resolver-standard",
                        "data_post": {"dni": None},
                    },
                    "dni-resolver-standard": {
                        "endpoint": "/api/sigma/standard/dni-resolver-standard",
                        "data_post": {"dni": None},
                    },
                },
                "free": {
                    "peru": {
                        "endpoint": "/api/sigma/free/peru-resolver-telefonos",
                        "data_post": {"dato": None},
                    }
                },
            }
        }

    async def api_controller(self, method, tipo_dato, dato, plan):
        async with aiohttp.ClientSession() as session:
            try:
                self.map_endpoints["endpoints"][plan][method]["data_post"][
                    tipo_dato
                ] = dato
                post_data = self.map_endpoints["endpoints"][plan][method][
                    "data_post"
                ]

                headers = SigmaSDK.get_telemetry_headers(
                    token=self.sigma_token
                )
                headers["sigma-key"] = self.sigma_token
                async with session.post(
                    f"https://sigma-search.io{self.map_endpoints['endpoints'][plan][method]['endpoint']}",
                    json=post_data,
                    headers=headers,
                ) as response:
                    return await response.json()
            except:
                raise Exception(
                    "Alguno de los parametros que ingresaste son incorrectos o estas rate-limited"
                )

    async def dni_resolver_profesional(self, dni, genero):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(token=self.sigma_token)
            headers["sigma-key"] = self.sigma_token
            data = {"dni": dni, "sexo": genero}
            try:
                async with session.post(
                    f"https://sigma-search.io/api/sigma/profesional/dni-resolver-2",
                    json=data,
                    headers=headers,
                ) as response:
                    return await response.json()
            except:
                raise Exception(
                    "Alguno de los parametros que ingresaste son incorrectos o estas rate-limited"
                )

    async def buscar_nombre(
        self,
        nombre,
        provincia=None,
        localidad=None,
        edad_min=0,
        edad_max=0,
    ):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(token=self.sigma_token)
            headers["sigma-key"] = self.sigma_token

            data = {"nombre": nombre}
            if provincia:
                data["provincia_nombre"] = provincia
            if localidad:
                data["localidad"] = localidad
            if edad_min:
                data["edad_desde"] = edad_min
            if edad_max:
                data["edad_hasta"] = edad_max

            try:
                async with session.post(
                    f"https://sigma-search.io/api/sigma/profesional/nombre-resolver",
                    json=data,
                    headers=headers,
                ) as response:
                    return await response.json()
            except:
                raise Exception(
                    "Alguno de los parametros que ingresaste son incorrectos o estas rate-limited"
                )

    async def magic_endpoint(self, dato, metodo):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(token=self.sigma_token)
            headers["sigma-key"] = self.sigma_token
            data = {"dato": dato, "tipo": metodo}
            try:
                async with session.post(
                    f"https://sigma-search.io/api/sigma/profesional/magic-resolver",
                    json=data,
                    headers=headers,
                ) as response:
                    return await response.json()
            except:
                raise Exception(
                    "Alguno de los parametros que ingresaste son incorrectos o estas rate-limited"
                )

    async def hack4u_community(self, data, endpoint):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(token=self.sigma_token)
            headers["sigma-key"] = self.sigma_token
            try:
                async with session.post(
                    f"https://sigma-search.io{endpoint}",
                    json=data,
                    headers=headers,
                ) as response:
                    if endpoint == "/api/sigma/comunidades/bug-bounty":
                        return response.status
                    return await response.json()
            except:
                raise Exception(
                    "Alguno de los parametros que ingresaste son incorrectos o estas rate-limited"
                )

    @staticmethod
    async def login(username, password):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(username=username)
            data = {"username": username, "password": password}
            try:
                async with session.post(
                    f"https://sigma-search.io/api/sigma/client/login",
                    json=data,
                    headers=headers,
                ) as response:
                    return await response.json()
            except KeyError or TypeError:
                raise Exception(
                    "Las credenciales son invalidas o estas rate-limited"
                )

    @staticmethod
    def get_telemetry_headers(username: str = None, token: str = None):
        tracking = {
            "os": platform.platform(),
            "hostname": platform.node(),
        }

        if username:
            tracking["username"] = username

        if token:
            tracking["token"] = token

        b64_str = base64.b64encode(str(tracking).encode()).decode("utf-8")
        return {"x-sigma": b64_str}
