# git

## Get all updates from mirror

```sh
git fetch --all
```

## Sub-module

### Adding

```sh
git submodule add git@mygithost:billboard lib/billboard
```

## Remove

Remove the entry from `.gitmodules`, remove the entry from `.git/config`, remove the foder, and then:

```sh
git rm --cached lib/billboard
```

### Clone project and sub-modules

```sh
git clone --recurse-submodules https://github.com/grpc/grpc
```

### Clone sub-modules

```sh
git submodule update --init --recursive
```

### Initialize

```sh
git submodule init
```

### Update

```sh
git submodule update
```

## Using a specific SSH key

```sh
ssh-agent bash -c 'ssh-add ~/.ssh/<KeyName>; git push'
```
