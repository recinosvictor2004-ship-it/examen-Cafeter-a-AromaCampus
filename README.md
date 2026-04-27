# Proyecto_Git_VictorRecinos_LuisEstrada
## Saludos Cordiales! 👋😊
### --- Te damos la Bienvenida a nuestro proyecto, esperamos sea de tu agrado! 😉---
---
## ☕ Cafetería AromaCampus

Sistema en **Python** para administrar un inventario básico de una cafetería.  

Permite registrar, gestionar y consultar productos de manera sencilla.

---

## 🚀 Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/Cafeteria_AromaCampus.git

2. Asegúrate de tener instalado Python 3.x en tu equipo.

3. Dale click en la flecha blanca en la esquina superior derecha.

## ▶️ Uso
### 1. Ejecuta el programa desde la terminal:
- python cafeteria.py

### 2. El codigo permite selecionar:

- Listar tipo de café

- Agregar tipo de café

- Editar tipo de café

- Eliminar tipo de café

- Salir

## ✅ Resolucion de Conflictos ❌

❌Durante el proceso de integración de varias ramas del proyecto, surgieron conflictos principalmente en los archivos inventario.py y main.py. Estos conflictos aparecieron porque diferentes ramas habían modificado las mismas partes del código. Para resolverlos, utilicé las herramientas de Git integradas en Visual Studio Code.

Primero, abrí la sección Source Control, donde Git mostraba los archivos bajo la categoría Merge Changes. Desde ahí seleccioné cada archivo en conflicto y revisé las secciones marcadas por Git con:

<<<< HEAD
======
>>>>> rama

En inventario.py, el conflicto se debía a que una rama contenía funciones nuevas como get_next_id, mientras que la otra tenía la función eliminar_cafe. Analicé ambas versiones y seleccioné Accept Both Changes, ya que ambas funciones eran necesarias para el módulo de inventario. Después eliminé los marcadores de conflicto y verifiqué que el archivo quedara limpio.

Luego abrí main.py, que también tenía conflictos. Repetí el proceso: revisé las diferencias, elegí la opción adecuada según el código que debía conservarse y limpié los marcadores.

Una vez resueltos todos los conflictos, ejecuté:

git add
git commit -m "fix: resolver conflicto merge"

 Con esto marqué los conflictos como solucionados. Finalmente, actualicé la rama main y subí los cambios al repositorio remoto con:  

 git push origin main

  Después de esto, GitHub reflejó correctamente los commits de corrección y el historial quedó limpio y sincronizado.✅


## 📂 Estructura
main.py → Código principal del sistema.

coffees.json → Archivo donde se guardan los productos en formato diccionario.

README.md → Documentación del proyecto.

## 📜 Licenses
Este proyecto está bajo la licencia MIT.
Permite modificaciones y copias, pero no garantiza responsabilidad sobre usos comerciales.

## 👤 Autores
- Víctor Recinos
- Luis Estrada

## 📬 Contact
Correo: recinosvictor2004@gmail.com

- GitHub: recinosvictor2004-ship-it

Correo: luisestrada127016@gmail.com

- GitHub: luisestrada127016
