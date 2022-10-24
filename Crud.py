import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.1.189",
    user="root",
    password="test",
    database="concesionario"
)
confirmacion = 0

while (confirmacion != "x"):
    confirmacion = input("Introduzca 1 VER TODO, 2 INSERTAR, 3 ELIMINAR, 4 ACTUALIZAR, 5 BUSQUEDA AVANZADA o x para salir: ")
    if (confirmacion == "1"):
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM coches")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        confirmacion = input("Introduzca 2 si quiere insertar datos, 1 para volver o x para salir: ")

    elif (confirmacion == "2"):
        mycursor = mydb.cursor()
       
        marca = input("Introdzuca la marca: ")
        modelo = input("Introduzca el modelo: ")
        potencia = input("introduzca la potencia: ")
        precio = input("introduzca el precio: ")
       
      
        sql = "INSERT INTO coches ( marca, modelo, potencia, precio ) VALUES ( %s, %s, %s, %s)"
        val = (marca, modelo, potencia, precio)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    elif (confirmacion == "3"):
        ID = input("Introduzca el id que quiere eliminar: ")
        mycursor = mydb.cursor()

        sql = f"DELETE FROM concesionario WHERE id = '{id}'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")
    elif(confirmacion == "4"):
        pregunta = input("Introduzca que quiere modificar: ")
        pregunta2 = input("Introduzca el valor a buscar: ")
        pregunta3 = input("Por qué valor")
        mycursor = mydb.cursor()

        sql = f"UPDATE concesionario SET {pregunta} = '{pregunta3}' WHERE {pregunta} = '{pregunta2}'"

        mycursor.execute(sql)

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")
    elif(confirmacion=="5"):
        pregunta = input("Introduzca un id para buscar: ")
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT * FROM concesionario WHERE id = '{pregunta}'")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
        confirmacion = 1