### Redis

Redis (Remote dictionary server), is an in memory data structure
store that can be utilized as a database, cache, or a message broker.


Data stored in Redis in the form of key-values where the keys are used to locate and extract the data
on the Redis Instance

Normal databases store data to disk, which brings in the extra cost, in terms of time and hardware resources.
Redis avoids this by storing all the data in memory, which makes 
the data readily available and increases the speed of data access and manipulation, as compared to normal
databases.


### Application of Redis

1. Caching: Redis has become an ideal solution for temporarily storing data in a cache to accelerate data access in the future.
2. Messaging Queuing: With the capability of implementing the Publish/Subscribe messaging paradigm, Redis has become a message broker for message queueing systems.
3. Data storage: Redis can be used to store key-value data as a NoSQL database.

###### Install Redis

```
sudo apt-get install redis
```

###### Redis cli

```
redis-cli -v
```

### Redis command

1. SET: This command is used to set a key and its value, with additional
optional parameters to specify the expiration of the key-value entry.

```
SET hello "world" Ex 10
```

EX is expiry time

2. GET: This command is used to get the value
associated with a key. After expiration time the value is nil

```
GET hello
```

3. DELETE: This command deletes a key and the associated value
```
DEL hello
```

4. TTL: When a key is set with an expiry, this command can be used to view how much time is left
```
TTL hello
```

5. PERSIST: f we change our mind about a key's expiry, we can use this command to remove the expiry period
```
PERSIST hello
```

6. RENAME: This command is used to rename the keys in our redis server
```
RENAME hello hello2
```

7. FLUSHALL: Purge all the key-value entries we have set in out current session

###### Install redis

```
pip install redis
```