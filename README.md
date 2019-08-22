# docker-helloworld

```
docker build --tag=friendlyhello .
docker image ls

docker run --rm -name friendlyhello -p 4000:80 friendlyhello
```

new load-balanced app
```
docker swarm init --advertise-addr 172.16.81.1
docker node ls
docker stack deploy -c docker-compose.yml swarm_test
```

安装nfs

```
sudo apt install nfs-kernel-server
sudo cat "/ext/test/       *(rw,sync,no_subtree_check,all_squash,anonuid=1000,anongid=1000)" >> /etc/exports
sudo exportfs -r
showmount -e 172.16.81.1
```