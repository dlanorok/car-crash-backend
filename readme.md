Install python with pip (v3)

Install requirements
>> pip3 install -r .\requirements\base.txt
>> pip3 install -r .\requirements\dev.txt

Run command... 

>> python manage.py migrate

...and start backend with...

>> python manage.py runserver

Run redis
>> docker run -d --name redis -p 6379:6379 redis/redis-stack-server:latest


Run celery 

>> celery -A config worker -l INFO -P solo

