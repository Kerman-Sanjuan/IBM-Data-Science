#How to open directories and print the content of a TXT
ejemplo = "D://Desktop/MachineLearning/IBM/prueba.txt"
with open(ejemplo,"r") as file1:
    print(file1.read(4))