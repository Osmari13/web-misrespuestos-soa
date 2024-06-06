from .conexion import obtener_conexion


def insertar_inventario(nombre,precio, serie, pago_adquisicion, pago_almacen, stock_producto, categoria, proveedor):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
      cur.execute("INSERT INTO gestion_inventario(nombre, precio, serie,stock_producto,  pago_adquisicion, pago_almacen, categoria, proveedor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
      ( nombre, precio, serie, pago_adquisicion, pago_almacen, stock_producto, categoria, proveedor))
   conexion.commit()
   conexion.close()

def listar_inventario():
   conexion = obtener_conexion()
   productos = []
   with conexion.cursor() as cur:
      cur.execute("SELECT id, nombre, precio, serie, stock_producto,pago_adquisicion, pago_almacen,  categoria, proveedor, fecha_creacion, fecha_actual FROM gestion_inventario")
      productos = cur.fetchall()
   conexion.close()
   return productos

def eliminar_inventario(id):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
      cur.execute("DELETE from gestion_inventario WHERE id = %s", (id,))
   conexion.commit()
   conexion.close()

def listar_inventario_id(id):
   conexion = obtener_conexion()
   producto = None
   with conexion.cursor() as cur:
      cur.execute("SELECT id, nombre, precio, serie,stock_producto, pago_adquisicion, pago_almacen,  categoria, proveedor, fecha_actual FROM gestion_inventario WHERE id = %s", (id,))
      producto = cur.fetchall()
   conexion.close()
   return producto



def actualizar_inventario(nombre, precio, serie, pago_almacen, pago_adquisicion, stock_producto, categoria, proveedor,fecha_actual, id):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
      cur.execute("UPDATE gestion_inventario SET nombre = %s, precio = %s, serie = %s, pago_adquisicion = %s, pago_almacen = %s, stock_producto=%s, categoria = %s, proveedor=%s, fecha_actual=%s WHERE id = %s",
      (nombre, precio, serie,  pago_almacen, pago_adquisicion, stock_producto, categoria, proveedor, fecha_actual, id))
   conexion.commit()
   conexion.close()
