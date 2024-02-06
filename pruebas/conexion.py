import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

try:
    mydb = client["prueba"]
    mycollection = mydb["coleccionprueba"]
    print("Conexión a MongoDB local establecida con éxito.")
except Exception as e:
    print(f"Error al conectar a MongoDB local: {str(e)}")
