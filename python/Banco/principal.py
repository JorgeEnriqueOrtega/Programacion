from Login import *

opc = 0
while opc != 3:
    print("""Menu Inicial
        1. Entrar al sistema
        2. Gestionar Sistema
        3. Salir
            """)
    opc = int(input("Opcion: "))
    if opc == 1:
        sesion = Login()
        sesion.iniciar_sesion()
    elif opc == 2:
        print("""Menu de CSV
              1. Generar csv de clientes
              2. Generar csv de ejecutivos
              """)
        csv = int(input("Opcion: "))
        if csv == 1:
            df_cliente_global = Banco.generar_csv_clientes()
        elif csv == 2:
            df_ejecutivo_global = Banco.generar_csv_ejecutivos()
            df_ejecutivo_global = MenuEjecutivo.registrar_ejecutivo_nuevo(df_ejecutivo_global)
        df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
        df_ejecutivo_global, diccionario_ejecutivos = Banco.lectura_ejecutivos()
