# Parity

## In order to see all accounts, use:

```sh
curl --data '{"method":"eth_accounts","params":[],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -X POST localhost:8545
```

## Get balance of an specific address:

```sh
curl --data '{"method":"eth_getBalance","params":["0x00a329c0648769a73afac7f9381e08fb43dbea72"],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -X POST localhost:8545
```

## Making a transaction.

```sh
export transfer_from='0x00a329c0648769a73afac7f9381e08fb43dbea72'`
`export transfer_to='0x8f420832871d9b7205491cd59cdb30507a744500'`
```

Then create the transaction params:

```sh
export transfer_params='[{"from": "'$transfer_from'", "to": "'$transfer_to'", "gas": "0x76c0", "gasPrice": "0x9184e72a000", "value": "0x9184e72a", "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"}]'
export transfer_json='{"jsonrpc": "2.0", "method": "eth_sendTransaction", "params": '$transfer_params', "id": 1}'
```

Call the method to send the transaction:

```sh
curl --data '$transfer_json' -H "Content-Type: application/json" -X POST localhost:8545
```
