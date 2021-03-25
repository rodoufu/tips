# docker

## Build a dockerfile

```sh
docker build -t me/wallet-backend-eth:v1 -f Dockerfile-base .
```

## Run bash inside the container

```sh
docker run -it me/wallet-backend-eth:v1 /bin/bash
```

## Execution

```sh
docker exec -it $(docker container ls | grep $container_name | awk '{print $1}') /bin/bash
```

## Logs

```sh
docker logs $(docker container ls | grep $container_name | awk '{print $1}') --tail 10 -f 2>&1 | grep "looking for this"
```
