from .conexion import obtener_conexion


def listar_cliente():
   conexion = obtener_conexion()
   clientes = []
   with conexion.cursor() as cur:
      cur.execute("SELECT id, name, telefono FROM cliente")
      clientes = cur.fetchall()
   conexion.close()
   return clientes

def listar_cliente_id(id):
   conexion = obtener_conexion()
   cliente = []
   with conexion.cursor() as cur:
      cur.execute("SELECT id, name, telefono FROM cliente WHERE id = %s",(id,))
      cliente = cur.fetchall()
   conexion.close()
   return cliente



