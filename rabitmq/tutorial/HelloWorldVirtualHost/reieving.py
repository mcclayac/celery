
import pika

credentials = pika.PlainCredentials('vh_user', '11javajava')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'vh_test',
                                       credentials)


connection = pika.BlockingConnection(parameters)

channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


