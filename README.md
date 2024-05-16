<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://static.magneto365.com/lib/assets/cef805bdf449b93b.svg" alt="Logo" style = "background-color:white" width = "400px">
  </a>

  <h3 align="center">SISTEMA DE GESTIÓN DE GRUPOS DE EMPLEABILIDAD</h3>
  <p>SISTEMAS DE INFORMACIÓN</p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenidos</summary>
  <ol>
    <li><a href="#sobre-el-proyecto">Sobre el proyecto</a></li>
    <li><a href="#herramientas-con-las-que-se-desarrolló">Herramientas con las que se desarrolló</a></li>
    <li><a href="#instalación">Instalación</a></li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#autores">Autores</a></li>
    <li><a href="#reconocimientos">Reconocimientos</a></li>
  </ol>
</details>


## Sobre el proyecto
### Problemática

El problema identificado en este proceso radica principalmente en la cantidad significativa de actividades manuales requeridas por parte de [Magneto](https://www.magneto365.com/es) en el envio de vacantes laborales a grupos de empleabilidad en distintas plataformas . La clasificación de vacantes debe realizarse manualmente debido a errores en el sistema, lo que conlleva un porcentaje de vacantes mal clasificadas o no geográficamente asignadas correctamente. Además, se necesita una verificación manual para evitar la duplicación de publicaciones en los grupos de WhatsApp. A esto se suma la creación manual de mensajes, gráficos y UTM para las publicaciones y el envio de todo lo mencionado anteriormente a los grupos en las distintas plataformas.

El proceso actual, que depende en gran medida de la intervención humana, no permite una gestión eficiente de los grupos de empleo. Por lo tanto, hemos identificado la necesidad de automatizar la clasificación de vacantes según el sector productivo y su asignación a los grupos de empleo correspondientes, asegurando la diversidad del contenido y evitando repeticiones. Además, el uso exclusivo de WhatsApp como plataforma de difusión limita el alcance a personas que utilizan otras herramientas en su vida diaria.

### Solución
En el proyecto de automatización de grupos de empleabilidad, a través de la plataforma n8n, se logró automatizar el envío y clasificación de vacantes laborales a grupos de empleabilidad en Telegram. Esto permitió a Magneto, como organización, alcanzar a 9,276 personas adicionales en ciudades como Barranquilla, Bogotá, Cartagena, Santa Marta, Medellín e Ibagué, a través de mensajes llamativos que captan la atención de las personas para aplicar a oportunidades laborales. Anteriormente, esta información no llegaba a esta cantidad de personas debido a que Magneto no utilizaba Telegram para compartir vacantes laborales.

Además, se priorizó la escalabilidad en el flujo, lo que permite utilizarlo en el futuro para enviar vacantes laborales a otras plataformas, como WhatsApp, entre otros. De esta manera, Magneto puede enviar un conjunto de vacantes críticas al flujo creado, el cual se encargará de clasificarlas y enviarlas a la plataforma correspondiente según el sector especificado y los grupos asociados al mismo. Esto elimina la necesidad de que las personas realicen esta acción manualmente, ahorrando tiempo y recursos.

También se implementó en el sistema la gestión de notificaciones sobre los envíos de vacantes laborales mencionados anteriormente, para así, mantener informado al administrador sobre envíos exitosos y con fallos, siendo esto funcional y escalable para las distintas plataformas que se planeen implementar en un futuro.

Por último, se dejó una documentación completa sobre el funcionamiento del flujo, credenciales,  pasos necesarios para utilizar el flujo, y parámetros sobre cómo escalar el mismo para las distintas plataformas.



**Imagen del flujo creado en n8n:**
<div align = "center">
  <img src = "https://i.imgur.com/bTF9TqI.png"/> 
</div>

**Imagen de envio real por parte de Magneto de una vacante laboral de manera automatizada a grupos de empleabilidad existentes con lo implementado:**
<div align = "center">
  <img src = "https://i.imgur.com/Uzpdv8h.png"/> 
</div>

**Imagen de base de datos con grupos de empleabilidad ofrecidos a la organización, con más de 9276 personas vinculadas:**
<div align = "center">
  <img src = "https://i.imgur.com/0a7eOZE.png"/> 
</div>


## Herramientas implicadas en el desarrollo
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,github,git" />
    <img src = "https://img.godotassetlibrary.com/K_2VqYVfAzYw-kw2ZOukZlCF6_GT9-8phSzRgYpY6QE/rs:fit:1920:1080:0/g:no/aHR0cHM6Ly91cGxvYWQud2lraW1lZGlhLm9yZy93aWtpcGVkaWEvY29tbW9ucy84LzgyL1RlbGVncmFtX2xvZ28uc3Zn.webp" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "telegram"/>
    <img src = "https://avatars.githubusercontent.com/u/45487711?s=200&v=4" width = 48px style = "border-radius:10px;margin-inline:3px" alt = "n8n"/>
  </a>
</p>

## Instalación
1. Agregar el flujo de n8n al workspace, para ello, se descarga el archivo JSON de [automation-employability-groups](https://github.com/kristianrpo/automation-employability-groups/blob/main/n8n/automation_employability_groups_RPA.json), y se importa dentro de un flujo en la plataforma
2. Seguir los pasos especificados como [pre-requisitos](https://github.com/kristianrpo/automation-employability-groups/blob/main/docs/Documentation.md#pre-requisitos-para-funcionamiento) en la documentación de todo el proyecto para dejar el flujo de n8n totalmente funcional.
3. Asegúrate de tener instalado Python en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
4. Clonar el proyecto 
```bash
  git clone https://github.com/kristianrpo/automation-employability-groups.git
```
5. Configurar el entorno virtual, navegando hasta el directorio y aplicando el comando correspondiente para el funcionamiento del mismo.
```bash
  cd automation-employability-groups
  python -m venv venv 
```
6. Activar el entorno virtual creado con el comando correspondiente
```bash
  ./venv/Scripts/activate
```
7. Instalar dependencias para el correcto funcionamiento del proyecto
```bash
  pip install -r requirements.txt
```
8. Ejecutar la aplicacion de FastAPI
```bash
  uvicorn main:app --reload
```
9. Ahora el flujo de n8n puede conectarse al endpoint para permitir el envio de vacantes laborales a la plataforma de Telegram y futuras implementaciones.
## Uso
A el endpoint generado por n8n, se envía un conjunto de vacantes laborales criticas a enviar a ciertas plataformas, con una serie atirbutos necesarios sobre dicha vacante, especificados en la documentación.

Posteriormente, el flujo de n8n se encargará de procesar dicha vacante y segun un sector ID asociado y una plataforma, hace la clasificacion correspondiente y el envio de los datos necesarios al endpoint en FAST API.

El endpoint de FASTAPI recibe los datos, y hace el uso de las diferentes APIS de las diferentes plataformas para hacer el envío de la vacante al grupo correcto.

## Autores
El proyecto fué realizado por Kristian Restrepo Osorio, Luisa María Álvarez García, Miguel Ángel Martínez García y Sebastian Restrepo Ortiz.
