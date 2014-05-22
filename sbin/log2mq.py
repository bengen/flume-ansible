#!/usr/bin/env python
import pika
import sys
import tailer

for message in tailer.follow(open('/data1/logs/flume/1399625340262-1'), 0.1):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.10.3.208', port=5672, credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()

    channel.exchange_declare(exchange='kfs.userlog',
                         type='topic')

    routing_key = 'userlog'

    channel.basic_publish(exchange='kfs.userlog',routing_key=routing_key,body=message)
    print " [x] Sent %r:%r" % (routing_key, message)
    connection.close()
