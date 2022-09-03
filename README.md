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
![image](https://user-images.githubusercontent.com/74129955/188284886-b2671f7d-7ee3-4368-ae8c-20d21f5ed483.png)
![image](https://user-images.githubusercontent.com/74129955/188284918-9becaf63-8eee-4416-9255-a344f1f1108f.png)
![image](https://user-images.githubusercontent.com/74129955/188284963-665fccaa-de20-4a43-ba46-651312d42419.png)
![image](https://user-images.githubusercontent.com/74129955/188284977-37d8b753-9331-436d-aba8-d44425d32d00.png)
![image](https://user-images.githubusercontent.com/74129955/188285007-d9b511f3-d832-47af-95de-1012f9586fe8.png)
![image](https://user-images.githubusercontent.com/74129955/188285018-3376c30b-68a3-4b92-8f6d-9f779b4c6fa6.png)
![image](https://user-images.githubusercontent.com/74129955/188285032-cca8e792-0d54-4218-bcd0-f737e08235c9.png)



## Requerimientos
```console
aiohttp==3.7.4.post0
PyQt5==5.15.7
```

## Instalación
### Binarios precompilados
Para utilizar este programa se pueden descargar los binarios precompilados disponibles para [Linux](https://github.com/SigmaCorp/Sigma-Client/releases/download/v0.7.0/Sigma_client_linux_amd64_v0.7.0) y [Windows](https://github.com/SigmaCorp/Sigma-Client/releases/download/v0.7.0/Sigma_client_windows_amd64_v0.7.0.exe)

**Latest release:** https://github.com/SigmaCorp/Sigma-Client/releases/tag/v0.7.0

### Compilacion
Se puede compilar en un ejecutable utilizando `PyInstaller`
```console
git clone https://github.com/SigmaCorp/Sigma-Client
cd Sigma-Client/devtools
pyinstaller build_sigma.spec
```

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
