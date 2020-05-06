# kubectl

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

```sh
kubectl get pod --all-namespaces
```

## Switch context

```sh
kubectl config use-context ireland.kubernetes.qume.io
kubectl config use-context gke.prod
```

```sh
kubectl config use-context staging.kubernetes.qume.io
kubectl config use-context gke.stag
```

```sh
kubectl config use-context kubernetes.coinecta.com
```

## Getting container information

```sh
kubectl get statefulset parity-net -n parity-net -oyaml
```

## matar pod

```sh
kubectl -n staging delete pod wallet-eth-backend-7b8d44bb54-kzttg --force --grace-period=0
```

## Accessing graphQL

```sh
kubectl -n staging exec -it express-graphql-f9c4f89d-4wt59 bash
```

```sh
kubectl exec -it -n parity-net parity-net-0 -- /bin/bash
```

## Portas port forward

```sh
kubectl port-forward -n parity-net parity-net-0 8545 8546 30303
```

```sh
kubectl port-forward -n parity-net $(kubectl get pod -l app=eth-node -n parity-net -ojsonpath='{.items[0].metadata.name}')  8545 8546 30303
```

## Scale pod

```sh
kubectl -n ${NS} scale sts wallet-crypto --replicas=0
```

## List running pods

```sh
kubectl -n ${NS} get pods
```

## Get logs

```sh
kubectl logs -n <namespace> <pod> <container>
```

If you want to keep listening to it, add the `-f` parameter.
```sh
kubectl logs -f -n <namespace> <pod> <container>
```
