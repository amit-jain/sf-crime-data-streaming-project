import asyncio

from confluent_kafka import Consumer
from confluent_kafka.admin import AdminClient, NewTopic

BROKER_URL = "PLAINTEXT://localhost:9092"

async def consume(topic_name):
    """Consumes data from a Kafka Topic"""
    c = Consumer({"bootstrap.servers": BROKER_URL, "group.id": "org.sfpd"})
    c.subscribe([topic_name])

    while True:
        messages = c.consume(5, timeout=0.1)
        for message in messages:
            if message is None:
                print('No message')
            elif message.error() is not None:
                print(f'error: {message.error()}')
            else:
                print(f'{message.value()}')
                print('\n')

        await asyncio.sleep(0.01)


def main():
    try:
        asyncio.run(consume("org.sfpd.service.calls"))
    except KeyboardInterrupt as e:
        print("Shut down")


if __name__ == "__main__":
    main()
