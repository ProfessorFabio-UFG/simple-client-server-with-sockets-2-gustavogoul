import pickle
from socket  import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)
print("Tentando conectar ao servidor...")
s.connect((HOST, PORT))
print("Conectado com sucesso!")
op = input("Qual operação a ser realizada? (add, subtract, multiply, divide)\n")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

data = {"OP": op, "Num1": num1, "Num2": num2}
msg = pickle.dumps(data)
s.send(msg)
print("Mensagem enviada, aguardando resposta...")

msg = s.recv(1024)
data = pickle.loads(msg)

if data["STATUS"] == "OK":
  print ("Resultado da operação: ", data["RES"])
elif data["STATUS"] == "NOK" and data["RES"] == 1:
  print ("Operação não existe.")
else:
  print ("Resultado inesperado.")

s.close()
print("Conexão encerrada.")
input("Pressione Enter para sair...")