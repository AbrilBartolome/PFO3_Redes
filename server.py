import socket
import threading
import pika

def handle_client(con, addr, channel):
    print(f"[Conectado correctamente] {addr}")
    while True:
        data = con.recv(1024)
        if not data:
            break
        task = data.decode()
        print(f"[Se ha recibido el mensaje] {task}")
        channel.basic_publish(exchange='', routing_key='task_queue', body=task)
        con.send(b"Tarea recibida")
    con.close()
    print(f"[Conexión cerrada] {addr}")

def start_server():
    con = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = con.channel()
    channel.queue_declare(queue='task_queue')

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999 ))
    server.listen()
    print("[Servidor inicializado] Se esperan conexiones")

    while True:
        con, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(con, addr, channel))
        thread.start()

if __name__ == "__task__":
    start_server()