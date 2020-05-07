# vault

## Start

```sh
docker run --cap-add=IPC_LOCK -e 'VAULT_DEV_ROOT_TOKEN_ID=myroot' -e 'VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200' -p 8200:8200 -p 8201:8201 --rm -d --name dev-vault vault
```

## Strop

```sh
docker stop dev-vault
```
