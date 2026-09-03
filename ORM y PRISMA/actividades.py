from sqlalchemy import Column, Integer, String, Boolean, create_engine,Float,or_
from sqlalchemy.orm import DeclarativeBase, Session
# 1. Definimos la clase (una sola vez)
class Base(DeclarativeBase):
    pass

class Productos (Base):
    __tablename__ = "Producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    categoria = Column(String)
    precio = Column (Float)
    stock = Column (Integer)
    activo = Column (Boolean)

engine = create_engine("sqlite:///mi_app.db")
Base.metadata.create_all(engine)
session = Session(engine)

2 #Ingresar lista o productos por separado.
productos = [
    Productos(
        nombre="Teclado mecanico",
        categoria="perifericos",
        precio=8500,
        stock=15,
        activo=True
    ),

    Productos(
        nombre="Mouse inalambrico",
        categoria="perifericos",
        precio=4200,
        stock=30,
        activo=True
    ),

    Productos(
        nombre="Monitor 24 pulgadas",
        categoria="monitores",
        precio=62000,
        stock=8,
        activo=True
    ),

    Productos(
        nombre="Auriculares bluetooth",
        categoria="audio",
        precio=12300,
        stock=20,
        activo=True
    ),

    Productos(
        nombre="Webcam Full HD",
        categoria="perifericos",
        precio=9800,
        stock=12,
        activo=True
    ),

    Productos(
        nombre="SSD 1TB",
        categoria="almacenamiento",
        precio=18500,
        stock=25,
        activo=True
    ),

    Productos(
        nombre="RAM 16GB",
        categoria="componentes",
        precio=15600,
        stock=18,
        activo=True
    ),

    Productos(
        nombre="Mousepad XL",
        categoria="perifericos",
        precio=2100,
        stock=40,
        activo=True
    ),

    Productos(
        nombre="Hub USB-C",
        categoria="accesorios",
        precio=5400,
        stock=6,
        activo=False
    ),

    Productos(
        nombre="Cable HDMI",
        categoria="accesorios",
        precio=1800,
        stock=50,
        activo=True
    )
]

if session.query(Productos).count() == 0:
    session.add_all(productos)
    session.commit()
    
3  #productos_perifericos = session.query(Productos).filter(
#    Productos.categoria == "perifericos"
#).all()

#for producto in productos_perifericos:
#    print(producto.nombre, "-", producto.precio)

4  #productos_caros = session.query(Productos).filter(
#    Productos.precio > 10000
#).order_by(
#    Productos.precio.desc()
#).all()
#for producto in productos_caros:
#    print(producto.nombre, "-", producto.precio)



5 #productos_stock = session.query(Productos).filter(
#    Productos.stock <= 12,
#    Productos.activo == True).all()
#for producto in productos_stock:
#    print(producto.nombre, "-", producto.stock)


6 #productos_precio = session.query(Productos).filter(
   # Productos.precio >=5000).filter(
    #Productos.precio <= 20000
#).all()
#for producto in productos_precio:
#    print(producto.nombre, "-", producto.precio)

7 #producto_caro = session.query(Productos).order_by(
#    Productos.precio.desc()
#).first()

#print(producto_caro.nombre, "-", producto_caro.precio)

8 #productos_inactivos = session.query(Productos).filter(
#    Productos.activo == False
#).all()

#for producto in productos_inactivos:
#    print(producto.nombre, "-", producto.precio)


9 #productos_categorias = session.query(Productos).filter(
#    or_(
#        Productos.categoria == "audio",
#        Productos.categoria == "componentes"
#    )
#).all()

#for producto in productos_categorias:
#    print(producto.nombre, "-", producto.categoria)

10 #productos_con_a = session.query(Productos).filter(
#    Productos.nombre.contains("a")
#).all()

#for producto in productos_con_a:
#    print(producto.nombre)

#print("Cantidad:", len(productos_con_a))

11 #productos_m = session.query(Productos).filter(
#    Productos.nombre.startswith("M")
#).all()

#for producto in productos_m:
#    print(producto.nombre)




# 2. Consultamos como si fueran objetos Python (filtrar tablas aca.!)
#with Session(engine) as session:
#    usuarios = session.query(Usuario) \
#    .filter(Usuario.activo == True) \
#    .all()
#for u in usuarios:
#    print(u.nombre, u.email) # ← atributos reales, no índices