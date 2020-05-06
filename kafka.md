# Kafka

## Size of topics

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

## Getting the lag for a consumer group

```sh
/kafka_2.12-2.3.0/bin/kafka-consumer-groups.sh --bootstrap-server kafka-operator-kafka-bootstrap.kafka:9092 --describe --group process_block_request_group
```

## Consuming all messages

```sh
/kafka_2.12-2.3.0/bin/kafka-console-consumer.sh --bootstrap-server kafka-operator-kafka-bootstrap.kafka:9092 --topic DepositNotification-FIXME --from-beginning
```

## Producing a message

```sh
echo '{"blockNumber":"0x8dde30","assetId":"ETH"}' | /kafka_2.12-2.3.0/bin/kafka-console-producer.sh --broker-list kafka-operator-kafka-bootstrap.kafka:9092 --topic ProcessBlockRequest > /dev/null
```

## Removing a topic

```sh
/home/kafka/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic WithdrawalRequest
```
