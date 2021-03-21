# Kafka

## Quick tips

### Size of topics

In case disks are being crazily filled up by Kafka and you need to find out who's the bad guy:

```sh
./kafka-topics.sh --bootstrap-server bootstrap.development:9092 --list | while read topic; do echo $(./kafka-log-dirs.sh --bootstrap-server bootstrap.development:9092 --topic-list "${topic}" --describe | grep '^{'   | jq '[ ..|.size? | numbers ] | add') ${topic}; done | sort -n | tac
```

You can also investigate which topics are consuming the most with this one-liner:

```sh
for p in $(kubectl -n development get pod -l app=kafka -o jsonpath='{.items[*].metadata.name}'); do
echo ${p}; kubectl -n development exec -it ${p} -- sh -c 'cd /var/lib/kafka/data/topics; ls -1 -d */ | while read t; do du -csh ${t}/*.log | tail -1 | sed "s@total@${t}@"; done | sort -h';
done
```

### Getting the lag for a consumer group

```sh
/kafka_2.12-2.3.0/bin/kafka-consumer-groups.sh --bootstrap-server kafka-operator-kafka-bootstrap.kafka:9092 --describe --group process_block_request_group
```

### Consuming all messages

```sh
/kafka_2.12-2.3.0/bin/kafka-console-consumer.sh --bootstrap-server kafka-operator-kafka-bootstrap.kafka:9092 --topic DepositNotification-FIXME --from-beginning
```

### Producing a message

```sh
echo '{"blockNumber":"0x8dde30","assetId":"ETH"}' | /kafka_2.12-2.3.0/bin/kafka-console-producer.sh --broker-list kafka-operator-kafka-bootstrap.kafka:9092 --topic ProcessBlockRequest > /dev/null
```

### Removing a topic

```sh
/home/kafka/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic WithdrawalRequest
```

### Setting the offset of a consumer group for a topic

```sh
bash /kafka_2.12-2.3.0/bin/kafka-consumer-groups.sh --bootstrap-server $KAFKA --group ob_persistence_beta --topic orderbook_update --reset-offsets --to-offset 52178 --execute
```

Aditional help:
https://gist.github.com/marwei/cd40657c481f94ebe273ecc16601674b

## Kafdrop

https://github.com/HomeAdvisor/Kafdrop

https://github.com/obsidiandynamics/kafdrop

```
kafdrop_docker:
	docker run --name kafdrop -it --rm --net="host" -v $(kafdrop_path):/Kafdrop 99taxis/mini-java8 /bin/bash
kafdrop_start:
	nohup docker run --name kafdrop --rm --net="host" -v $(kafdrop_path):/Kafdrop 99taxis/mini-java8 java -jar /Kafdrop/target/kafdrop-2.0.6.jar --zookeeper.connect=$(zookeeper) > kafdrop.out 2>&1 &
kafdrop_stop:
	docker stop kafdrop
```

## kafkacat

### List topics

```sh
kafkacat -b kafka:9092 -L
```

### Consume all messages from a topic

```sh
kafkacat -b kafka:9092 -C -t mytopic
```

### Producing messages from stdin

```sh
kafkacat -b kafka:9092 -P -t mytopic
```
