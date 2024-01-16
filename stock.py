from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# Inventario simple, inicialmente vacío
inventario = {}

# Log de acciones
log_acciones = []

@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = ''
    clase_mensaje = ''
    if request.method == 'POST':
        accion = request.form['accion']
        producto = request.form['producto']
        detalles = request.form.get('detalles', '')  # Obtiene el detalle, si existe

        # ... dentro de tu función index ...

    if request.method == 'POST':
        accion = request.form['accion']
        producto = request.form['producto']

        if accion in ['agregar', 'quitar']:
            cantidad = int(request.form['cantidad'])

            if producto not in inventario:
                inventario[producto] = 0

            if accion == 'agregar':
                inventario[producto] += cantidad
                mensaje = f'Producto {producto} agregado. Cantidad actual: {inventario[producto]}'
            elif accion == 'quitar':
                if inventario[producto] >= cantidad:
                    inventario[producto] -= cantidad
                    mensaje = f'Producto {producto} quitado. Cantidad actual: {inventario[producto]}'
                else:
                    mensaje = 'No hay suficiente stock para quitar'
                    clase_mensaje = 'error'
            
             # Agregar entrada al log con detalles
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_acciones.append(f"{fecha_hora}: {accion} {cantidad} de '{producto}'. Detalles: {detalles}")

    return render_template('stockweb.html', mensaje=mensaje, clase_mensaje=clase_mensaje, inventario=inventario, log_acciones=log_acciones)

if __name__ == '__main__':
    app.run(debug=True)
