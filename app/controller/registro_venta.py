from .conexion import obtener_conexion


def insertar_registroventa(id_cliente, id_inventario, cantidad_venta, total_precio):
    conexion = obtener_conexion()
    with conexion.cursor() as cur:

        cur.execute(
            "INSERT INTO registro_venta(id_cliente, id_inventario, cantidad_venta, total_precio) VALUES (%s, %s, %s, %s)",
            (id_cliente, id_inventario, cantidad_venta, total_precio),
        )
    conexion.commit()
    conexion.close()


def listar_registroventa():
    conexion = obtener_conexion()
    ventas = []

    with conexion.cursor() as cur:
        cur.execute(
            "SELECT registro_venta.id,cliente.name, gestion_inventario.nombre, gestion_inventario.precio, registro_venta.cantidad_venta, registro_venta.total_precio,  registro_venta.fecha_creacion, registro_venta.fecha_actual, cliente.id, gestion_inventario.id  FROM registro_venta JOIN cliente ON registro_venta.id_cliente = cliente.id JOIN gestion_inventario ON registro_venta.id_inventario = gestion_inventario.id ORDER BY registro_venta.id DESC"
        )
        ventas = cur.fetchall()
    conexion.close()
    return ventas


def factura(id_cliente):
    conexion = obtener_conexion()
    ventas = []
    with conexion.cursor() as cur:
        cur.execute(
            "SELECT registro_venta.id ,cliente.name, gestion_inventario.nombre,registro_venta.cantidad_venta, registro_venta.total_precio,  registro_venta.fecha_creacion, registro_venta.fecha_actual, cliente.id, gestion_inventario.id FROM registro_venta JOIN cliente ON registro_venta.id_cliente = cliente.id JOIN gestion_inventario ON registro_venta.id_inventario = gestion_inventario.id WHERE cliente.id = %s",
            (id_cliente,),
        )
        ventas = cur.fetchall()
    conexion.close()
    return ventas


def listar_registroventa_id(id):
    conexion = obtener_conexion()
    venta = None
    with conexion.cursor() as cur:
        cur.execute(
            "SELECT registro_venta.id ,cliente.name, gestion_inventario.nombre,registro_venta.cantidad_venta, registro_venta.total_precio,  registro_venta.fecha_creacion, registro_venta.fecha_actual, cliente.id, gestion_inventario.id FROM registro_venta JOIN cliente ON registro_venta.id_cliente = cliente.id JOIN gestion_inventario ON registro_venta.id_inventario = gestion_inventario.id WHERE registro_venta.id = %s",
            (id,),
        )
        venta = cur.fetchall()
    conexion.close()

    return venta


def actualizar_registroventa(
    id_cliente, id_inventario, cantidad_venta, total_precio, fecha_actual, id
):
    conexion = obtener_conexion()
    with conexion.cursor() as cur:
        cur.execute(
            "UPDATE registro_venta SET id_cliente = %s, id_inventario = %s, cantidad_venta = %s, total_precio = %s, fecha_actual=%s  WHERE id = %s",
            (id_cliente, id_inventario, cantidad_venta, total_precio, fecha_actual, id),
        )
    conexion.commit()
    conexion.close()
