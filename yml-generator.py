import datetime
import sys
import django
import os
from faker import Faker
from yaml import dump
from django.contrib.auth.hashers import make_password

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

def main(n):
    with open('apps/fixtures/users.yaml', 'w') as file:
        fake = Faker()
        data = [
            {
                'model': 'users.user',
                'pk': i + 4,
                'fields': {
                    'first_name': fake.name(),
                    'email': fake.email(),
                    'password': make_password(fake.password()),
                    'date_joined': datetime.datetime.utcnow()
                }
            } for i in range(int(n))
        ]
        dump(data, file, sort_keys=False)


if __name__ == '__main__':
    main(*sys.argv[1:])
