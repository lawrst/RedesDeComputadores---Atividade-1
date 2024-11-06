import threading
import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('127.0.0.1', 8000))
        print('Conectado ao servidor na porta 7777')
    except Exception as e:
        print('\nErro ao conectar ao servidor:', e)
        return  # Pare o código caso a conexão falhe

    username = input('Usuário> ')
    print('\nConectado como', username)

    # Inicie as threads de envio e recebimento
    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            if msg:
                print(msg)
            else:
                print("Conexão fechada pelo servidor.")
                client.close()
                break
        except Exception as e:
            print('\nErro ao receber mensagens:', e)
            client.close()
            break

def sendMessages(client, username):
    while True:
        try:
            msg = input()
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except Exception as e:
            print('Erro ao enviar mensagem:', e)
            client.close()
            break

main()
