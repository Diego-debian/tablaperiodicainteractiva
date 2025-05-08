# Importar la instancia de SQLAlchemy (db) desde el módulo data_base
from data_base import db

# Definición de la clase Elemento que hereda de db.Model
# Esta clase representa la tabla 'elemento' en la base de datos
class Elemento(db.Model):
    # Configuración de las columnas de la tabla
    
    # ID único como clave primaria
    id = db.Column(db.Integer, primary_key=True)
    
    # Número atómico (único y obligatorio)
    number = db.Column(db.Integer, unique=True, nullable=False)
    
    # Símbolo químico (obligatorio, máximo 2 caracteres)
    symbol = db.Column(db.String(2), nullable=False)
    
    # Nombre del elemento (obligatorio, máximo 50 caracteres)
    name = db.Column(db.String(50), nullable=False)
    
    # Categoría del elemento (ej: metal, no metal, metaloide)
    category = db.Column(db.String(50))
    
    # Grupo en la tabla periódica
    group = db.Column(db.Integer)
    
    # Periodo en la tabla periódica
    period = db.Column(db.Integer)
    
    # Masa atómica (en unidades de masa atómica)
    atomic_mass = db.Column(db.Float)
    
    # Configuración electrónica (ej: [He] 2s2 2p2)
    electron_config = db.Column(db.String(100))
    
    # Año de descubrimiento
    discovery = db.Column(db.Integer)
    
    # Persona(s) que descubrió el elemento
    discoverer = db.Column(db.String(100))
    
    # Densidad (en g/cm³)
    density = db.Column(db.Float)
    
    # Punto de fusión (en K)
    melt = db.Column(db.Float)
    
    # Punto de ebullición (en K)
    boil = db.Column(db.Float)
    
    # Fase a temperatura ambiente (sólido, líquido, gas)
    phase = db.Column(db.String(20))
    
    # Resumen/descripción del elemento
    summary = db.Column(db.Text)

    # Método para convertir el objeto Elemento a un diccionario
    # Útil para serializar el objeto a JSON
    def to_dict(self):
        return {
            'number': self.number,
            'symbol': self.symbol,
            'name': self.name,
            'category': self.category,
            'group': self.group,
            'period': self.period,
            'atomic_mass': self.atomic_mass,
            'electron_config': self.electron_config,
            'discovery': self.discovery,
            'discoverer': self.discoverer,
            'density': self.density,
            'melt': self.melt,
            'boil': self.boil,
            'phase': self.phase,
            'summary': self.summary
        }