# !/usr/bin/env python
import pika
import time
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='balance1')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
for i in range(100000000):
    channel.basic_publish(exchange='',
                          routing_key='balance1',
                          body=str(i))


connection.close()
