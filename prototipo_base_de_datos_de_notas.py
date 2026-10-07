import sqlite3

# nota para mi: conexion al archivo local
conexion = sqlite3.connect("registro_colegio.db")
mensajero = conexion.cursor()

# nota para mi: la tabla basica para guardar las notas del colegio
mensajero.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    nombre VARCHAR,
    tipo_doc VARCHAR,
    documento INT,
    nota VARCHAR
)
""")
conexion.commit()

def agregar():
    print("\n-- AGREGAR ESTUDIANTE --")
    n = input("Nombre completo: ")
    
    print("Tipo de documento:")
    print("1. TI")
    print("2. CC")
    t_op = input("Selecciona (1 o 2): ")
    
    # nota para mi: validar rapido si es TI o CC
    if t_op == "1":
        td = "TI"
    elif t_op == "2":
        td = "CC"
    else:
        td = "TI"
        
    doc = input("Numero de documento: ")
    not_est = input("Nota: ")
    
    # nota para mi: acordarme de las comillas simples en los textos
    mensajero.execute(f"INSERT INTO estudiantes VALUES ('{n}', '{td}', {doc}, '{not_est}')")
    conexion.commit()
    print("Guardado con exito.")

def mostrar_todos():
    print("\n-- LISTA COMPLETA DE NOTAS --")
    mensajero.execute("SELECT * FROM estudiantes")
    datos = mensajero.fetchall()
    
    for fila in datos:
        print(fila)

def buscar_documento():
    print("\n-- BUSCAR POR DOCUMENTO --")
    d_bus = input("Ingresa el numero de documento: ")
    
    # nota para mi: filtrar con WHERE usando el numero de documento
    mensajero.execute(f"SELECT * FROM estudiantes WHERE documento = {d_bus}")
    resultado = mensajero.fetchall()
    
    if resultado:
        for fila in resultado:
            print(fila)
    else:
        # nota para mi: por si no aparece en la bd
        print("No se encontro ningun estudiante con ese documento.")

# nota para mi: script del menu
while True:
    print("\n=== REGISTRO DE NOTAS ===")
    print("1. Agregar estudiante")
    print("2. Ver todas las notas")
    print("3. Buscar por documento")
    print("4. Salir")
    
    op = input("Opcion: ")
    
    if op == "1":
        agregar()
    elif op == "2":
        mostrar_todos()
    elif op == "3":
        buscar_documento()
    elif op == "4":
        print("Saliendo...")
        conexion.close()
        break
    else:
        # nota para mi: por si eligen una opcion que no existe
        print("Opcion invalida.")