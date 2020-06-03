# unix

## Filter active services

```sh
systemctl list-units --type=service --state=active
```

## SSH using a specific key

```sh
ssh -i <Key location> <user>@<host name>
```

## Print ports in use

```sh
sudo lsof -i -P -n | grep LISTEN
```
