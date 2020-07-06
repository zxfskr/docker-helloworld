# 1 启动srs

```
# echo "Run SRS 3.0 in docker"

docker run -d --rm --name serverA -p 1935:1935 -p 1985:1985 -p 8080:8080 fig/srs3:latest

docker run -d --rm --name serverA -p 1935:1935 -p 1985:1985 -p 8080:8080 -v /logrotate.d/logrotate-srs:/etc/logrotate.d/logrotate-srs -v /config/origin.cluster.serverA.conf:/usr/local/srs/conf/srs.conf fig/srs3:latest

```

# 2 推流命令

```
for((;;)); do ffmpeg -re -f v4l2 -i /dev/video0 -f alsa -i hw:0 -tune zerolatency -c:v libx264 -c:a libfdk_aac -r 30 -g 30 -preset ultrafast -f flv rtmp://127.0.0.1:1935/live/test; done;

ffplay rtmp://127.0.0.1:1935/live/test -fflags nobuffer
```