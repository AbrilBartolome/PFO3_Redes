import pika
import time

def callback(ch, method, properties, body):
    task = body.decode('utf-8')
    print(f"[Worker] Tarea recibida: {task}")
    
    time.sleep(2)
    
    print(f"[Worker] Tarea completada: {task}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_worker():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print("[Worker] Esperando tareas. Presione CTRL+C para salir.")
    channel.start_consuming()

if __name__ == "__task__":
    start_worker()