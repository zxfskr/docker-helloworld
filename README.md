# docker-helloworld
安装docker
```
bash install.sh --mirror Aliyun
```

将当前用户添加到docker用户组,可以不用sudo运行docker
```
sudo usermod -aG docker $USER
```

安装docker-mechine
```
 base=https://github.com/docker/machine/releases/download/v0.16.0 &&
   sudo wget $base/docker-machine-$(uname -s)-$(uname -m) -O /usr/local/bin/docker-machine &&
  sudo chmod +x /usr/local/bin/docker-machine
```

安装docker-compose
```
sudo wget https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -O /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

使用 docker swarm
```
docker build --tag=swarm_test .
docker image ls

docker run --rm -name swarm_test -p 4000:80 swarm_test
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