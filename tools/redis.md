# Redis

## Quick tips

### Starting a local node

```sh
docker run --name redis5 -p 6379:6379 -d redis:5.0-rc3
```

### Starting a redis client

```sh
docker run -it --link redis5:redis --rm redis redis-cli -h redis -p 6379
```

## redis-cli

### Adding elements to a stream

```sh
redis:6379> XADD mystream * sensor-id 1234 temperature 19.8
1531989605376-0
```

Added one element to the stream `mystream` with 2 key-value pairs `sensor-id 1234` and `temperature 19.8`.

## Nubmer of elements

```sh
redis:6379> XLEN mystream
(integer) 1
```

## Querying values

```sh
redis:6379> XRANGE mystream 1531989605376 1531989605377
1) 1) 1531989605376-0
  2) 1) "sensor-id"
     2) "1234"
     3) "temperature"
     4) "19.8"
```

You can use - for the smallest ID and + for the biggest ID:

```sh
redis:6379> XRANGE mystream - +
1) 1) 1531989605376-0
  2) 1) "sensor-id"
     2) "1234"
     3) "temperature"
     4) "19.8"
```

You can use count to limit the number of fetched messages:

```sh
redis:6379> XRANGE mystream - + COUNT 2
1) 1) 1531989605376-0
  2) 1) "sensor-id"
     2) "1234"
     3) "temperature"
     4) "19.8"
```

### Create a consumer group

```sh
redis:6379> XGROUP CREATE mystream mygroup01 $
OK
```

### Reading data with the consumer group

```sh
redis:6379> XREADGROUP GROUP mygroup01 Alice COUNT 1 STREAMS mystream >
1) 1) "mystream"
  2) 1) 1) 1531999977149-0
        2) 1) "message"
           2) "apple"
```
