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
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#pre-requisitos-para-funcionamiento"> Pre-requisitos</a></li>
    <li><a href="#explicación-de-flujo-general">Explicación flujo</a></li>
    <li><a href="#configuracion-de-endpoint">Endpoint</a></li>
    <li><a href="#escalabilidad">Escalibilidad</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Pre-requisitos para funcionamiento
Para empezar el correcto funcionamiento del flujo es necesario realizar las siguientes acciones:

### Conexión con base de tatos de EXCEL
Es necesario **vincular la base de datos de Excel con los grupos de empleabilidad en el flujo**, para esto:
1. Se selecciona el nodo 'Database', el cual se encarga de conectarse con la base de datos y obtener la informacion de la tabla con los grupos de empleabilidad.

<div align = "center">
<img src = "https://i.imgur.com/19BBCOu.png"/> 
</div>

2. En la interfaz que se abre, se selecciona la opcion de **seleccionar una credencial**, la cual corresponderá a la cuenta de Microsoft que contenga el Excel de la base de datos.

<div align = "center">
<img src = "https://i.imgur.com/557P07T.png"/> 
</div>

3. Una vez conectada la credencial de Microsoft, es necesario elegir que el recurso que se va a obtener de dicho excel es una **tabla**, la cual contiene la informacion de los grupos de empleabilidad

<div align = "center">
<img src = "https://i.imgur.com/aeUlI9q.png"/> 
</div>

4. Posteriormente, se selecciona la operacion que se va a realizar sobre la table, en este caso, obtener cada una de las filas de la misma
<div align = "center">
<img src = "https://i.imgur.com/qun8dnf.png"/> 
</div>

5. Una vez establecida la operacion, se selecciona el archivo de excel que representa la base de datos, se escoge la hoja en que se encuentra la tabla, y se escoge la tabla existente sobre esa hoja de Excel en especifico.
<div align = "center">
<img src = "https://i.imgur.com/fGBhqlM.png"/> 
</div>


### Conexión con API de Telegram
Para conectar una sesión de Telegram con el flujo para el envío de mensajes sin el uso de un BOT de Telegram, se debe hacer de la cuenta del encargado en enviar los mensajes un tipo de "BOT", teniendo una sesión abierta de la conexion de la API de telegram, y esta se encarga de hacer los envios. para esto, debemos:

1. Debemos obtener el API ID y API HASH que va a estar vinculado con una sesión en nuestra cuenta, para esto, creamos una aplicacion en la [página oficial de Telegram](https://my.telegram.org/auth?to=apps). Primeramente iniciando sesión en la plataforma con el numero de quien será encargado de mandar las vacantes laborales 

<div align = "center">
<img src = "https://i.imgur.com/uiTVXS8.png"/> 
</div>

2. Una vez dentro de la plataforma, se selecciona la opción de 'Herrmaientas de desarrollo API'


<div align = "center">
  <img src = "https://i.imgur.com/vhwC98f.png"/> 
</div>

3. Posteriormente, se llenan los campos vacios a gusto de la organizacion, escribiendo el nombre de la app (como se vera la sesion iniciada en telegram cuando se mira en dispositivos), la url poniendo por defecto www.telegram.org, escribiendo la plataforma en la que se pretende usar y una descripción del mismo

<div align = "center">
  <img src = "https://i.imgur.com/ToGpCsX.png"/> 
</div>

4. Una vez creado, podemos observar los campos de API ID y API HASH, los cuales serán utilizados para crear un token de sesión en la plataforma de nuestra cuenta, para asi permitir que esta app se establezca como sesion en el Telegram del administrador

<div align = "center">
  <img src = "https://i.imgur.com/Yf7Q8yv.png"/> 
</div>

5. Ahora, una vez teniendo el API ID y el API HASH, se debe generar un 'sessionstring' con el [código de ErichDaniken](https://replit.com/@ErichDaniken/Generate-Telegram-String-Session#main.py) que se encuentra en la plataforma de Replit (aunque se recomienda copiarlo y utilizarlo de manera local para evitar errores). Se ejecuta el código, se selecciona la opcion de telethon y se ingresa el API ID y el API HASH generado anteriormente, ademas de otro datos, como el numero de telefono y el código que llega de verificacion al mismo. Posteriormente podra ver como la app que usted creó anteriormente aparece en su Telegram como una sesión iniciada.

6. Ahora se necesita vincular esta sesión con el flujo para que a través de dicho medio se envíen los mensajes a los grupos a los que pertenece el usuario en cuestión. Para ello, se debe acceder a las **variables** del flujo de automatización de grupos de empleabilidad en n8n y agregar el API ID Y API HASH bien mencionado anteriormente.

<div align = "center">
  <img src = "https://i.imgur.com/piJd29J.png"/> 
</div>

<div align = "center">
  <img src = "https://i.imgur.com/xxd7uwH.png"/> 
</div>

7. Por ultimo, se debe agregar el 'sessionstring' manualmente en el nodo que realiza el POST a la API en FASTAPI para el envío de mensajes en Telegram. Por lo cual, se selecciona el nodo correspondiente y en el campo de 'sessionstring' se agrega todo el string generado anteriormente de la sesión correspondiente.

<div align = "center">
  <img src = "https://i.imgur.com/2yio227.png"/> 
</div>

<div align = "center">
  <img src = "https://i.imgur.com/yC15qeI.png"/> 
</div>

### Conexión con correo Outlook para envío de notificaciones.
1. Se selecciona el nodo de Outlook, llamado 'Send Notify', el cual permite conectarse con Outlook y mandar un correo al destino que se desee.

<div align = "center">
<img src = "https://i.imgur.com/xEohfCM.png"/> 
</div>

2. Se selecciona la credencial de Outlook, la cual permite hacer el envio de correos desde la cuenta que se asocie con la misma.

<div align = "center">
<img src = "https://i.imgur.com/b053EC3.png"/> 
</div>

3. Se escribe el correo destino al cual le van a llegar las notificaciones de cuando se realicen envios exitosos de vacantes laborales a grupos de empleabilidad. 

<div align = "center">
<img src = "https://i.imgur.com/BVJm4HF.png"/> 
</div>

**Cabe recalcar que para la configuracion del envío de notificación para el flujo de error se hacen exactamente los mismos pasos mencionados anteriormente**

### Configuración de flujo de error para envío de notificaciones de fallo
1. En los 3 puntos dentro del flujo de 'automation-employability-groups', seleccionar la opción 'settings'
<div align = "center">
<img src = "https://i.imgur.com/MMIIZwQ.png"/> 
</div>

2. En la opción 'Error Workflow' escoger el flujo de error realizado para mandar el envío de la notificación, en este caso, llamado de la misma manera 'Error Workflow' y guardar los cambios.

<div align = "center">
<img src = "https://i.imgur.com/CITbVtg.png"/> 
</div>


<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>


## Explicación de flujo general

### Creación de Endpoint

La primera etapa del flujo se centra en la recolección de información a través de un endpoint. El nodo inicial representa un endpoint de tipo POST, diseñado para recibir datos en formato JSON. En este caso, el endpoint está destinado a recibir información sobre vacantes críticas junto con sus respectivos campos.

Una vez recibidos los datos JSON, el flujo avanza hacia un nodo denominado "Obtain Body JSON", el cual se configura manualmente. Este nodo tiene la función de extraer la parte principal del JSON recibido, es decir, el cuerpo que contiene los detalles de las vacantes críticas, descartando cualquier información adicional que no sea relevante.

Esta parte del flujo se visualiza en el siguiente segmento del proceso:

<div align = "center">
<img src = "https://i.imgur.com/KwOMKBk.png"/> 
</div>


### Iteración sobre cada vacante de la base datos

Después de recibir y procesar la información de las vacantes críticas, se procede a la lectura de los grupos disponibles en la base de datos de Excel. Este proceso se lleva a cabo a través de los siguientes nodos:

1. **Base de datos:** La organización mantiene un archivo de Excel que contiene una tabla con información sobre los grupos de empleabilidad, ya sean creados por la organización o preexistentes para las vacantes. Cada grupo tiene un identificador único (ID), una plataforma asociada, uno o más identificadores de sector (SectorID) y un token de autenticación (Token).

2. **Para cada grupo:** El flujo itera sobre cada fila de la tabla, lo que significa que procesará cada grupo individualmente. Esto permite realizar operaciones específicas para cada grupo en los pasos posteriores.

3. **División de SectorIDs:** Dado que un grupo puede estar asociado con varios sectores (por ejemplo, ventas, marketing y finanzas), el valor de la columna SectorID se divide en una lista de identificadores individuales. Esto facilita la posterior comparación con los sectores asociados a cada vacante crítica.

4. **Limpieza del cuerpo JSON:** En este punto, se realiza un procesamiento adicional en el cuerpo JSON que contiene los datos de las vacantes críticas recibidas. Esto puede incluir la eliminación de campos innecesarios, la reestructuración del formato JSON, o cualquier otra transformación necesaria para preparar los datos para el siguiente paso.

5. **Para cada vacante:** Finalmente, el flujo itera sobre cada vacante crítica individual presente en el cuerpo JSON limpio. Esto se hace para poder comparar cada vacante con los grupos procesados anteriormente.

Esta parte del flujo se visualiza en el siguiente segmento del proceso:

<div align = "center">
<img src = "https://i.imgur.com/ZEGSMCv.png"/> 
</div>

### Asociación entre cada vacante y cada grupo

Durante esta etapa, el objetivo principal es identificar las vacantes que coinciden con los criterios de cada grupo y tomar las acciones correspondientes según la plataforma asociada.

1. **Para cada vacante:** Este nodo itera sobre cada vacante crítica individual presente en el cuerpo JSON limpio, lo que permite evaluar cada una de ellas individualmente.

2. **Verificar IDs:** En este paso, se compara el identificador de sector (SectorID) asociado a la vacante actual con el identificador de sector del grupo que se está procesando. Esta comparación se realiza para determinar si la vacante pertenece al sector representado por el grupo actual.

3. **Verificar Plataforma:** Si los identificadores de sector coinciden, el flujo avanza al siguiente nodo, donde se verifica la plataforma asociada al grupo. Aunque este flujo está configurado inicialmente para manejar la plataforma Telegram, se ha diseñado de manera que pueda integrarse fácilmente con otras plataformas en el futuro.

4. **Identificar Plataforma para Enviar Mensaje:** Si la plataforma del grupo es Telegram, el flujo continúa hacia el nodo "Identificar Plataforma para Enviar Mensaje". Aquí, se redirige al flujo de envío de la plataforma específica para determinar cómo y a quién se debe enviar un mensaje o notificación relacionado con la vacante que coincide con el grupo actual.

Esta parte del flujo se visualiza en el siguiente segmento del proceso:

<div align = "center">
<img src = "https://i.imgur.com/Zt0XMv3.png"/> 
</div>

### Envio a plataforma especifica

En este punto, luego de identificar la plataforma, se procede a ejecutar toda la parte del envío a esta plataforma:

1. **Identificar Plataforma para Enviar Mensaje:** Este nodo determina que la plataforma seleccionada para enviar el mensaje es Telegram, y por lo tanto, activa el flujo correspondiente.

2. **Telegram:** Representa la integración con la API de Telegram. Aquí se configura el envío de un mensaje a través de Telegram, el cual contiene información sobre la vacante crítica que coincide con el grupo analizado previamente.

3. **Combinar Información:** En este nodo se fusiona la información proveniente de dos entradas diferentes. En este caso, se combina la información del mensaje enviado a Telegram con otros datos relevantes del proceso, como detalles del grupo o de la vacante crítica.

4. **Listar Respuesta de Telegram:** Después de enviar el mensaje a través de Telegram, este nodo recopila y lista la respuesta obtenida de la API de Telegram. Esta respuesta contiene información útil, como el estado del envío, el ID del mensaje, entre otros detalles.


Este proceso permite notificar de manera automatizada a los destinatarios correspondientes en Telegram sobre las vacantes críticas que coinciden con los criterios de los grupos predefinidos.


Esta parte del flujo se visualiza en el siguiente segmento del proceso:

<div align = "center">
<img src = "https://i.imgur.com/LRmrAKZ.png"/> 
</div>

### Enviar notificacion de vacantes enviadas

Luego de completar todo el proceso de envío de vacantes a sus respectivos grupos, se procede a leer todos los registros de la base de datos y enviar un correo de notificación que indica las vacantes enviadas junto con información adicional:

1. **Listar Información de Telegram:** Este nodo recopila y almacena toda la información relacionada con los mensajes enviados a través de Telegram. Esto incluye detalles como el contenido del mensaje, el destinatario, la hora de envío, el estado de entrega, entre otros.

2. **Interruptor (Switch):** Actuando como un punto de control, este nodo evalúa una condición o regla específica. Dependiendo del resultado de esta evaluación, el flujo tomará una ruta diferente.

3. **Enviar Notificación:** Si se cumple la condición establecida en el nodo "Interruptor", el flujo avanza hacia el nodo "Enviar Notificación". Aquí se configurará y enviará un correo electrónico a través de Outlook.

El correo electrónico enviado desde Outlook contiene un resumen o informe de las vacantes críticas que coincidieron con los grupos y fueron notificadas a través de Telegram. Esto permite informar a los interesados o responsables relevantes sobre las acciones tomadas y el estado de las notificaciones enviadas.

Este paso final del flujo de trabajo tiene como objetivo consolidar y compartir la información relevante sobre el procesamiento de las vacantes críticas y las notificaciones enviadas. Al enviar un correo electrónico a través de Outlook, se asegura que los interesados reciban una actualización completa sobre el proceso realizado, lo que facilita el seguimiento y la toma de decisiones posteriores.

De esta manera, el flujo completo con esta ultima seccion se veria : 

<div align = "center">
<img src = "https://i.imgur.com/6EuhtqF.png"/> 
</div>

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>

## Configuración de endpoint

El endpoint creado espera que el conjunto de vacantes criticas que recibe este dado bajo la siguiente estructura en formato JSON con una petición POST:

```JSON
[
 {
    "job_title": "Nombre de la vacante laboral (str)",
    "location": "Ubicación de la vacante laboral (str)",
    "requirements": ["Requerimiento 1 (str)", "Requerimiento 2 (str)". "Requerimiento n (str)"],
    "job_link": "Enlace de la vacante (str)",
    "salary": "Salario de la vacante + unidad monetaria (str) ",
    "required_experience": "experiencia requerida para la vacante laboral (str) ",
    "sector_id": "ID del secto de la vacante laboral (str)",
    "platform": "Plataforma donde se va a enviar la vacante laboral (str)"
 } // más vacantes criticas...
]
```
Recordar también que el flujo de 'automation-employability-groups', debe ser activado y las peticiones POST se realizan al link de producción de la URL
<div align = "center">
<img src = "https://i.imgur.com/7YshO7L.png"/> 
</div>

<div align = "center">
<img src = "https://i.imgur.com/FLOigH8.png"/> 
</div>


<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>


## Escalabilidad

El enfoque que se ha tomado con este flujo de trabajo en n8n es diseñarlo de manera escalable y flexible, lo que permite agregar fácilmente nuevas plataformas para el envío de notificaciones de vacantes críticas.
Algunos puntos clave a destacar:

1. Base de datos centralizada: Toda la información sobre los grupos y sus criterios asociados se almacena en un archivo de Excel. Esto facilita la gestión y actualización de los grupos, ya que solo se requiere agregar o modificar filas en la hoja de cálculo correspondiente como se ve en la siguiente imagen  : 

<div align = "center">
<img src = "https://i.imgur.com/qx9gURY.png"/> 
</div>

2. Lectura automática de la base de datos: El flujo de trabajo lee automáticamente los datos de la hoja de cálculo, lo que significa que cualquier cambio o adición en la base de datos se reflejará automáticamente en el procesamiento de los grupos y las vacantes críticas.

3. Nodo "Identify Platform To Send Message": Este nodo actúa como un punto de decisión clave en el flujo de trabajo. Aquí es donde se evalúa la plataforma asociada a cada grupo y se determina qué flujo específico de notificación se debe activar.

4. Escalabilidad mediante nuevos flujos: Para agregar una nueva plataforma de notificación, como WhatsApp o Facebook, simplemente se debe crear un nuevo flujo de trabajo dedicado a esa plataforma y conectarlo al nodo "Identify Platform To Send Message". De esta manera, cuando se identifique un grupo asociado a la nueva plataforma, el flujo de trabajo correspondiente se activará automáticamente. Esto se realiza en la siguiente parte del flujo : 

<div align = "center">
<img src = "https://i.imgur.com/kvSFkjR.png"/> 
</div>

5. Integraciones preexistentes: n8n ofrece una amplia gama de integraciones listas para usar con diversos servicios y plataformas. Esto facilita la creación de flujos de trabajo para nuevas plataformas, aprovechando las integraciones ya disponibles y evitando tener que desarrollar desde cero.

Este enfoque modular y escalable permite a la organización adaptarse rápidamente a nuevos requisitos o canales de notificación. Simplemente se agregan los nuevos grupos a la base de datos centralizada y se crea el flujo de trabajo correspondiente para la nueva plataforma, aprovechando la infraestructura existente.
Además, al centralizar la información de los grupos en un archivo de Excel, se simplifica la gestión y el mantenimiento de los datos, lo que facilita la incorporación de nuevos grupos o la modificación de los existentes sin afectar el flujo de trabajo principal.

<p align="right">(<a href="#readme-top">Volver arriba</a>)</p>



