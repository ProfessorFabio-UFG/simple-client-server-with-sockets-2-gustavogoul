import pickle
from socket import *
from constCS import *

def calculate(operation, num1, num2):
    operation = operation.strip().lower()
    try:
        if operation == 'add':
            print("Operation add.")
            return {"STATUS": "OK", "RES": num1 + num2}
        elif operation == 'subtract':
            return {"STATUS": "OK", "RES": num1 - num2}
        elif operation == 'multiply':
            return {"STATUS": "OK", "RES": num1 * num2}
        elif operation == 'divide':
            return {"STATUS": "OK", "RES": num1 / num2} if num2 != 0 else {"STATUS": "NOK", "RES": 2}
        else:
            return {"STATUS": "NOK", "RES": 1}
    except Exception as e:
        print("Erro no cálculo:", e)
        return {"STATUS": "NOK", "RES": 3}

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(f"Server escutando {HOST}:{PORT}")

(conn, addr) = s.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        print("Nenhum dado recebido, fechando conexão.")
        break

    request = pickle.loads(data)
    
    operation = request.get("OP")
    num1 = request.get("Num1")
    num2 = request.get("Num2")
    
    result = calculate(operation, num1, num2)
    conn.send(pickle.dumps(result))
    
conn.close()