import socket

def servidor():
    #portas disponíveis para clientes
    ports = [7777, 7778]
    host = ['', '']
    con_tcp_socket = []
    clientes = []
    conexoes = []


    #IMPLEMENTANDO O SOCKET (SERVIDOR)
    #AF_INET: é uma família de endereços usada para designar o tipo de endereços com os quais seu soquete pode se comunicar (neste caso, endereços de Protocolo de Internet v4)
    #SOCK_STREAM: Fornece fluxos de bytes bidirecionais sequenciados com um mecanismo de transmissão para dados de fluxo (TCP).
    try:
        for idx in range(2):
            conexao_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conexao_tcp.bind((host[idx], ports[idx]))
            conexao_tcp.listen(1)
            con_tcp_socket.append(conexao_tcp)
        print("Servidor Online! Aguardando Conexões...")
    except Exception:
        raise Exception

    try:
        for conexao_tcp in con_tcp_socket:
            index = con_tcp_socket.index(conexao_tcp)
            con, client = conexao_tcp.accept()
            conexoes.append(con)
            conexoes[index].send(str(index + 1).encode())
            clientes.append(client)
            print('Conexão estabelecida por: ', clientes[index])
    except Exception:
        raise Exception

    resul_parcial1 = float(conexoes[0].recv(4096))
    resul_parcial2 = float(conexoes[1].recv(4096))

    print("\nValor parcial da equação recebido do client 01: ", resul_parcial1)
    print("\nValor parcial da equação recebido do client 02: ", resul_parcial2)

    #Area(tot) = A(lat) + 2*A(base)

    areaTotal = resul_parcial2 + (2 * resul_parcial1)

    print("\nResultado final (Area Total): ", areaTotal)

if __name__ == "__main__":
    servidor()
