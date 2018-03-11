from func.vk_group import *

#send(140420515, 'Прив')

while True:
	for i in group = vks.method('wall.get', {'owner_id': '-119926143'})['items']

for i, post in enumerate(group):
	group[i] = [post['likes']['count'] / post['views']['count'], post['id']]

print(*sorted(group)[::-1], sep='\n')