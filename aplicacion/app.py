
from imp import reload
import os

from os import abort
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, null

from werkzeug.utils import redirect
import config
from forms import *
from funciones import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A0Zr98j/asdf3422a3+/*?)$/abSD3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object( config )


db = SQLAlchemy( app )

# esta importación se hace despues de la conexion a la BD sino, no obtendremos nada.

from models import *

@app.route( '/', methods=['GET', 'POST'] )
def inicio():
    return render_template("inicio.html")


####################### CLIENTES #####################################

@app.route('/Clientes', methods=['GET', 'POST'] )
def clientes():
    clientes = cliente.query.all()
    return render_template("clientes.html", clientes=clientes)


#Creacion de nuevo cliente.
@app.route('/Clientes/New', methods=['GET', 'POST'])
def clientes_new():

    cli = cliente()
    #recopilacion de datos del cliente
    formNewCliente = formCliente()

    if formNewCliente.submit.data and formNewCliente.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators
    
      #Creacion del cliente para subirlo
        cl = cliente(Empresa=formNewCliente.Empresa.data,
                        CifNif=formNewCliente.CifNif.data,
                        Direccion=formNewCliente.Direccion.data,
                        CP=formNewCliente.CP.data,
                        Ciudad=formNewCliente.Ciudad.data,
                        Provincia=formNewCliente.Provincia.data,
                        Telefono=formNewCliente.Telefono.data,
                        Email=formNewCliente.Email.data,
                        Contacto=formNewCliente.Contacto.data,
                        Baja=formNewCliente.Baja.data)


        db.session.add(cl)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewCliente.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("clientes_new.html", form=formNewCliente)


@app.route( '/Clientes/<id>/edit', methods=["get", "post"] )
def clientes_edit(id):
    clien = cliente.query.get(id)
    if clien is None:
        abort( 404 )

    formEditCliente = formCliente(obj=clien)
   

    if formEditCliente.validate_on_submit():
        formEditCliente.populate_obj( clien )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "clientes_new.html", form=formEditCliente )


####################### PROVEEDORES #####################################
@app.route('/Proveedores', methods=['GET', 'POST'] )
def proveedores():
    proveedores = proveedor.query.all()
    return render_template("proveedores.html", proveedores=proveedores)

#Creacion de nuevo proveedor.
@app.route('/Proveedores/New', methods=['GET', 'POST'])
def proveedores_new():

    prv = proveedor()
    #recopilacion de datos del proveedor
    formNewProveedor = formProveedor()

    if formNewProveedor.submit.data and formNewProveedor.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators
    
      #Creacion del proveedor para subirlo
        pv = proveedor(Empresa=formNewProveedor.Empresa.data,
                        CifNif=formNewProveedor.CifNif.data,
                        Direccion=formNewProveedor.Direccion.data,
                        CP=formNewProveedor.CP.data,
                        Ciudad=formNewProveedor.Ciudad.data,
                        Provincia=formNewProveedor.Provincia.data,
                        Telefono=formNewProveedor.Telefono.data,
                        Email=formNewProveedor.Email.data,
                        Contacto=formNewProveedor.Contacto.data,
                        Baja=formNewProveedor.Baja.data)


        db.session.add(pv)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewProveedor.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("proveedores_new.html", form=formNewProveedor)


@app.route( '/Proveedores/<id>/edit', methods=["get", "post"] )
def proveedores_edit(id):
    prv = proveedor.query.get(id)
    if prv is None:
        abort( 404 )

    formEditProveedor = formProveedor(obj=prv)
   

    if formEditProveedor.validate_on_submit():
        formEditProveedor.populate_obj( prv )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "proveedores_new.html", form=formEditProveedor )


####################### TRABAJADORES #####################################

@app.route('/Trabajadores', methods=['GET', 'POST'] )
def trabajadores():
    trabajadores = trabajador.query.all()
    return render_template("trabajadores.html", trabajadores=trabajadores)

#Creacion de nuevo trabajador.
@app.route('/Trabajadores/New', methods=['GET', 'POST'])
def trabajadores_new():

    trb = trabajador()
    #recopilacion de datos del trabajador
    formNewTrabajador = formTrabajador()

    if formNewTrabajador.submit.data and formNewTrabajador.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators

      #Creacion del trabajador para subirlo
        trb = trabajador(Nombre=formNewTrabajador.Nombre.data,
                        Apellidos=formNewTrabajador.Apellidos.data,
                        Telefono=formNewTrabajador.Telefono.data,
						Baja = formNewTrabajador.Baja.data,
                        Rol = formNewTrabajador.Rol.data,
                        Usuario=formNewTrabajador.Usuario.data,
                        Contrasena = None
                        )

        print(trb.Baja, ' ', trb.Usuario)
        db.session.add(trb)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewTrabajador.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("trabajadores_new.html", form=formNewTrabajador)


@app.route( '/Trabajadores/<id>/edit', methods=["get", "post"] )
def trabajadores_edit(id):
    trb = trabajador.query.get(id)
    if trb is None:
        abort( 404 )

    formEditTrabajador = formTrabajador(obj=trb)
   
    if formEditTrabajador.validate_on_submit():
        formEditTrabajador.populate_obj( trb )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "trabajadores_new.html", form=formEditTrabajador )


####################### UNIDADES #####################################

@app.route('/UnidadMedida', methods=['GET', 'POST'] )
def unidades():
    unidades = unidad.query.all()
    return render_template("unidadMedida.html", unidades=unidades)

@app.route('/UnidadMedida/New', methods=['POST'])
def unidades_new():
    un = unidad()
    if request.method == 'POST':
        un.Unidad = request.form['Unidad']
        db.session.add(un)
        db.session.commit()
        return redirect(url_for("inicio"))
    else:
        return render_template("unidadMedida.html")

@app.route( '/UnidadMedida/<id>/edit', methods=["get", "post"] )
def unidades_edit(id):
    un = unidad.query.get(id)
    if un is None:
        abort( 404 )

    formEditUnidad = formUnidad(obj=un)
   
    if formEditUnidad.validate_on_submit():
        formEditUnidad.populate_obj( un )
        db.session.commit()
        return redirect( url_for( "inicio" ) )
    else:
        return render_template("unidadMedida_edit.html", form=formEditUnidad)
   

####################### PRODUCTOS #####################################


@app.route('/Productos', methods=['GET', 'POST'] )
def productos():
    productos = producto.query.all()
    um = unidad.query.all()
    return render_template("productos.html", productos=productos, unidadMedida=um)

#Creacion de nuevo producto.
@app.route('/Productos/New', methods=['GET', 'POST'])
def productos_new():

    prd = producto()
    #recopilacion de datos del producto
    formNewProducto = formProducto()

    # Añado mi listado de medidas al select / choices definidos en el form de Producto 
    formNewProducto.idUnidad.choices = listaunidades()


    if formNewProducto.submit.data and formNewProducto.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators
    
      #Creacion del producto para subirlo
        prd = producto(Nombre=formNewProducto.Nombre.data,
                        Precio=formNewProducto.Precio.data,
                        idUnidad=formNewProducto.idUnidad.data)

        print("id unidad: ", formNewProducto.idUnidad.data)

        db.session.add(prd)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewProducto.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("productos_new.html", form=formNewProducto )

@app.route( '/Productos/<id>/edit', methods=["get", "post"] )
def productos_edit(id):
    prd = producto.query.get(id)
    if prd is None:
        abort( 404 )

    formEditProducto = formProducto(obj=prd)
    
    # Añado mi listado de medidas al select / choices definidos en el form de Producto 
    # ver funciones.listaunidades. 
    formEditProducto.idUnidad.choices= listaunidades()
   

    if formEditProducto.validate_on_submit():
        formEditProducto.populate_obj( prd )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "productos_new.html", form=formEditProducto )

####################### UNIDADES #####################################

@app.route('/Estado', methods=['GET', 'POST'] )
def estados():
    estados = estado.query.all()
    return render_template("estados.html", estados=estados)

@app.route('/Estado/New', methods=['POST'])
def estados_new():
    es = estado()
    if request.method == 'POST':
        es.Estado = request.form['Estado']
        db.session.add(es)
        db.session.commit()
        return redirect(url_for("inicio"))
    else:
        return render_template("estados.html")

@app.route( '/Estado/<id>/edit', methods=["get", "post"] )
def estados_edit(id):
    es = estado.query.get(id)
    if es is None:
        abort( 404 )

    formEditEstado = formEstado(obj=es)
    
    if formEditEstado.validate_on_submit():
        print("estoy aqui")
        formEditEstado.populate_obj( es )
        db.session.commit()
        return redirect( url_for( "inicio" ) )
    else:
        return render_template("estados_edit.html", form=formEditEstado)


####################### ALBARANES #####################################

@app.route('/Albaranes', methods=['GET', 'POST'] )
def albaranes():
    albaranes = albaran.query.all()
    proveedores = proveedor.query.all()
    return render_template("albaranes.html", albaranes=albaranes, proveedores=proveedores)

#Creacion de nuevo albaran.
@app.route('/Albaranes/New', methods=['GET', 'POST'])
def albaranes_new():

    alb = albaran()
    #recopilacion de datos del albaran
    formNewAlbaran = formAlbaran()
	

	# Añado el listado de los proveedores al formulario.
    # He creado un archivo donde recojo las funciones que utilizo. 
    formNewAlbaran.idProveedor.choices = listaproveedores()

    if formNewAlbaran.submit.data and formNewAlbaran.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators

      #Creacion del albaran para subirlo
        alb = albaran(Numero=formNewAlbaran.Numero.data,
                       idProveedor=formNewAlbaran.idProveedor.data)             

        db.session.add(alb)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewAlbaran.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("albaranes_new.html", form=formNewAlbaran)


@app.route( '/Albaranes/<id>/edit', methods=["get", "post"] )
def albaranes_edit(id):
    alb = albaran.query.get(id)
    if alb is None:
        abort( 404 )

    formEditAlbaran = formAlbaran(obj=alb)	
	
	# Añado el listado de los proveedores al formulario
    formEditAlbaran.idProveedor.choices = listaproveedores()
   
    if formEditAlbaran.validate_on_submit():
        formEditAlbaran.populate_obj( alb )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "albaranes_new.html", form=formEditAlbaran )



####################### TAREAS #####################################

@app.route('/Tareas', methods=['GET', 'POST'] )
def tareas():
    tareas = tarea.query.all()
    obras = obra.query.all()
    return render_template("tareas.html", tareas=tareas, obras=obras)

#Creacion de nuevo tarea.
@app.route('/Tareas/New', methods=['GET', 'POST'])
def tareas_new():

    tar = tarea()
    #recopilacion de datos del tarea
    formNewTarea = formTarea()
	

	# Añado el listado de los obras al formulario.
    # He creado un archivo donde recojo las funciones que utilizo. 
   
    formNewTarea.idObra.choices = listaobras()

    if formNewTarea.submit.data and formNewTarea.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators


      #Creacion del tarea para subirlo
        tar = tarea(Descripcion=formNewTarea.Descripcion.data,
					EstadoTarea = formNewTarea.EstadoTarea.data,
					Notas = formNewTarea.Notas.data,
                    idObra=formNewTarea.idObra.data)             

        db.session.add(tar)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewTarea.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("tareas_new.html", form=formNewTarea)


@app.route( '/Tareas/<id>/edit', methods=["get", "post"] )
def tareas_edit(id):
    tar = tarea.query.get(id)
    if tar is None:
        abort( 404 )

    formEditTarea = formTarea(obj=tar)	
	
	# Añado el listado de los obras al formulario
    formEditTarea.idObra.choices = listaobras()
   
    if formEditTarea.validate_on_submit():
        formEditTarea.populate_obj( tar )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

    return render_template( "tareas_new.html", form=formEditTarea )

####################### OBRAS #####################################

@app.route('/Obras', methods=['GET', 'POST'] )
def obras():
    obras = obra.query.all()
    clientes = cliente.query.all()
    estados = estado.query.all()
    return render_template("obras.html", obras=obras, clientes=clientes, estados=estados)


#Creacion de nuevo obra.
@app.route('/Obras/New', methods=['GET', 'POST'])
def obras_new():

    ob = obra()
    #recopilacion de datos del obra
    formNewObra = formObra()
	
	# Añado el listado de los obras al formulario.
    # He creado un archivo donde recojo las funciones que utilizo. 
   
    formNewObra.idCliente.choices = listaclientes()
    formNewObra.idEstado.choices = listaestados()
    formAddProducto = formObraProducto()
    

    if formNewObra.submit.data and formNewObra.validate():
            #validacion de los campos según nuestro form, que hemos puesto Validators


      #Creacion del obra para subirlo
        ob = obra(Nombre=formNewObra.Nombre.data,
					idEstado = formNewObra.idEstado.data,
					idCliente = formNewObra.idCliente.data,
                    NumeroPedido=formNewObra.NumeroPedido.data)             

        db.session.add(ob)
        db.session.commit()
        return redirect(url_for("inicio"))
    elif formNewObra.btn_cancel.data:
        return redirect(url_for("inicio"))
    else:
        return render_template("obras_new.html", form=formNewObra, obr=ob, formularioProductos = formAddProducto)


@app.route( '/Obras/<id>/edit', methods=["get", "post"] )
def obras_edit(id):

    #Obra seleccionada.
    ob = obra.query.get(id)
    if ob is None:
        abort( 404 )

    #asigno todos los campos con los que he recuperado de la query. 
    formEditObra = formObra(obj=ob)	
	
	# Añado el listado de los obras al formulario
    formEditObra.idCliente.choices = listaclientes()
    formEditObra.idEstado.choices = listaestados()

    #en este form tengo que añadir todos los productos que se habian utilizado. hay que populate
    formEditProducto = formObraProducto()
    formEditProducto.idProducto.choices = listaproductos()

    productosSeleccionados = db.session.query(obraproducto.idProducto, db.func.sum(obraproducto.Cantidad)).group_by(obraproducto.idProducto, obraproducto.idObra).filter(obraproducto.idObra==id).all()
    prod = listaproductos()
  
    for a in productosSeleccionados:
       for p in prod:
           if a[1] == p[0]:
               print(a[0], " -",p[1], " -" , a[2])

    #Tengo que rellenar el form con los datos 

    #Hago una select en la tabla obraproducto por el id de obra, y recojo todos los productos. 
    #productosSeleccionados = obraproducto.query.filter_by(idObra=id).all()
    products = producto.query.all()
    #for ps in productosSeleccionados:
    #    print(ps.Cantidad)


    if formEditProducto.btn_add.data:
        # Añadimos un producto a la obra. 
      
    
        if formEditProducto.Cantidad.data > 0:
       
            if formEditProducto.idObra.data==None:
                formEditProducto.idObra.data = id
                obrPrd = obraproducto(Cantidad=formEditProducto.Cantidad.data,
                        idProducto = formEditProducto.idProducto.data,
                        idObra = formEditProducto.idObra.data)
    
                db.session.add(obrPrd)
                db.session.commit()
                
                productosSeleccionados = db.session.query(obraproducto.idProducto, db.func.sum(obraproducto.Cantidad)).group_by(obraproducto.idProducto, obraproducto.idObra).filter(obraproducto.idObra==id).all()

                
                formEditProducto.Cantidad.data = 0
                

                

    if formEditObra.submit.data:
        formEditObra.populate_obj( ob )
        db.session.commit()
        return redirect( url_for( "inicio" ) )

   
    formEditProducto.Cantidad.data = 0
    
   
    return render_template( "obras_new.html",
     form=formEditObra,
     obr = ob,
     formularioProductos=formEditProducto,
     productosSeleccionados=productosSeleccionados, 
     products= products )


if __name__ == '__main__':
    app.run()
