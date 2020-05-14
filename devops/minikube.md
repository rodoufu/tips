# minikube

## Install

```sh
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
sudo install minikube /usr/local/bin/
```

## Start

```sh
minikube start --driver=docker
```

```sh
minikube start --driver=kvm2
```

## Deployments

## Apply

```sh
kubectl apply -f nginx-deployment.yaml
```

### List

```sh
kubectl get deployment
```

### Delete

```sh
kubectl delete deployment nginx-deployment
```

### Describe

```sh
kubectl describe deployments
```
