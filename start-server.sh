# /git/usr/bin/bash
C:/Users/NEKIWANUKA/Desktop/fgf_esystems/fgf/start-server.sh

# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd fgf; python manage.py createsuperuser --no-input)
fi
(cd fgf; gunicorn fgf.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"

# to run execute (icacls start-server.sh)
