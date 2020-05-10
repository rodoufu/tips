# docker

## Build a dockerfile

```sh
docker build -t me/wallet-backend-eth:v1 -f Dockerfile-base .
```

## Run bash inside the container

```sh
docker run -it me/wallet-backend-eth:v1 /bin/bash
```
