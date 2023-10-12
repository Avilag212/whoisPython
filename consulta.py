import socket
import sys

def consulta(target):
    #Abre socket com o IANA
    try:
        soc = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        soc.connect(("whois.iana.org",43))
        try:
            message = target+"\r\n"
            soc.send(message.encode())
            response = soc.recv(1024)
            lista = response.decode('ISO-8859-1').split()
            soc.close() 
            #Indice 19 da lista contém o whois responsável pelo domínio pesquisado
            whoisResponsavel = lista[19]
            
        except TypeError as erro:
            print(f"Erro ao enviar consulta para o IANA:\n{erro}")

    except ConnectionRefusedError as erro:
        print(f"Erro de conexão com o IANA:\n{erro}")

    #Abre socket com o whois responsável pelo domínio pesquisado
    try:
        soc = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
        soc.connect((whoisResponsavel,43))
        try:
            message = target+"\r\n"
            soc.send(message.encode())
            response = soc.recv(1024)
            soc.close()
            return response.decode('ISO-8859-1') #Retona reposta do whois
            
            
        except TypeError as erro:
            print(f"Erro ao enviar consulta para o Whois responsável:\n{erro}")
            print(f'Whois responsavel:{whoisResponsavel}')

    except ConnectionRefusedError as erro:
        print(f"Erro de conexão com o whois responsável:\n{erro}")
        print(f'Whois responsavel:{whoisResponsavel}')



    

if(__name__ == '__main__'):
    if (len(sys.argv) < 2):
        print(f'Modo de uso: python3 consulta.py <target>')
    else:
        #O script utiliza o protocolo Whois que roda por default na porta 43
        #Função consulta() abre socket primeiro com o IANA para verificar quem é o NIR responsável pelo domíno pesquisado na porta 43 (Whois)
        #Então a função abre um socket com o NIR responsável e envia uma nova query para saber os dados de registro do domíno pesquisado.
        response = consulta(sys.argv[1])
        print(response)
        
