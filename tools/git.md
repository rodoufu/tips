# git

## Get all updates from mirror

```sh
git fetch --all
```

## Sub-module

### Adding

```sh
git submodule add https://github.com/google/googletest/
```
### Clone project and sub-modules

```sh
git clone --recurse-submodules https://github.com/grpc/grpc
```

### Clone sub-modules

```sh
git submodule update --init --recursive
```
