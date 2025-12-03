# Tema1 - Formulario de Contacto (Flask)

Autor: Fabiola Rodriguez - 2023100468

## Contenido
- app.py        -> aplicación Flask simple
- templates/    -> HTML para formulario, gracias y dashboard
- create_table_mysql.sql -> script SQL para crear la tabla en MySQL (opcional)
- requirements.txt

## Ejecutar local (usa SQLite por defecto)
1. Crear un entorno virtual (recomendado):
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows

2. Instalar dependencias:
   pip install -r requirements.txt

3. Ejecutar:
   python app.py






   mi enlace de pagina  tema 2
   file:///C:/Users/FABIOLA/Desktop/holi/Fabiola_Rodriguez_2023100468/Tema2/index.html

5. Abrir en el navegador (para acceder desde otro equipo en la misma red local):
   http://<IP-del-equipo>:5000  (ej: http://192.168.0.10:5000)

## Notas:
- Para usar MySQL en vez de SQLite: editar app.py y reemplazar la lógica de sqlite3 por un conector MySQL (pymysql o mysql-connector-python)

