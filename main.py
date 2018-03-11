from func.vk_group import *
import json, time, random

GROUP_ID = -163409528

''''''

def max_size(lis):
	q = set(lis.keys())
	ma = 0
	for t in q:
		if 'photo_' in t and int(t[6:]) > ma:
			ma = int(t[6:])
	return lis['photo_' + str(ma)]

def process(mes):
	attachments = []

	if 'attachments' in mes:
		for u in mes['attachments']:

#Картинки
			if u['type'] == 'photo':
				attachments.append({'type': 'image', 'url': max_size(u['photo']), 'from': u['photo']['owner_id'], 'id': u['photo']['id'], 'album': u['photo']['album_id']})

	return attachments

''''''

with open('set.json', 'r') as file:
	groups = json.loads(file.read())['groups']

while True:
	try:
		for group in groups:
			posts = vks.method('wall.get', {'owner_id': group, 'count': 10})['items'] #, 'offset': groups[group]

			for post in posts[::-1]:
				if post['id'] > groups[group] and time.time() - post['date'] > 600:
					groups[group] = post['id']

					if post['likes']['count'] / post['views']['count'] > 0.05:
						a = ','.join(['photo%s_%d' % (i['from'], i['id']) for i in process(post)])

						if post['text'] or a:
							print(post['id'], a)
							vks.method('wall.post', {'owner_id': GROUP_ID, 'message': post['text'], 'attachments': a})
							time.sleep(random.randint(60, 600))

			time.sleep(1)
		time.sleep(60)

	except:
		with open('set.json', 'w') as file:
			print(json.dumps({'groups': groups}, indent=4), file=file)

		break