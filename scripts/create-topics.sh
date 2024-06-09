KAFKA_TOPICS="topic1 topic2 topic3 topic4 topic5"
for topic in $KAFKA_TOPICS; do
  kafka-topics --create --topic $topic --bootstrap-server kafka:29092 --partitions 1 --replication-factor 1
done
