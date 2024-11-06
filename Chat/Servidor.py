import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('127.0.0.1', 8000))
        server.listen()
        print('Servidor iniciado e aguardando conexões na porta 7777...')
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept()
        print(f'Nova conexão de {addr}')
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            if msg:
                print(f'Mensagem recebida: {msg.decode("utf-8")}')
                broadcast(msg, client)
        except:
            print('Erro ao receber mensagem. Cliente será removido.')
            deleteClient(client)
            break

def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

def deleteClient(client):
    if client in clients:
        clients.remove(client)
        print(f'Cliente removido: {client}')

main()
