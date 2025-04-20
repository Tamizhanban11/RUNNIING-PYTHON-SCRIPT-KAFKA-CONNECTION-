# Kafka Producer and Consumer Python Scripts

## Prerequisites

### 1. Kafka Setup
   - Ensure Kafka and Zookeeper are installed and running on your machine. If not, follow the Kafka setup guide provided in the [official documentation](https://kafka.apache.org/quickstart).
   
### 2. Python Environment
   - Make sure Python 3.x is installed on your system.
   - Install the required Kafka Python client using the following:
     ```bash
     pip install kafka-python
     ```

### 3. Kafka Topics
   - Before running the scripts, ensure the topic `test-topic` is created. If it doesn't exist, create it using this command:
     ```bash
     bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```

---

## Step-by-Step Execution

### Step 1: Start Kafka and Zookeeper
   1. **Start Zookeeper:**
      Open **Terminal 1** and run:
      ```bash
      bin/zookeeper-server-start.sh config/zookeeper.properties
      ```
      
   2. **Start Kafka Broker:**
      Open **Terminal 2** and run:
      ```bash
      bin/kafka-server-start.sh config/server.properties
      ```

### Step 2: Running the Producer Script
   1. Navigate to the directory where your `producer.py` script is located.
   
   2. Run the producer script to start sending messages to the Kafka topic `test-topic`:
      ```bash
      python producer.py
      ```
      The producer will begin sending messages to the Kafka topic, and you will see the output in your terminal.

   3. To stop the producer script, press **Ctrl + C** in the terminal.

---

### Step 3: Running the Consumer Script
   1. Open a new **Terminal** and navigate to the directory where your `consumer.py` script is located.

   2. Run the consumer script to listen for messages from the Kafka topic `test-topic`:
      ```bash
      python consumer.py
      ```
      The consumer will continuously print messages that are produced by the producer in real-time.

   3. To stop the consumer script, press **Ctrl + C** in the terminal.

---

## Troubleshooting

### Kafka Not Running:
   - Ensure that Kafka and Zookeeper are properly running. You can check by running:
     ```bash
     bin/kafka-topics.sh --list --bootstrap-server localhost:9092
     ```
   - If Kafka or Zookeeper isn't running, recheck their configuration and startup steps.

### Topic Creation Issues:
   - If the topic `test-topic` doesn't exist, you can create it using this command:
     ```bash
     bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
     ```

### Python Module Errors:
   - Ensure that the required Python module (`kafka-python`) is installed by running:
     ```bash
     pip install kafka-python
     ```

---

## Kafka Cleanup
   - If you want to delete the topic after testing, you can run:
     ```bash
     bin/kafka-topics.sh --delete --topic test-topic --bootstrap-server localhost:9092
     ```

---

This README provides all the steps to set up Kafka, run the producer and consumer scripts, and troubleshoot common issues. Follow these steps carefully for a smooth experience with Kafka using Python.
