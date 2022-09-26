import pymysql

def obtener_conexion():
    return pymysql.connect(host='localhost', user='root', password='', db='repuestosdb', port= 3307)