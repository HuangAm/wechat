import pika
import sys
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101')
connection = pika.BlockingConnection(parameters)
channel = connection.channel() #队列连接通道

channel.exchange_declare(exchange='direct_log',type='direct')
log_level = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(
    exchange='direct_log',
    routing_key=log_level,
    body=message
)
print("[x] Sent %r" %message)
connection.close()
