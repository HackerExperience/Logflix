import pika
import cache
from logs.tracker import track_recv


def thread_consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='rabbitmq.service.consul',
            credentials=pika.PlainCredentials('he2', 'he2')))
    channel = connection.channel()

    channel.exchange_declare(exchange='exchange_log',
                             type='topic', durable=False)

    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    print(queue_name)

    channel.queue_bind(exchange='exchange_log',
                       queue=queue_name,
                       routing_key='log.DEBUG')

    print ' [*] Waiting for logs. To exit press CTRL+C'

    def callback(ch, method, properties, body):
        track_recv(body)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)
    cache.con = connection

    try:
        channel.start_consuming()
    except:
        pass


from threading import Thread
consumer = Thread(target=thread_consume)
consumer.start()


def stop_consumer():
    try:
        cache.con.close()
    except RuntimeError:
        pass
