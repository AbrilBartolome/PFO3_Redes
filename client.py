import socket

def send_task(task):
    try: 
        client = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
        client.connect(('localhost', 9999))
        
        client.send(task.encode())
        
        response = client.recv(1024)
        
        print(f"[Respuesta del servidor] {response.decode()}")
    except ConnectionRefusedError:
        print("Error de conexión")
    
    finally:
        client.close()

if __name__ == "__task__":
    while True:
        task = input("Ingresar tarea o finalizar")
        if task.lower() == 'salir':
            break
        send_task(task)