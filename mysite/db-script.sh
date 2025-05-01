# /bin/bash

sleep 10
# python3 /app/manage.py migrate

python3 manage.py makemigrations
python3 manage.py migrate
# python3 /app/manage.py collectstatic --noinput
# python3 /app/manage.py loaddata /app/fixtures/initial_data.json
# python3 /app/manage.py loaddata /app/fixtures/initial_data_2.json
# python3 /app/manage.py loaddata /app/fixtures/initial_data_3.json   
# python3 /app/manage.py loaddata /app/fixtures/initial_data_4.json
# python3 /app/manage.py loaddata /app/fixtures/initial_data_5.json
# python3 /app/manage.py loaddata /app/fixtures/initial_data_6.json   
# python3 /app/manage.py loaddata /app/fixtures/initial_data_7.json