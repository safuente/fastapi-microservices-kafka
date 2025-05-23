import asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaConnectionError

app = FastAPI()

KAFKA_TOPIC = "test-topic"
KAFKA_BOOTSTRAP_SERVERS = "kafka:9092"

producer: AIOKafkaProducer | None = None

class Message(BaseModel):
    content: str


@app.on_event("startup")
async def startup_event():
    global producer
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

    while True:
        try:
            await producer.start()
            print("Kafka producer connected")
            break
        except KafkaConnectionError:
            print("Kafka producer not available. Retrying in 5 seconds...")
            await asyncio.sleep(5)


@app.on_event("shutdown")
async def shutdown_event():
    global producer
    if producer:
        await producer.stop()
        print("Kafka producer stopped")


@app.post("/produce")
async def produce_message(message: Message):
    if producer is None:
        return {"error": "Kafka producer is not started"}

    await producer.send_and_wait(KAFKA_TOPIC, message.content.encode("utf-8"))
    return {"status": "message sent", "content": message.content}
