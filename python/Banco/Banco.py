from Cliente import Cliente
from Ejecutivo import Ejecutivo
import pandas as pd
from pathlib import Path

ruta_ejecutivos = Path(Path.home(), "registro_ejecutivos.csv")
ruta_clientes = Path(Path.home(), "registro_clientes.csv")


class Banco:

    @staticmethod
    def generar_csv_clientes():
        # Crear un DataFrame con la información de los clientes
        data = {'Nombre': [],
                'Apellido': [],
                'Fecha': [],
                'Correo': [],
                'Telefono': [],
                'Contrasenia': [],
                'Numero_Cuenta': [],
                'Saldo': [],
                'Apartado':[]}
        df_cliente = pd.DataFrame(data)
        df_cliente.to_csv(ruta_clientes, index = False)
        print(type(df_cliente))
        return df_cliente
    
    @staticmethod
    def registrar_cliente(usuario:Cliente, df_cliente:pd):
            new_row =pd.DataFrame ({'Nombre': [usuario.nombre],
            'Apellido': [usuario.apellido],
            'Fecha': [usuario.fecha],
            'Correo': [usuario.correo],
            'Telefono': [usuario.telefono],
            'Contrasenia': [usuario.contrasenia],
            'Numero_Cuenta': [usuario.numero_cuenta],
            'Saldo': [usuario.saldo],
            'Apartado': [usuario.apartado]})
            df_cliente = pd.concat([df_cliente, new_row], ignore_index = True)
            df_cliente.to_csv(ruta_clientes, index = False)
            return df_cliente 
    
    @staticmethod
    def lectura_clientes():
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto cliente}
        """
        df_cliente = pd.read_csv(ruta_clientes)
        personas_diccionario = {}
        for index, row in df_cliente.iterrows():
            usuario = Cliente(row['Nombre'], 
                                row['Apellido'], 
                                row['Fecha'], 
                                row['Correo'],
                                row['Telefono'],
                                row['Contrasenia'],
                                row['Numero_Cuenta'],
                                float(row['Saldo']),
                                row['Apartado'])
            personas_diccionario[int(row['Numero_Cuenta'])] = usuario
        print(df_cliente)
        print("-" * 100 + '\n')
        return df_cliente,personas_diccionario
    
    @staticmethod
    def guardar_mov_cliente(usuario: Cliente, df_cliente: pd):
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Nombre'] = usuario.nombre
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Apellido'] =usuario.apellido
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Correo'] =usuario.correo
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Telefono'] =usuario.telefono
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Contrasenia'] =usuario.contrasenia
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Saldo'] =usuario.saldo 
        df_cliente.loc[df_cliente['Numero_Cuenta'] == usuario.numero_cuenta, 'Apartado'] =usuario.apartado 
        return df_cliente
    
    @staticmethod
    def eliminar_cliente(numero_cuenta: str, df_ejecutivo: pd):
        """
        Elimina un cliente del DataFrame según su número de cuenta.

        Parameters:
            numero_cuenta (str): Número de cuenta del cliente a eliminar.
            df (pd.DataFrame): DataFrame que contiene la información de los clientes.

        Returns:
            pd.DataFrame: DataFrame actualizado sin el cliente eliminado.
        """
        df_ejecutivo = df_ejecutivo[df_ejecutivo['Numero_Cuenta'] != numero_cuenta]
        df_ejecutivo.to_csv(ruta_clientes, index=False)
        return df_ejecutivo

    @staticmethod
    def generar_csv_ejecutivos():
        # Crear un DataFrame con la información de los ejecutivos
        data = {'Nombre': [],
                'Apellido': [],
                'Fecha': [],
                'Correo': [],
                'Telefono': [],
                'Contrasenia': [],
                'Numero_Cuenta': [],
                'Puesto': [],
                'Sucursal': []}
        df_ejecutivo = pd.DataFrame(data)
        df_ejecutivo.to_csv(ruta_ejecutivos, index = False)
        print(type(df_ejecutivo))
        return df_ejecutivo
    
    @staticmethod
    def registrar_ejecutivo(usuario:Ejecutivo, df_ejecutivo:pd):
            new_row =pd.DataFrame ({'Nombre': [usuario.nombre],
            'Apellido': [usuario.apellido],
            'Fecha': [usuario.fecha],
            'Correo': [usuario.correo],
            'Telefono': [usuario.telefono],
            'Contrasenia': [usuario.contrasenia],
            'Numero_Cuenta': [usuario.numero_cuenta],
            'Puesto': [usuario.puesto],
            'Sucursal': [usuario.sucursal]})
            df_ejecutivo = pd.concat([df_ejecutivo, new_row], ignore_index = True)
            df_ejecutivo.to_csv(ruta_ejecutivos, index = False)
            return df_ejecutivo
    
    @staticmethod
    def lectura_ejecutivos():
        """Leera y guardara todos los datos del archivo .csv

        Returns:
            dict{Numero_cuenta: objeto ejecutivo}
        """
        df_ejecutivo = pd.read_csv(ruta_ejecutivos)
        personas_diccionario = {}
        for index, row in df_ejecutivo.iterrows():
            usuario = Ejecutivo(row['Nombre'], 
                                row['Apellido'], 
                                row['Fecha'], 
                                row['Correo'],
                                row['Telefono'],
                                row['Contrasenia'],
                                row['Numero_Cuenta'],
                                row['Puesto'],
                                row['Sucursal'])
            personas_diccionario[(row['Numero_Cuenta'])] = usuario
        print(df_ejecutivo)
        print("-" * 115 + '\n')
        return df_ejecutivo,personas_diccionario
    
    @staticmethod
    def guardar_mov_ejecutivos(usuario: Ejecutivo, df_ejecutivo: pd):
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Nombre'] = usuario.nombre
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Apellido'] =usuario.apellido
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Correo'] =usuario.correo
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Telefono'] =usuario.telefono
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Contrasenia'] =usuario.contrasenia
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Puesto'] =usuario.puesto
        df_ejecutivo.loc[df_ejecutivo['Numero_Cuenta'] == usuario.numero_cuenta, 'Sucursal'] =usuario.sucursal 
        return df_ejecutivo
    
    @staticmethod
    def guardar_clientes(df_clientes:pd):
        df_clientes.to_csv(ruta_clientes, index=False)

    @staticmethod
    def guardar_ejecutivos(df_ejecutivos):
        df_ejecutivos.to_csv(ruta_ejecutivos, index=False)
        

df_cliente_global, diccionario_clientes = Banco.lectura_clientes()
df_ejecutivo_global, diccionario_ejecutivos = Banco.lectura_ejecutivos()