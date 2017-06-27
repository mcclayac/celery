


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()



# channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello', durable=True)

for i in range(5):
    channel.basic_publish(exchange="",
                      routing_key='hello',
                      body='Hello World')
    print(" [x] Sent 'HelloWorld")


connection.close()