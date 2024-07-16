# chain-with-history-by-using-redis

# redis 설치

```
$ docker pull redis

$ docker run \
-d \
--name=redis \
-p 6379:6379 \
-e TZ=Asia/Seoul \
-v /redis.conf:/etc/redis/redis.conf \
-v /redis_data:/data \
redis:latest redis-server /etc/redis/redis.conf
```
