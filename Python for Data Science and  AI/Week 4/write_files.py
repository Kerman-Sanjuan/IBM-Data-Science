texto = ["hola \n","que tal \n","estass!!!!!"]
ejemplo = "D://Desktop/MachineLearning/IBM/prueba_escritura.txt"
with open(ejemplo,"a") as file1:
    file1.write("Esto esta escrito con VSCode " )
    for palabras in texto: #En este modo escribe en el texto.
        file1.write(palabras)