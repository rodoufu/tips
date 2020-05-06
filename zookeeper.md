# zookeeper

## Creating a node

```sh
${kafka_pah}/bin/zookeeper-shell.sh ${zookeeper_address} create /nodePath "<node value>"
```

## Changing a node value

The node needs to already exists.

```sh
${kafka_pah}/bin/zookeeper-shell.sh ${zookeeper_address} set /nodePath "<node value>"
```

## Listing nodes node

```sh
${kafka_pah}/bin/zookeeper-shell.sh ${zookeeper_address} ls /nodePath
```

## zk-shell

https://pypi.org/project/zk-shell/

### Installing

```sh
pip install zk-shell
```

### Usage

```sh
zk-shell localhost:2181
(CONNECTED) /> ls
zookeeper
(CONNECTED) /> create foo 'bar'
```
