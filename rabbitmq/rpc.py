import loggus

from pika import BasicProperties, PlainCredentials, ConnectionParameters, BlockingConnection


def test():
    log = loggus.withFields({"VirtualHost": "/rpc"})
    credentials = PlainCredentials("root", "root")
    parameters = ConnectionParameters(credentials=credentials, host="localhost", port=5672, virtual_host="/rpc")
    connection = BlockingConnection(parameters)
    channel = connection.channel()

    result = channel.queue_declare("", exclusive=True)
    queue_name = result.method.queue
    log = log.withFields({"QueueName": queue_name})
    with log.withCallback():
        channel.basic_publish(routing_key="test",
                              exchange="",
                              body="test",
                              properties=BasicProperties(
                                  delivery_mode=2,
                              ))
        log.info("publish ok!")


if __name__ == '__main__':
    test()
