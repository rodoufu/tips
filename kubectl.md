# kubectl

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

kubectl get pod --all-namespaces

Trocar contexto
kubectl config use-context ireland.kubernetes.qume.io
kubectl config use-context gke.prod

kubectl config use-context staging.kubernetes.qume.io
kubectl config use-context gke.stag

kubectl config use-context kubernetes.coinecta.com

Getting container information
kubectl get statefulset parity-net -n parity-net -oyaml

dashboard.dev.kubernetes.qume.io
dashboard.staging.kubernetes.qume.io

## matar pod

kubectl -n staging delete pod wallet-eth-backend-7b8d44bb54-kzttg --force --grace-period=0

## Accessing graphQL

kubectl -n staging exec -it express-graphql-f9c4f89d-4wt59 bash

kubectl exec -it -n parity-net parity-net-0 -- /bin/bash

## Portas port forward

kubectl port-forward -n parity-net parity-net-0 8545 8546 30303

