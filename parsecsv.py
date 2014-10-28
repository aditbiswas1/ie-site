import csv
from django.contrib.auth.models import User

def run():
	with open('ie.csv', 'rb') as csvfile:
		contactreader = csv.reader(csvfile, delimiter = ' ')
		for row in contactreader:
			if len(row) == 1:
				username = row[0]
			else:
				username = ''.join(row)
			User.objects.create_superuser(username, None, 'rainbows')
	