



import redisio


r = redis.StrictRedis(host="localhost", port=6379, db=0)



# r = redis.Redis(
#     host='hostname',
#     port=port,
#     password='password')

#r = redis.StrictRedis(host='localhost', port=6379, db=0)

result = r.set('foo', 'bar')
print(result)

result = r.get('foo')
print(result)



