import redis
import uuid

def create_uuid(num,length = 16):
	result = []
	i = 0
	while i < num:
		new_uuid = uuid.uuid1()
		temp = str(new_uuid).replace('-','')[:length]
		if temp not in result:
			result.append(temp)
		i += 1
	return result

def save_to_redis(uuid_list):
	r = redis.Redis(host = 'localhost',port = 6379,db = 0)
	for uuid in uuid_list:
		r.lpush('uuid',uuid)
	print('save Success...')

def main():
	result = create_uuid(200)
	save_to_redis(result)

if __name__ == '__main__':
	main()