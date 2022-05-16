#!/usr/bin/env python
import pika
import os
from dotenv import load_dotenv
import json
from services import consumer_service

load_dotenv()

exchange_name = os.getenv("AMQP_EXCHANGE_NAME")
queue_name = os.getenv("AMQP_QUEUE_NAME")

credentials = pika.PlainCredentials(os.getenv('AMQP_USER'), os.getenv('AMQP_PASSWORD'))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=os.getenv('AMQP_HOST'), port=int(os.getenv('AMQP_PORT')), credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)

result = channel.queue_declare(queue=queue_name, durable=True)
queue_name = result.method.queue

channel.queue_bind(exchange=exchange_name, queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    consumer_service.consume(body)
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue=queue_name, on_message_callback=callback)

channel.start_consuming()
