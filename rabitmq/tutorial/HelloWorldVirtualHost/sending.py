


import pika


import pika


credentials = pika.PlainCredentials('vh_user', '11javajava')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'vh_test',
                                       credentials)


connection = pika.BlockingConnection(parameters)
channel = connection.channel()



# channel.queue_declare(queue='hello')
channel.queue_declare(queue='hello', durable=True)

for i in range(5):
    channel.basic_publish(exchange="",
                      routing_key='hello',
                      body='Hello World')
    print(" [x] Sent 'HelloWorld")


connection.close()