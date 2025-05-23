from fastapi import FastAPI
import asyncio
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError

app = FastAPI()

KAFKA_TOPIC = "test-topic"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"


async def consume():
    print(f"Entering in consume")
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="my-fastapi-consumer-group",
        auto_offset_reset="earliest",
    )

    while True:
        try:
            await consumer.start()
            print("Kafka consumer connected and listening...")
            break
        except KafkaConnectionError:
            print("Kafka not available. Retrying in 5 seconds...")
            await asyncio.sleep(5)

    while True:
        try:
            print("Waiting for messages..")
            async for msg in consumer:
                print(f"Message received: {msg.value.decode('utf-8')}")
        except Exception as e:
            print(f"Error in consumer loop: {e}")
            await asyncio.sleep(5)



@app.on_event("startup")
async def startup_event():
    print("Startup event launched...")
    await asyncio.sleep(10)
    asyncio.create_task(consume())


@app.get("/")
async def root():
    return {"message": "Microservice B is running!"}
