from .conexion import obtener_conexion

#GESTION DE INVENTARIO
def listar_reporteInventarioSem():
   conexion = obtener_conexion()
   rep_inventario_sem = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_inventario, costoTotal_sem  FROM reporte_costeinventario_sem ")
      rep_inventario_sem = cur.fetchall()
   conexion.close()
   return rep_inventario_sem

def insertar_reporteInventarioSem(id_inventario, costoTotal_sem):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_costeinventario_sem( id_inventario, costoTotal_sem) VALUES (%s, %s)",
      ( id_inventario, costoTotal_sem))
   conexion.commit()
   conexion.close()



def listar_reporteInventarioMes():
   conexion = obtener_conexion()
   rep_inventario_mes = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_inventario, costoTotal_mes  FROM reporte_costeinventario_mes ")
      rep_inventario_mes = cur.fetchall()
   conexion.close()
   return rep_inventario_mes

def insertar_reporteInventarioMes(id_inventario, costoTotal_mes):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_costeinventario_mes(id_inventario, costoTotal_mes) VALUES (%s, %s)",
      (id_inventario, costoTotal_mes))
   conexion.commit()
   conexion.close()



#DEFICIT DEL PRODUCTO

def listar_DefProductSem(): 
   conexion = obtener_conexion()
   rep_defProductSem = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_inventario, deficit_totalSem FROM reporte_deficitproduct_sem")
      rep_defProductSem = cur.fetchall()
   conexion.close()
   return rep_defProductSem

def insertar_DefProductSem(id_inventario, defict_totalSem):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_deficitproduct_sem(deficit_totalSem, id_inventario) VALUES (%s, %s)",
      (defict_totalSem, id_inventario))
   conexion.commit()
   conexion.close()




def listar_DefProductMes(): 
   conexion = obtener_conexion()
   rep_defProductMes = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_inventario, deficit_totalMes  FROM reporte_deficitproduct_mes")
      rep_defProductMes = cur.fetchall()
   conexion.close()
   return rep_defProductMes

def insertar_DefProductMes(id_inventario, deficit_totalMes):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_deficitproduct_mes(deficit_totalMes, id_inventario) VALUES (%s, %s)",
      (deficit_totalMes, id_inventario))
   conexion.commit()
   conexion.close()


#ESTADO DE CUENTA

def listar_stadoCuentaSem():
   conexion = obtener_conexion()
   rep_stCuentaSem = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_registro_venta, saldoActual_sem FROM reporte_stdcuenta_sem")
      rep_stCuentaSem = cur.fetchall()
   conexion.close()
   return rep_stCuentaSem

def insertar_stadoCuentaSem(id_registro_venta, saldoActual_sem):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_stdcuenta_sem(id_registro_venta, saldoActual_sem) VALUES (%s, %s)",
      (id_registro_venta, saldoActual_sem))
   conexion.commit()
   conexion.close()

def listar_stadoCuentaMes():
   conexion = obtener_conexion()
   rep_stCuentaMes = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_registro_venta, saldoActual_mes  FROM reporte_stdcuenta_mes")
      rep_stCuentaMes = cur.fetchall()
   conexion.close()
   return rep_stCuentaMes

def insertar_stadoCuentaMes(id_registro_venta, saldoActual_mes):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_stdcuenta_mes(id_registro_venta, saldoActual_mes) VALUES ( %s, %s)",
      (id_registro_venta, saldoActual_mes))
   conexion.commit()
   conexion.close()


#REGISTRO DE VENTAS  


def listar_VentasSem():
   conexion = obtener_conexion()
   rep_ventasSem = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_registro_venta, venta_totalSem  FROM reporte_gestionventas_sem ")
      rep_ventasSem = cur.fetchall()
   conexion.close()
   return rep_ventasSem

def insertar_VentasSem(id_registro_venta, venta_totalSem):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_gestionventas_sem(id_registro_venta, venta_totalSem) VALUES ( %s, %s)",
      (id_registro_venta, venta_totalSem))
   conexion.commit()
   conexion.close()


def listar_VentasMes():
   conexion = obtener_conexion()
   rep_ventasMes = []
   
   with conexion.cursor() as cur:
      cur.execute("SELECT id, id_registro_venta, venta_totalMes  FROM reporte_gestionventas_mes ")
      rep_ventasMes = cur.fetchall()
   conexion.close()
   return rep_ventasMes

def insertar_VentasMes(id_registro_venta, venta_totalMes ):
   conexion = obtener_conexion()
   with conexion.cursor() as cur:
  
      cur.execute("INSERT INTO reporte_gestionventas_mes(id_registro_venta, venta_totalMes ) VALUES ( %s, %s)",
      (id_registro_venta, venta_totalMes))
   conexion.commit()
   conexion.close()