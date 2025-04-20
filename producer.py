from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = 'test-topic'
message = "tamizhanban Big Data Engineer"
producer.send(topic, message.encode('utf-8'))
print(f"Sent: {message}")
producer.flush() 
