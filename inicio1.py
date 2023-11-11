import pandas as pd
df = pd.read_csv("base.csv")

def mostrar_menu():
    print("Menú:")
    print("1. Ingresar Registro")
    print("2. Buscar Registro")
    print("3. Modificar Registro")
    print("4. Eliminar Registro")
    print("5. Guardar Registros")
    print("6. Cerrar el Programa")

def ingresar_registro():
    import pandas as pd

    # Valores para los cálculos
    valor_turno_dia = 35000
    valor_turno_noche = 40000
    valor_he_dia = 2917
    valor_he_noche = 3333

    # Leer el archivo CSV
    try:
        df = pd.read_csv('base.csv')
    except FileNotFoundError:
        df = pd.DataFrame()

    while True:
        print("Ingresa los datos:")
        fecha = input("Fecha (dd-mm-aa): ")
        mes = input("Mes: ")
        año = int(input("Año: "))
        patente = input("Patente (6 caracteres): ")
        km_inicio = int(input("Km Inicio: "))
        km_termino = int(input("Km Termino: "))
        personal_id = input("Personal ID: ")
        cargo = input("Cargo (tens o conductor): ")
        turno = input("Turno (dia o noche): ")
        tipo_he = input("Tipo de HE (dia o noche): ")
        horas_extras = float(input("Horas Extras: "))

        monto_turno = valor_turno_dia if turno == 'dia' else valor_turno_noche
        monto_he = horas_extras * (valor_he_dia if turno == 'dia' else valor_he_noche)
        monto_a_pagar = monto_turno + monto_he

        # Agregar los valores ingresados al DataFrame
        df = pd.concat([df, pd.DataFrame({
            'fecha': fecha,
            'mes': mes,
            'año': año,
            'patente': patente,
            'km inicio': km_inicio,
            'km termino': km_termino,
            'km recorrido': km_termino - km_inicio,
            'personal_id': personal_id,
            'cargo': cargo,
            'turno': turno,
            'tipo he': tipo_he,
            'horas extras': horas_extras,
            'monto turno': monto_turno,
            'monto he': monto_he,
            'monto a pagar': monto_a_pagar
        }, index=[0])], ignore_index=True)

        print("Valores ingresados y calculados:")
        print(df.tail(1))

        # Guardar los datos en el archivo CSV
        df.to_csv('datos.csv', index=False)

        continuar = input("¿Deseas ingresar otro registro? (s/n): ")
        if continuar.lower() != 's':
            break

    # Guardar los datos en el archivo CSV
    df.to_csv('datos.csv', index=False)


def buscar_registro():
    print("Opciones de búsqueda:")
    print("1. Buscar por fecha")
    print("2. Buscar por patente")
    print("3. Buscar por personal_id")
    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        fecha_busqueda = input("Ingresa la fecha a buscar (dd-mm-aa): ")
        resultado = df.query(f"fecha == '{fecha_busqueda}'")
    elif opcion == "2":
        patente_busqueda = input("Ingresa la patente a buscar: ")
        resultado = df.query(f"patente == '{patente_busqueda}'")
    elif opcion == "3":
        personal_id_busqueda = input("Ingresa el personal_id a buscar: ")
        resultado = df.query(f"personal_id == '{personal_id_busqueda}'")
    else:
        print("Opción no válida.")
        return

    if not resultado.empty:
        print("Registros encontrados:")
        for i, registro in resultado.iterrows():
            print(f"Número de registro: {i}")
            print(registro)
            print("")
    else:
        print("No se encontraron registros para la búsqueda.")

import pandas as pd



def modificar_registro():
    df = pd.read_csv("base.csv")
    # Constantes
    VALOR_TURNO_DIA = 35000
    VALOR_TURNO_NOCHE = 40000
    VALOR_HE_DIA = 2917
    VALOR_HE_NOCHE = 3333

    # Datos del registro
    numero_registro = int(input("Ingresa el número de registro que deseas modificar: "))

    if numero_registro < 1 or numero_registro > len(df):
        print("Número de registro no válido.")
        return

    print("Registro actual:")
    print(df.iloc[numero_registro])

    # Solicitar datos nuevos
    print("Ingresa los nuevos datos:")
    datos_nuevos = {}
    datos_nuevos['fecha'] = input("Fecha (dd-mm-aa): ")
    datos_nuevos['mes'] = int(input("Mes: "))
    datos_nuevos['año'] = int(input("Año: "))
    datos_nuevos['patente'] = input("Patente (6 caracteres): ")
    datos_nuevos['km inicio'] = int(input("Km Inicio: "))
    datos_nuevos['km termino'] = int(input("Km Termino: "))
    datos_nuevos['personal_id'] = input("Personal ID: ")
    datos_nuevos['cargo'] = input("Cargo (tens o conductor): ")
    datos_nuevos['turno'] = input("Turno (dia o noche): ")
    datos_nuevos['tipo he'] = input("Tipo de HE (dia o noche): ")
    datos_nuevos['horas extras'] = float(input("Horas Extras: "))

    # Calcular nuevos montos
    datos_nuevos["km recorrido"] = datos_nuevos["km termino"] - datos_nuevos["km inicio"]
    datos_nuevos["monto turno"] = VALOR_TURNO_DIA if datos_nuevos['turno'] == 'dia' else VALOR_TURNO_NOCHE
    datos_nuevos["monto he"] = datos_nuevos['horas extras'] * (VALOR_HE_DIA if datos_nuevos['turno'] == 'dia' else VALOR_HE_NOCHE)
    datos_nuevos["monto a pagar"] = datos_nuevos["monto turno"] + datos_nuevos["monto he"]

    # Actualizar el DataFrame
    df.at[numero_registro, 'monto turno'] = datos_nuevos["monto turno"]
    df.at[numero_registro, 'monto he'] = datos_nuevos["monto he"]
    df.at[numero_registro , 'monto a pagar'] = datos_nuevos["monto a pagar"]
    df.loc[numero_registro] = datos_nuevos

    # Guardar los datos en el archivo CSV
    df.to_csv('base.csv', index=False)

    print("Registro modificado:")
    print(df.iloc[numero_registro]) # Restamos 1 para ajustar al índice


import pandas as pd

def eliminar_registro():
    df = pd.read_csv("base.csv")
    num_registro = int(input("Ingresa el número de registro que deseas eliminar: "))

    if num_registro < 1 or num_registro > len(df):
        print("Número de registro no válido.")
        return

    registro_a_eliminar = df.iloc[num_registro] # Obtenemos el registro a eliminar

    print("Registro a eliminar:")
    print(registro_a_eliminar)

    confirmacion = input("¿Estás seguro de que deseas eliminar este registro? (s/n): ")

    if confirmacion.lower() == 's':
        df = df.drop(num_registro - 1) # Eliminamos el registro del DataFrame

        print("Registro eliminado.")
        df.to_csv("base.csv", index=False)  # Guardamos el DataFrame modificado en el archivo CSV
    else:
        print("Eliminación cancelada.")

def guardar_registros():
    df.to_csv("base.csv", index=False)

# MENU INTERACTIVO

while True:
    mostrar_menu()

    opcion = input("Selecciona una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        ingresar_registro()
    elif opcion == "2":
        buscar_registro()
    elif opcion == "3":
        modificar_registro()
    elif opcion == "4":
        eliminar_registro()
    elif opcion == "5":
        guardar_registros()
        print("Registros guardados en base.csv")
    elif opcion == "6":
        print("Cerrando el programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")


