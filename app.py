# Importar las librerías necesarias
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import json
from Elemento import Elemento
from data_base import db
from flask import render_template, redirect, url_for
import os

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elementos.db'  # Usar SQLite como base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar el seguimiento de modificaciones para mejorar el rendimiento

# Configurar correctamente las carpetas para los archivos estáticos (CSS, JS, imágenes)
app.static_folder = 'static'
app.static_url_path = '/static'

# Inicializar la base de datos con la aplicación Flask
db.init_app(app)

# Crear las tablas en la base de datos dentro del contexto de la aplicación
with app.app_context():
    db.create_all()

# Función auxiliar para convertir un objeto Elemento a un diccionario
def elemento_to_dict(elemento):
    return {
        'number': elemento.number,
        'symbol': elemento.symbol,
        'name': elemento.name,
        'category': elemento.category,
        'group': elemento.group,
        'period': elemento.period,
        'atomic_mass': elemento.atomic_mass,
        'electron_config': elemento.electron_config,
        'discovery': elemento.discovery,
        'discoverer': elemento.discoverer,
        'density': elemento.density,
        'melt': elemento.melt,
        'boil': elemento.boil,
        'phase': elemento.phase,
        'summary': elemento.summary
    }

# Ruta para agregar elementos (POST)
@app.route('/elementos', methods=['POST'])
def add_elementos():
    # Cargar datos desde el JSON en la solicitud
    elementos_data = request.get_json()
    
    # Verificar si se proporcionaron datos
    if not elementos_data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    # Asegurarse de que los datos sean una lista (para manejar tanto uno como varios elementos)
    if not isinstance(elementos_data, list):
        elementos_data = [elementos_data]
    
    added = 0  # Contador de elementos agregados exitosamente
    errors = []  # Lista para almacenar errores
    
    # Procesar cada elemento en los datos recibidos
    for elemento_data in elementos_data:
        try:
            # Crear un nuevo objeto Elemento con los datos proporcionados
            nuevo_elemento = Elemento(
                number=elemento_data['number'],
                symbol=elemento_data['symbol'],
                name=elemento_data['name'],
                category=elemento_data.get('category'),
                group=elemento_data.get('group'),
                period=elemento_data.get('period'),
                atomic_mass=elemento_data.get('atomic_mass'),
                electron_config=elemento_data.get('electron_config'),
                discovery=elemento_data.get('discovery'),
                discoverer=elemento_data.get('discoverer'),
                density=elemento_data.get('density'),
                melt=elemento_data.get('melt'),
                boil=elemento_data.get('boil'),
                phase=elemento_data.get('phase'),
                summary=elemento_data.get('summary')
            )
            
            # Agregar el nuevo elemento a la sesión de la base de datos
            db.session.add(nuevo_elemento)
            added += 1
        except IntegrityError:
            # Manejar error de integridad (elemento duplicado)
            db.session.rollback()
            errors.append(f"Elemento {elemento_data.get('symbol')} ya existe")
        except Exception as e:
            # Manejar otros errores
            db.session.rollback()
            errors.append(str(e))
    
    try:
        # Intentar confirmar los cambios en la base de datos
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
    # Retornar respuesta con el número de elementos agregados y errores encontrados
    return jsonify({
        "message": f"Se agregaron {added} elementos",
        "errors": errors
    }), 201 if added > 0 else 400

# Ruta para obtener todos los elementos (GET)
@app.route('/api/elementos', methods=['GET'])
def get_elementos():
    try:
        # Obtener todos los elementos de la base de datos
        elementos = Elemento.query.all()
        # Convertir cada elemento a diccionario y retornar como JSON
        return jsonify([elemento_to_dict(e) for e in elementos])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para obtener un elemento específico por número atómico (GET)
@app.route('/api/elementos/<int:number>', methods=['GET'])
def get_elemento(number):
    try:
        # Buscar el elemento por número atómico
        elemento = Elemento.query.filter_by(number=number).first()
        if elemento:
            # Si se encuentra, retornar sus datos
            return jsonify(elemento_to_dict(elemento))
        # Si no se encuentra, retornar error 404
        return jsonify({"error": "Elemento no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para mostrar la página de un elemento específico
@app.route('/elemento/<int:number>')
def show_elemento(number):
    # Buscar el elemento o retornar 404 si no existe
    elemento = Elemento.query.filter_by(number=number).first_or_404()
    # Renderizar la plantilla con los datos del elemento
    return render_template('elemento.html', elemento=elemento)

# Manejador de error para páginas no encontradas (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Ruta para editar un elemento (GET para mostrar formulario, POST para procesar cambios)
@app.route('/elemento/<int:number>/edit', methods=['GET', 'POST'])
def edit_elemento(number):
    # Buscar el elemento o retornar 404 si no existe
    elemento = Elemento.query.filter_by(number=number).first_or_404()
    
    if request.method == 'POST':
        # Actualizar los campos del elemento con los datos del formulario
        elemento.symbol = request.form.get('symbol', elemento.symbol)
        elemento.name = request.form.get('name', elemento.name)
        elemento.category = request.form.get('category', elemento.category)
        elemento.group = request.form.get('group', elemento.group)
        elemento.period = request.form.get('period', elemento.period)
        elemento.atomic_mass = request.form.get('atomic_mass', elemento.atomic_mass)
        elemento.electron_config = request.form.get('electron_config', elemento.electron_config)
        elemento.discovery = request.form.get('discovery', elemento.discovery)
        elemento.discoverer = request.form.get('discoverer', elemento.discoverer)
        elemento.density = request.form.get('density', elemento.density)
        elemento.melt = request.form.get('melt', elemento.melt)
        elemento.boil = request.form.get('boil', elemento.boil)
        elemento.phase = request.form.get('phase', elemento.phase)
        elemento.summary = request.form.get('summary', elemento.summary)
        
        try:
            # Intentar guardar los cambios
            db.session.commit()
            # Redirigir a la página del elemento editado
            return redirect(url_for('show_elemento', number=elemento.number))
        except Exception as e:
            # Si hay error, mostrar el formulario nuevamente con el mensaje de error
            db.session.rollback()
            return render_template('/forms/edit_elemento.html', elemento=elemento, error=str(e))
    
    # Mostrar el formulario de edición con los datos actuales del elemento
    return render_template('/forms/edit_elemento.html', elemento=elemento)

# Ruta API para actualizar un elemento (PUT)
@app.route('/api/elementos/<int:number>', methods=['PUT'])
def update_elemento(number):
    # Buscar el elemento o retornar 404 si no existe
    elemento = Elemento.query.filter_by(number=number).first_or_404()
    data = request.get_json()
    
    # Verificar si se proporcionaron datos
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    # Actualizar solo los campos proporcionados en el JSON
    for field in ['symbol', 'name', 'category', 'group', 'period', 'atomic_mass', 
                 'electron_config', 'discovery', 'discoverer', 'density', 
                 'melt', 'boil', 'phase', 'summary']:
        if field in data:
            setattr(elemento, field, data[field])
    
    try:
        # Intentar guardar los cambios
        db.session.commit()
        # Retornar los datos actualizados del elemento
        return jsonify(elemento_to_dict(elemento))
    except Exception as e:
        # Si hay error, retornar mensaje de error
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
# Ruta principal que muestra la tabla periódica
@app.route('/')
def index():
    # Obtener todos los elementos ordenados por número atómico
    elementos = Elemento.query.order_by(Elemento.number).all()
    
    # Agregar un script para actualizar el año del copyright automáticamente
    current_year = {
        'year': 2025  # Este valor podría obtenerse dinámicamente con datetime.now().year
    }
    
    # Renderizar la plantilla principal con los elementos y el año actual
    return render_template('index.html', elementos=elementos, current_year=current_year)

# Punto de entrada principal para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar en modo debug para desarrollo