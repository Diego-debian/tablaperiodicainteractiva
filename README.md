# Tabla Periódica Interactiva 🌍⚗️

¡Explora, busca y edita los elementos químicos de forma dinámica con esta tabla periódica interactiva! Una herramienta educativa y visual para estudiantes, profesores y entusiastas de la química.


📹 **Video demostrativo**: 
 ![Tabla periodica](img/tablap.gif) 



## ✨ Funcionalidades
- **Búsqueda inteligente**: Encuentra elementos por nombre, símbolo o número atómico.
- **Modo edición**: Añade notas personalizadas o ajusta datos (modo offline/local).
- **Datos detallados**: Masa atómica, configuración electrónica, estado de oxidación y más.
- **Diseño responsive**: Compatible con móviles, tablets y desktop.
- **Tema /claro**: Personaliza la visualización.

## 🛠️ Tecnologías
- **Frontend**: HTML5, CSS3, JavaScript.
- **Backend**: Python - Flask
- **Bsase de Datos**: SQL_ALCHEMY
- **Estilos**: Flexbox/Grid, animaciones CSS.
- **Extra**: LocalStorage (para guardar ediciones), API de datos químicos (si usas una).


## Cómo Clonar el repositorio
Debes tener gitbash(Windows) o git(GNULinux) al igual que python instalado con virtualenv activo

### 1. Clonar el Repositorio de Git

El primer paso es obtener una copia local del código del repositorio. Asegúrate de tener Git instalado en tu sistema.

1.  Abre tu terminal o línea de comandos.
2.  Navega hasta la carpeta donde quieres guardar el proyecto usando el comando `cd`. Por ejemplo:
    ```bash
    cd ~/Documentos/Proyectos
    ```
3.  Clona el repositorio ejecutando el comando `git clone` seguido de la URL del repositorio:
    ```bash
    git clone https://github.com/Diego-debian/tablaperiodicainteractiva.git
    ```
  
    Esto creará una nueva carpeta con el nombre del repositorio y descargará todos los archivos en ella.

### 2. Navegar al Directorio del Repositorio

Una vez completada la clonación, accede a la carpeta del proyecto:

```bash
cd nombre-del-proyecto
```
### 3.  Crear y Activar un Entorno Virtual con virtualenv
Es una práctica recomendada usar entornos virtuales para mantener las librerías de Python de tu proyecto separadas de las del sistema y de otros proyectos.

Verificar o Instalar virtualenv: Si no tienes virtualenv instalado, puedes hacerlo con pip:
```Bash
pip install virtualenv
```
Crear el Entorno Virtual: Dentro del directorio de tu proyecto clonado, crea el entorno virtual. Un nombre común es venv:
```Bash
virtualenv venv
```
Esto creará una subcarpeta llamada venv con los ejecutables de Python y pip aislados.

Activar el Entorno Virtual: Debes activar el entorno virtual para usar las librerías instaladas dentro de él. El comando varía según tu sistema operativo:

En Linux o macOS:
```Bash
source venv/bin/activate
```
En Windows (usando Command Prompt):
```Bash
venv\Scripts\activate
```

Sabrás que el entorno virtual está activo porque verás su nombre (por ejemplo, (venv)) al inicio de tu línea de comandos.

4. Instalar las Dependencias
La mayoría de los proyectos de Python que utilizan dependencias externas tienen un archivo requirements.txt que lista las librerías necesarias.

Asegúrate de que el entorno virtual esté activado (verás (venv) al inicio de la línea de comandos).
Ejecuta el siguiente comando para instalar todas las dependencias listadas en requirements.txt:
```Bash
pip install -r requirements.txt
```

Pip descargará e instalará todas las librerías especificadas en el archivo dentro de tu entorno virtual activo.

5. Ejecuta el programa

```bash
python app,py
```

 ![Tabla periodica](img/tabla_1.gif) 

