uwsgi --protocol=https --socket=0.0.0.0:54321 --master --enable-threads -w wsgi:app