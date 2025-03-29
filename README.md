[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qjXMgXsV)
# Calculadora Remota

Este projeto implementa um sistema cliente-servidor simples para realizar operações matemáticas remotamente.

## Funcionalidades

* O cliente envia uma requisição contendo uma operação matemática (add, subtract, multiply, divide) e dois operandos.
* O servidor processa a requisição e retorna o resultado ao cliente.
* Caso a operação seja inválida, o servidor retorna um código de erro.

## Como executar
### 1. Iniciar o servidor
``` python server.py ```
O servidor irá aguardar a conexão.
### 2. Executar o cliente
Abra outro terminal e execute:
``` python client.py ```
O cliente solicitará a operação e os operandos:

### Exemplo:
```
Qual operação a ser realizada? (add, subtract, multiply, divide): add
Primeiro número: 5
Segundo número: 3
```
O servidor responderá com o resultado:
```
Resultado da operação: 8
```
### Em caso de erros:
* Operação inválida: Operação não existe.
* Divisão por zero: Resultado inesperado.
