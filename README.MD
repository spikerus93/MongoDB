1. Start DB server (e.g. mysql)
2. Apply schema.sql
3. Generate data 
```
cd ./generator
# E.g. generate data for 5000 users
./generate.py 5000 > data.sql
# E.g. upload dump to mysql
mysql < data.sql
```