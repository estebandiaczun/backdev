#API test from Esteban 1.0.0
***

API test from Esteban es una API desarrollada sobre Python 2.7.18 para el alta y baja de usuarios en una aplicacion web.

### HOW TO DOWNLOAD ###
* Ejecutar comando git clone https://github.com/estebandiaczun/Proyecto-Scraping-Flask/tree/main <Directorio en el que se va a descargar>

 esto te va a descargar la carpeta del repositorio.

## HOW TO INSTALL ##
* Este proyecto fue creado sobre un entorno virtual asi que para su correcto funcionamiento seguir los pasos 

 ejecutar comando $ pip install virtualenv para instalar la herramienta virtualenv (virtualenv es una herramienta que se utiliza para crear entornos Python aislados. )

 para verificar la correcta instalacion $ virtualenv --version

 para la creacion del entorno usar $ python3 -m venv EJEMPLO (DEBE remplazar EJEMPLO por el nombre que le quiera poner a su entorno virtual)

 para entrar en el creado usar $ source EJEMPLO/bin/activate 

 podra salir usando $ deactivate 

* Para instalar todas las dependencias utilizadas en este proyecto utilizar el comando $ pip install -r requirements.txt

## RUN API ##
* Para ejecutar esta API debera iniciar un servidor local utilizando Uvicorn previamente instalado para ello ejecutar

$ uvicorn main:app --reload

con el server ya levantado podra ingresar a la siguiente direccion en el navegador:

http://127.0.0.1:8000/ apareciendo en pantalla el mensaje "Hola mundito"

* Los endpoints y mas documentacion estaran en: 

    http://127.0.0.1:8000/docs






 

 




