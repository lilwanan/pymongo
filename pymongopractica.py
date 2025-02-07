import pymongo


def eleccionaccion():
    salir = True
    while salir:

        print("Introduce base de datos a trabajar",
              myclient.list_database_names())
        dbelec = input()  # eleccion base de datos
        mydb = myclient[dbelec]
        dblist = myclient.list_database_names()  # listado de todas las base de datos
        if dbelec in dblist:
            print("base datos existente")
        print("Introduce nombre de coleccion: ", mydb.list_collection_names())
        creacoleccion = input()
        listacolecciones = mydb.list_collection_names()
        mycol = mydb[creacoleccion]
        if creacoleccion in listacolecciones:
            print("coleccion existente")
        for documento in mycol.find():
            print(documento)

        print("""Selecciona accion
                1. INSERTAR
                2. CONSULTAR
                3. UPDATE
                4. DELETE
                5. SALIR""")
        eleccion = int(input())
        if (eleccion == 1):
            diccionario = busqueda_campos()
            resultadoinsert = mycol.insert_one(diccionario)
            print("Documento insertado", resultadoinsert.inserted_id)
        elif (eleccion == 2):
            resultado = busqueda_campos()
            multiple = input(
                "True para varios o False para uno ").lower == True
            result = find_document(mycol, resultado, multiple)
            if multiple:
                for documento in result:
                    print(documento)
            else:
                print(result)
        elif (eleccion == 3):
            print("Introduce valores que quieres actualizar ")
            consulta = busqueda_campos()
            print("Introduce nuevos valores a actualizar ")
            valores_actualizados = busqueda_campos()
            update_document(mycol, consulta, valores_actualizados)
            print("Documento actualizado")
        elif (eleccion == 4):
            print("Inserta valores a eliminar ")
            consulta = busqueda_campos()
            delete_document(mycol, consulta)
            print("Valores borradas")
        elif (eleccion == 5):
            print("Saliendo...")
            salir = False


def find_document(collection, elements, multiple=False):
    """ Función que obtiene uno o varios documentos dependiendo
         del valor de multiple
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)


def busqueda_campos():
    campos = {}
    print("Introduce campos o fin para finalizar ")
    while True:
        campo = input("Introduce nombre del campo o fin para finalizar ")
        if campo.lower() == "fin":
            break
        valor = input(f"Introduce el valor para el campo {campo} ")

        campos[campo] = valor
    return campos


def update_document(collection, query_elements, new_values):
    """ Función que actualiza un documento en una colección.
    """
    collection.update_one(query_elements, {'$set': new_values})


def delete_document(collection, query):
    """ Función para borrar un único documento de una colección.
    """
    collection.delete_one(query)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

eleccionaccion()


# myclient.close()  # cierra la conexion


# creacion de coleccion(hay que insertar un documento para q se cree)
