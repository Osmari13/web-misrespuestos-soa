from .conexion import obtener_conexion

def insertar_registroventa(id_cliente, id_inventario, cantidad_venta, total_precio):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO registro_venta(id_cliente, id_inventario, cantidad_venta, total_precio) VALUES (%s, %s, %s, %s)", ( id_cliente, id_inventario, cantidad_venta, total_precio))
   conexion.commit()
   conexion.close()

def listar_registroventa():
   conexion = obtener_conexion()
   ventas = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT *  FROM registro_venta ")
      ventas = cur.fetchall()
   conexion.close()
   return ventas

def listar_registroventa_id(id):
   conexion = obtener_conexion()
   venta = None
   with conexion.cursor() as cur:
     cur.execute("SELECT * FROM registro_venta WHERE id = %s ", (id,))
     venta = cur.fetchone()   
   conexion.close()

   return venta


def actualizar_registroventa(id_cliente, id_inventario, cantidad_venta, total_precio, id):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
      cur.execute("UPDATE registro_venta SET id_cliente = %s, id_inventario = %s, cantidad_venta = %s, total_precio = %s  WHERE id = %s", (id_cliente, id_inventario, cantidad_venta, total_precio, id))
   conexion.commit()
   conexion.close()
