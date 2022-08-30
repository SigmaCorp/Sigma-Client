# Sigma Client
Sigma Client es una herramienta gráfica que facilita la interacción con la API de [Sigma Search](https://sigma-search.io) y muestra los datos de forma más organizada para el usuario. El software es **Open Source**, lo que garantiza la transparencia y confiabilidad del programa.

<p align="center">
  <img src="https://user-images.githubusercontent.com/74129955/185270717-b02838cf-d58b-4f37-a9f7-322263561e36.png" />
</p>

## Características
- Login a través de usuario y contraseña
- Acceso a todos los endpoints de Sigma Search
- Interfaz gráfica para los resultados
- Automaticamente utiliza los endpoints correspondientes al plan de la cuenta

## Screenshots
![client](https://user-images.githubusercontent.com/74129955/186548490-7d56e396-976b-4e6c-9bbc-3ee2c4762c32.png)


## Requerimientos
```console
aiohttp==3.7.4.post0
PyQt5==5.15.7
```

## Instalación
### Binarios precompilados
Para utilizar este programa se pueden descargar los binarios precompilados disponibles para [Linux](https://github.com/SigmaCorp/Sigma-Client/releases/download/v0.6.8/Sigma_client_linux_amd64_v0.6.8.release) y [Windows](https://github.com/SigmaCorp/Sigma-Client/releases/download/v0.6.8/Sigma_client_windows_amd64_v0.6.8.exe)

**Latest release:** https://github.com/SigmaCorp/Sigma-Client/releases/tag/v0.6.8

### Source
También se puede clonar el repositorio y correr el programa desde el script *app.py*
```console
git clone https://github.com/SigmaCorp/Sigma-Client
cd Sigma-Client
pip install -r requirements.txt
python app.py
```

## Creditos
Todos los derechos reservados por Sigma Corporation.
