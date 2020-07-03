# k3d

## Instalation

```sh
wget -q -O - https://raw.githubusercontent.com/rancher/k3d/master/install.sh | bash
```

## Create a cluster

```sh
k3d create --name dev --api-port 6551 --publish 8081:80
```

## Listing clusters

```sh
k3d list
```

## Configuring

```sh
export KUBECONFIG="$(k3d get-kubeconfig --name='dev')"
kubectl cluster-info
kubectl get nodes
```

https://medium.com/@yannalbou/k3d-k3s-k8s-perfect-match-for-dev-and-testing-896c8953acc0
