import os

if __name__ == "__main__":
    # El modo debug SOLO se activa si la variable de entorno FLASK_DEBUG=1
    # Nunca habilitar debug en producción: permite RCE vía /console de Werkzeug.
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"
    host = os.environ.get("FLASK_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_PORT", "5000"))
    app.run(host=host, port=port, debug=debug_mode)