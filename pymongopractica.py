import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.list_database_names())
print("Introduce base de datos a trabajar")
dbelec = input()  # eleccion base de datos
mydb = myclient[dbelec]

dblist = myclient.list_database_names()  # listado de todas las base de datos
if dbelec in dblist:
    print("base datos existente")
# myclient.close()  # cierra la conexion


# creacion de coleccion(hay que insertar un documento para q se cree)
print(mydb.list_collection_names())  # imprime las colecciones
print("Introduce coleccion")
creaColeccion = input()
listaColecciones = mydb.list_collection_names()
mycol = mydb[creaColeccion]
if creaColeccion in listaColecciones:
    print("coleccion existente")
for documento in mycol.find():
    print(documento)
# insertar un documento

campo1 = input("Introduce campo 1 \n")
valor1 = input("Introduce valor 1 \n")
campo2 = input("Introduce campo 1 \n")
valor2 = input("Introduce valor 1 \n")
insertado = mycol.insert_one({campo1: valor1, campo2: valor2})
print(insertado.inserted_id)
