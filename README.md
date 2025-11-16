📘 U3 – Aplicación Web con Flask

Programación Web – IPLACEX
Unidad 3 – Fundamentos de Python

📌 Descripción del proyecto

Este proyecto corresponde al Encargo 3 de Programación Web, cuyo objetivo es crear una aplicación web con Flask que implemente:

Un menú principal con dos ejercicios.

Formularios HTML.

Procesamiento de datos en Python.

Uso de plantillas con Jinja2 (templates/).

Hoja de estilos CSS (static/styles.css).

El desarrollo cumple íntegramente las instrucciones entregadas en el documento TA_6.docx.

🚀 Tecnologías utilizadas

Python 3.x

Flask 2.x

HTML5 & CSS3

Jinja2

Visual Studio Code

Entorno virtual (venv)

Git & GitHub

📁 Estructura del proyecto

La aplicación se ejecuta dentro de la carpeta app/, sin crear estructuras adicionales para evitar conflictos con el entorno virtual ya existente.

app/
│
├── main.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── ejercicio1.html
│   └── ejercicio2.html
│
└── static/
    └── styles.css

🧩 Funcionalidades del proyecto
🔹 1. Menú principal (index.html)

Página inicial que contiene dos botones para acceder a:

Ejercicio 1 – Cálculo de promedio y estado del estudiante.

Ejercicio 2 – Identificación del nombre con más caracteres.

El diseño utiliza enlaces generados con url_for() siguiendo las buenas prácticas de Flask.

🔹 2. Ejercicio 1 – Cálculo de promedio y asistencia

El formulario solicita:

Nota 1

Nota 2

Nota 3

Asistencia (%)

Lógica aplicada:

promedio = (n1 + n2 + n3) / 3


Condición de aprobación:

Promedio ≥ 40

Asistencia ≥ 75%

Si cualquiera de los datos es inválido, se muestra un mensaje de error.

🔹 3. Ejercicio 2 – Nombre con más caracteres

El usuario debe ingresar:

Nombre 1

Nombre 2

Nombre 3

La aplicación determina:

Cuál nombre tiene mayor longitud.

Cuántos caracteres posee.

Muestra los tres nombres ingresados.

Incluye validación para evitar espacios vacíos.

🔹 4. Plantillas HTML (Jinja2)

La aplicación usa:

base.html como estructura principal con:

Header

Footer

Barra de navegación

Bloques title y content

Los demás archivos (index.html, ejercicio1.html, ejercicio2.html) heredan desde base.html.

🔹 5. Estilos CSS (static/styles.css)

Incluye:

Colores base

Estilo para enlaces y botones

Diseño responsivo simple

Formularios estilizados

Sección de resultados

Estilo para mensajes de error

🛠 Instalación y ejecución

Sigue estos pasos dentro de la carpeta app/:

1️⃣ Activar el entorno virtual

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

2️⃣ Instalar los módulos requeridos
pip install -r requirements.txt

3️⃣ Ejecutar la aplicación Flask
python main.py


Abrir en el navegador:

👉 http://127.0.0.1:5000/

📸 Capturas recomendadas

(Pega tus capturas donde corresponda)

Menú principal

Formulario de Ejercicio 1

Resultado del Ejercicio 1

Formulario de Ejercicio 2

Resultado del Ejercicio 2

Estructura del proyecto en VS Code

🧪 Pruebas realizadas

Navegación entre rutas del menú

Validación de notas incorrectas

Validación de nombres vacíos

Procesamiento correcto de datos

Renderización dinámica con plantillas

Carga de estilos desde /static

Compatibilidad en Chrome y Edge

🔗 Repositorio del proyecto

Añade aquí tu repositorio cuando lo subas a GitHub:

https://github.com/tu_usuario/tu_repositorio

📄 Licencia académica

Este proyecto está destinado exclusivamente a fines educativos dentro del marco de la asignatura Programación Web – IPLACEX, Unidad 3.

Su uso o distribución fuera de este contexto debe ser autorizado por su autor/a.

✍️ Autor

Jonathan Damián Peña
Estudiante de Programación Web – IPLACEX
Año 2025
