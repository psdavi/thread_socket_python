# socket: link de comunicação bidirecional entre dois programas em execução na rede (Cliente/Servidor).
import socket
# sys: fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
import sys
# math: um módulo interno que estende a lista de funções matemáticas.
import math
# threading: é usado para executar vários threads (tarefas, chamadas de função) ao mesmo tempo.
import threading

# Endereco IP do Servidor
SERVER = '10.0.0.205'

# PORT: o cliente deve informar a porta que o servidor está disponibilizando
PORT = int(float(sys.argv[1]))

# IMPLEMENTANDO O SOCKET (CLIENTE)
# Recebe 2 parâmetros: AF_INET e SOCK_STREAM
conexao_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DESTINO = (SERVER, PORT)
# Que faz a conexão no nosso servidor.
conexao_tcp.connect(DESTINO)

lista = []
lista2 = []

funcao = conexao_tcp.recv(2048)
funcao = funcao.decode('utf-8')


def main(funcao):
    # base
    def calculo1(R):
        try:
            area_base = math.pi * (R * R)
            lista.append(area_base)
            # 12,56
        except Exception:
            raise Exception

    # area lateral
    def calculo2(R, H):
        try:
            area_lateral = (2 * (math.pi)) * (R * H)
            lista2.append(area_lateral)
            # 37,68
        except Exception:
            raise Exception

    if (funcao == '1'):
        # Criando a thread
        thread1 = threading.Thread(target=calculo1, args=[2])
        # Iniciando a thread
        thread1.start()
        # Encadear a thread
        thread1.join()
        res_parcial1 = lista[0]

        conexao_tcp.send(str(res_parcial1).encode())
        print("Resultado parcial 01: ", res_parcial1)

    elif (funcao == '2'):
        thread2 = threading.Thread(target=calculo2, args=[2, 3])
        thread2.start()
        thread2.join()

        res_parcial2 = lista2[0]
        conexao_tcp.send(str(res_parcial2).encode())
        print("Resultado parcial 02: ", res_parcial2)


if __name__ == "__main__":
    main(funcao)
