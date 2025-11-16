from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None

    if request.method == "POST":
        try:
            nota1 = float(request.form.get("nota1", 0))
            nota2 = float(request.form.get("nota2", 0))
            nota3 = float(request.form.get("nota3", 0))
            asistencia = float(request.form.get("asistencia", 0))

            # Cálculo del promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # Condiciones de aprobación:
            # promedio >= 40 y asistencia >= 75
            if promedio >= 40 and asistencia >= 75:
                estado = "APROBADO/A"
            else:
                estado = "REPROBADO/A"

            resultado = {
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3,
                "asistencia": asistencia,
                "promedio": round(promedio, 2),
                "estado": estado,
            }

        except ValueError:
            resultado = {
                "error": "Debes ingresar solo números válidos en notas y asistencia."
            }

    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None

    if request.method == "POST":
        nombre1 = request.form.get("nombre1", "").strip()
        nombre2 = request.form.get("nombre2", "").strip()
        nombre3 = request.form.get("nombre3", "").strip()

        # Validación sencilla
        if not nombre1 or not nombre2 or not nombre3:
            resultado = {
                "error": "Debes ingresar los tres nombres."
            }
        else:
            nombres = [nombre1, nombre2, nombre3]
            # Nombre con mayor cantidad de caracteres
            nombre_mas_largo = max(nombres, key=len)
            cantidad_caracteres = len(nombre_mas_largo)

            resultado = {
                "nombre1": nombre1,
                "nombre2": nombre2,
                "nombre3": nombre3,
                "nombre_mas_largo": nombre_mas_largo,
                "cantidad_caracteres": cantidad_caracteres,
            }

    return render_template("ejercicio2.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
