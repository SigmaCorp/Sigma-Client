import uuid
import platform
import aiohttp
import asyncio
import base64
import json

from typing import Dict, Any, ClassVar

__version__ = "0.6.2"


class Route:
    BASE: ClassVar[str] = "https://sigma-search.io/api/v2"

    def __init__(self, method: str, path: str, **parameters: Any) -> None:
        self.method: str = method
        self.path: str = path
        self.url: str = self.BASE + self.path

        if parameters:
            self.url = self.url.format_map(parameters)


class SigmaSDK:
    PLANES: Dict[int, str] = {
        0: "free",
        1: "profesional",
        2: "medium",
        3: "standard",
        4: "comunidades",
    }

    def __init__(self, token: str, plan: int) -> None:
        self.__session: aiohttp.ClientSession = None
        self.user_agent: str = "Sigma SDK v0.2.0 Client Special Release"
        self.token: str = token
        self.plan: int = self.PLANES[plan]

    async def request(self, route: Route, **kwargs: Any) -> Any:
        url = route.url
        method = route.method
        headers: Dict[str, str] = {
            "User-Agent": self.user_agent,
            "sigma-key": self.token,
        }

        if "json" in kwargs:
            headers["Content-Type"] = "application/json"
            kwargs["data"] = json.dumps(kwargs.pop("json"))

        kwargs["headers"] = headers

        async with self.__session.request(method, url, **kwargs) as res:
            try:
                response = await res.json()
            except:
                return {"error": "internal client error"}

        return response

    def reopen_session(self) -> None:
        if self.__session.closed:
            self.__session = aiohttp.ClientSession()

    def buscar_dni(self, dni: str):
        data = {"dni": dni}
        return self.request(
            Route("POST", f"/{self.plan}/osint/argentina/resolver/dni"),
            json=data,
        )

    def buscar_num_por_dni(self, dni: str):
        data = {"dni": dni}
        return self.request(
            Route(
                "POST", f"/{self.plan}/osint/argentina/resolver/dni_celular"
            ),
            json=data,
        )

    def buscar_patente(self, patente: str):
        data = {"patente": patente}
        return self.request(
            Route("POST", f"/{self.plan}/osint/argentina/resolver/patente"),
            json=data,
        )

    def buscar_patente_por_dni(self, dni: str):
        data = {"dni": dni}
        return self.request(
            Route(
                "POST", f"/{self.plan}/osint/argentina/resolver/patente_dni"
            ),
            json=data,
        )

    def buscar_email_movistar(self, num: str):
        data = {"num": num}
        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/movistar"),
            json=data,
        )

    def buscar_por_celular(self, num: str):
        data = {"num": num}
        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/celular"),
            json=data,
        )

    def buscar_por_direccion(self, direccion: str):
        data = {"direccion": direccion}
        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/direccion"),
            json=data,
        )

    def buscar_por_nombre(
        self,
        nombre: str,
        provincia: str = None,
        localidad: str = None,
        edad_min: int = 0,
        edad_max: int = 0,
    ):
        data = {"nombre": nombre}
        if provincia:
            data["provincia_nombre"] = provincia
        if localidad:
            data["localidad"] = localidad
        if edad_min:
            data["edad_desde"] = edad_min
        if edad_max:
            data["edad_hasta"] = edad_max

        print(data)

        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/nombre"),
            json=data,
        )

    def buscar_por_dni_pro(self, dni_genero: str):
        data = {"dato": dni_genero}
        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/dni_two"),
            json=data,
        )

    def magic_resolver(self, dato: str, metodo: str):
        data = {"dato": dato, "tipo": metodo}
        return self.request(
            Route("POST", f"/profesional/osint/argentina/resolver/magic"),
            json=data,
        )

    def data_breach_search(self, query: str):
        data = {"query": query}
        return self.request(
            Route(
                "POST",
                f"/profesional/osint/argentina/search_engine/data_breach",
            ),
            json=data,
        )

    def buscar_peru_persona(self, dato: str):
        data = {"dato": dato}
        return self.request(
            Route(
                "POST",
                f"/free/osint/peru/resolver/celular_dni",
            ),
            json=data,
        )

    async def close_session(self) -> None:
        if self.__session:
            await self.__session.close()

    async def create_session(self) -> None:
        self.__session = aiohttp.ClientSession()

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

    async def hack4u_community(self, data, endpoint):
        async with aiohttp.ClientSession() as session:
            headers = SigmaSDK.get_telemetry_headers(token=self.token)
            headers["sigma-key"] = self.token
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
