# 0x0B. Redis basic

is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices. The project was developed and maintained by Salvatore Sanfilippo.


## Learning Objectives
* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Install Redis on Ubuntu
`$ sudo apt-get -y install redis-server`

`$ pip3 install redis`

`$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf`

## Tasks

0. Writing strings to Redis
1. Reading from Redis and recovering original type
2. Incrementing values
3. Storing lists
4. Retrieving lists
5. Implementing an expiring web cache and tracker
