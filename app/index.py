from flask import Flask, render_template, request, redirect, flash
from controller import inventario, cliente, registro_venta, reportes
from controller import conexion
import datetime





app = Flask(__name__, template_folder='template')

app.config.from_mapping( #para evitar vulnerabilidades
    SECRET_KEY = 'llavesecreta'
)




#INVENTARIO
@app.route("/")
@app.route("/index_inventario")
def index_inventario():
    productos= inventario.listar_inventario()

    return render_template("inventario/tabla-inventario.html", productos=productos)

@app.route("/agregar_inventario")
def form_inventario():
  return render_template("inventario/registro-inventario.html")


@app.route("/add_inventario", methods=["POST"]) 
def add_inventario():

    stock_producto = request.form['stock_producto']
    nombre= request.form['nombre']
    categoria= request.form['categoria']
    proveedor= request.form['proveedor']
    precio= request.form['precio']
    serie= request.form['serie']

    pago_adquisicion = request.form['pago_adquisicion']
    pago_almacen = request.form['pago_almacen']
   
    
    try:
      inventario.insertar_inventario(nombre,precio, serie, pago_adquisicion, pago_almacen, stock_producto, categoria, proveedor)
      flash('Proceso realizado exitosamente', 'success')
    except:
      flash('Un error ha ocurrido', 'error')
    return redirect("/index_inventario")

@app.route("/eliminar_inventario", methods = ['POST'])
def eliminar_inventario():
    try:
     inventario.eliminar_inventario(request.form['id'])
     flash('Proceso realizado exitosamente', 'success')
    except:
     flash('Un error ha ocurrido', 'error')
    return redirect('/index_inventario')

@app.route("/form_editar_inventario/<id>") #devuelve el producto del inventario que se quiere editar dependiendo del id
def editar_inventario(id):
    producto = inventario.listar_inventario_id(id)
    return render_template("inventario/editar-inventario.html", producto = producto[0])

@app.route("/actualizar_inventario", methods = ['POST'])
def actualizar_inventario():
    id = request.form["id"]
    stock_producto = request.form['stock_producto']
    nombre= request.form['nombre']
    precio= request.form['precio']
    serie= request.form['serie']
    proveedor= request.form['proveedor']
    categoria = request.form['categoria']
    pago_almacen = request.form['pago_almacen']
    pago_adquisicion = request.form['pago_adquisicion']
    
    try:
      inventario.actualizar_inventario(nombre, precio, serie, pago_almacen, pago_adquisicion, stock_producto, categoria, proveedor, id)
      flash('Proceso realizado exitosamente', 'success')
    except:
      flash('Un error ha ocurrido', 'error')
    return redirect("/index_inventario")



#CLIENTE
@app.route("/clientes")
def clientes():
  client= cliente.listar_cliente()
  return render_template("cliente/tabla-cliente.html", client=client)
 
#REGISTRO VENTA

@app.route("/agregar_registroventa")
def form_registroventa():
 return render_template("registro_venta/registro_registroventa.html")

@app.route("/ingresar_registroventa", methods = ['POST'])
def ingresar_registroventa():
   total_precio = 0.0
   id_inventario = request.form['id_inventario']
   id_cliente = request.form['id_cliente']
  
   if id_inventario != '' and id_cliente != '':
        inv_ventas = inventario.listar_inventario_id(id_inventario)
        clint_ventas = cliente.listar_cliente_id(id_cliente)
        
        if type(inv_ventas) == tuple and type(clint_ventas) == tuple:
            #Al ingresar id se muestra la infrmacion que tienen los dos datos
           
            cantidad_venta = request.form['cantidad_venta']
            
            if int(cantidad_venta) <= int(inv_ventas[0][4]):
                total_precio = int(cantidad_venta) * inv_ventas[0][2]
                
                registro_venta.insertar_registroventa(id_cliente, id_inventario, cantidad_venta, total_precio)
                flash('Proceso realizado exitosamente', 'success')
               
                return redirect('/tabla_registroventa')
            else:
                flash('Un error ha ocurrido', 'error')
        else: 
         if inv_ventas == None:
           flash('Un error ha ocurrido', 'error')
             
        


@app.route("/tabla_registroventa")
def tabla_registroventa():
    ventas = registro_venta.listar_registroventa()
    cliente_ventas= cliente.listar_cliente()
    inventario_ventas = inventario.listar_inventario()
    return render_template ("registro_venta/registro_registroventa.html", ventas = ventas, cliente_ventas = cliente_ventas, inventario_ventas = inventario_ventas)

@app.route("/form_editar_registroventa/<id>") # lo que hace es devolver el registro que se quiere editar dependientdo del ID
def editar_venta(id):
    venta = registro_venta.listar_registroventa_id(id)
    conex = conexion.obtener_conexion()

    cliente_venta = []
    inventario_venta = []
    with conex.cursor() as cur:
     
      cur.execute("SELECT *  FROM cliente ")
      cliente_venta = cur.fetchall()
      cur.execute("SELECT *  FROM gestion_inventario ")
      inventario_venta = cur.fetchall()
    conex.close()
    return render_template("registro_venta/editar_venta.html", venta=venta, cliente_venta = cliente_venta, inventario_venta = inventario_venta )

@app.route("/actualizar-registroventa", methods = ['POST'])
def actualizar_venta():
   
   total_precio = 0.0
   id = request.form["id"]
   id_inventario = request.form['id_inventario']
   id_cliente = request.form['id_cliente']
 
   
   if id_inventario != '' and id_cliente != '':
        inv_venta = inventario.listar_inventario_id(id_inventario)
        clint_venta = cliente.listar_cliente_id(id_cliente)
        
        if type(inv_venta) == tuple and type(clint_venta) == tuple:
            #Al ingresar id se muestra la infrmacion que tienen los dos datos
           
            cantidad_venta = request.form['cantidad_venta']
            
            if int(cantidad_venta) <= int(inv_venta[0][4]):
                total_precio = int(cantidad_venta) * inv_venta[0][2]
                
                registro_venta.actualizar_registroventa(id_cliente, id_inventario, cantidad_venta, total_precio, id)
                flash('Proceso realizado exitosamente', 'success')
                
                return redirect('/tabla_registroventa')
            else:
                flash('Un error ha ocurrido', 'error')
        else: 
           if inv_venta == None:
            flash('Un error ha ocurrido', 'error')

#REPORTES


@app.route("/reportes-inventario-sem")
def reporte_inventario_sem():
    try:
        
        fechaInicial= datetime.date.today()

        fechaSem= datetime.datetime(2022, 10, 2)
        
        rep_inventario_sem=[]
        costoTotal_sem = 0.0
        report_inventario = inventario.listar_inventario()
        
        if fechaSem == fechaInicial : 
                    
            for result in report_inventario:
            
                costoTotal_sem = costoTotal_sem + result[5] + result[6]
                id_inventario = result[0]

                reportes.insertar_reporteInventarioSem(id_inventario, costoTotal_sem)
        else:
            flash('No ha transcurrido el tiempo', 'time')           
        rep_inventario_sem = reportes.listar_reporteInventarioSem() 
    
    except Exception as e:
        flash('Un error ha ocurrido', 'error')
        print(e)
    return render_template("reportes/semanales/reportes-inventario-sem.html", rep_inventario_sem = rep_inventario_sem)

@app.route("/reportes-inventario-mes")
def reporte_inventario_mes():
    try:
        
        fechaInicial= datetime.date.today()
        fechaMes= datetime.datetime(2022, 10, 25)

        costoTotal_mes = 0.0
        rep_inventario_mes = []
        report_inventario = inventario.listar_inventario()
        
        if fechaMes == fechaInicial: 
                    
            for result in report_inventario:
            
                costoTotal_mes = costoTotal_mes + result[5] + result[6]
                id_inventario = result[0]
                
                reportes.insertar_reporteInventarioMes(id_inventario, costoTotal_mes)              
        else:
            flash('No ha transcurrido el tiempo', 'time')         
        rep_inventario_mes = reportes.listar_reporteInventarioMes()     
    except Exception as e:
        flash('Un error ha ocurrido', 'error')
        print(e)
    return render_template("reportes/mensuales/reportes-inventario-mes.html", rep_inventario_mes = rep_inventario_mes)


@app.route("/reportes-deficit-sem")
def reporte_deficit_sem():
    try:
        

        rep_defProductSem =[]
        costoTotal_sem = 0.0
        defict_totalSem = 0.0
        
        report_inventario = inventario.listar_inventario()

        
        
        fechaInicial= datetime.date.today()

        fechaSem= datetime.datetime(2022, 10, 2)
        
        if fechaSem == fechaInicial: 
                    
            for result in report_inventario:
            
                costoTotal_sem = costoTotal_sem + result[5] + result[6]
                defict_totalSem = costoTotal_sem - result[2]
                id_inventario = result[0]
                reportes.insertar_DefProductSem(id_inventario, defict_totalSem)
        else:
            flash('No ha transcurrido el tiempo', 'time')             
        rep_defProductSem = reportes.listar_DefProductSem()    
    except Exception as e:
       flash('Un error ha ocurrido', 'error')
       print(e)
    return render_template("reportes/semanales/reportes-deficit-sem.html", rep_defProductSem = rep_defProductSem)

@app.route("/reportes-deficit-mes")
def reporte_deficit_mes():
    try:
        

        costoTotal_mes = 0.0
        defict_totalMes = 0.0
        report_inventario = inventario.listar_inventario()

        
        fechaInicial= datetime.date.today()
        fechaMes= datetime.datetime(2022, 10, 25)
        
        if fechaMes == fechaInicial:  
                    
            for result in report_inventario:
            
                costoTotal_mes = costoTotal_mes + result[5] + result[6]
                defict_totalMes = costoTotal_mes - result[2]
                id_inventario = result[0]
                reportes.insertar_DefProductMes(id_inventario, defict_totalMes)
        else:
            flash('No ha transcurrido el tiempo', 'time')             
        rep_defProductMes = reportes.listar_DefProductMes()
    
    except:
       flash('Un error ha ocurrido', 'error')
    return render_template("reportes/mensuales/reportes-deficit-mes.html", rep_defProductMes = rep_defProductMes)

@app.route("/reportes-stado-sem")
def reporte_stado_sem():
    try:
        
        rep_stCuentaSem=[]

        acum = 0.0
        saldoActual_sem = 0.0
        report_ventas = registro_venta.listar_registroventa()
        
        
        fechaInicial= datetime.date.today()

        fechaSem= datetime.datetime(2022, 10, 2)
        
        if fechaSem == fechaInicial:  
                    
            for result in report_ventas:
            
                saldoActual_sem = saldoActual_sem + result[4] 
                acum = acum + saldoActual_sem
                id_registro_venta = result[0]

                reportes.insertar_stadoCuentaSem(id_registro_venta, saldoActual_sem)
        else:
            flash('No ha transcurrido el tiempo', 'time')             
        rep_stCuentaSem = reportes.listar_stadoCuentaSem()
        print(acum)
    except Exception as e:
       flash('Un error ha ocurrido', 'error')
       print (e)
    return render_template("reportes/semanales/reportes-stado-sem.html", rep_stCuentaSem = rep_stCuentaSem)

@app.route("/reportes-stado-mes")
def reporte_stado_mes():
    try:
        
        rep_stCuentaMes=[]
        acum = 0.0
        saldoActual_Mes = 0.0
        report_ventas = registro_venta.listar_registroventa()
        
        
        fechaInicial= datetime.date.today()
        fechaMes= datetime.datetime(2022, 10, 25)
        
        if fechaMes == fechaInicial: 
                    
            for result in report_ventas:
            
                saldoActual_Mes = saldoActual_Mes - result[4] 
                acum = acum + saldoActual_Mes
                id_registro_venta = result[0]

                reportes.insertar_stadoCuentaMes(id_registro_venta, saldoActual_Mes)
        else:
            flash('No ha transcurrido el tiempo', 'time')             
        rep_stCuentaMes = reportes.listar_stadoCuentaMes()
        print (acum)
    except Exception as e:
       flash('Un error ha ocurrido', 'error')
       print(e)

    return render_template("reportes/mensuales/reportes-stado-mes.html", rep_stCuentaMes = rep_stCuentaMes)

@app.route("/reportes-ventas-sem")
def reporte_ventas_sem():
    try:
        
      
        venta_totalSem = 0.0
        report_ventas = registro_venta.listar_registroventa()
        acum = 0.0
        

        
        fechaInicial= datetime.date.today()

        fechaSem= datetime.datetime(2022, 10, 2)
        
        if fechaSem == fechaInicial: 
                    
            for result in report_ventas:
                acum = result[4]
                venta_totalSem = (acum / result[4]) * 100

                
                id_registro_venta = result[0]

                reportes.insertar_VentasSem(id_registro_venta, venta_totalSem)
        else:
            flash('No ha transcurrido el tiempo', 'time')             
        rep_ventasSem = reportes.listar_VentasSem()
    
    except:
       flash('Un error ha ocurrido', 'error')
    return render_template("reportes/semanales/reportes-ventas-sem.html", rep_ventasSem = rep_ventasSem)

@app.route("/reportes-ventas-mes")
def reporte_ventas_mes():
    try:
        
      
        venta_totalMes = 0.0
        report_ventas = registro_venta.listar_registroventa()
        acum = 0.0
        

        
        fechaInicial= datetime.date.today()
        fechaMes= datetime.datetime(2022, 10, 25)
        
        if fechaMes == fechaInicial: 
                    
            for result in report_ventas:
                acum = result[4]
                venta_totalMes = (acum / result[4]) * 100

                
                id_registro_venta = result[0]

                reportes.insertar_VentasMes(id_registro_venta, venta_totalMes)
        else:
            flash('No ha transcurrido el tiempo', 'time')              
        rep_ventasMes = reportes.listar_VentasMes()
    
    except:
      flash('Un error ha ocurrido', 'error')
    return render_template("reportes/mensuales/reportes-ventas-mes.html", rep_ventasMes = rep_ventasMes)


if __name__ == '__main__':
 app.run(host='localhost', port=5000, debug= True)
 