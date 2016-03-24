sudo apt-get update && apt-get install git-core curl build-essential openssl libssl-dev python-pip sqlite3
curl -sL https://deb.nodesource.com/setup_5.x | bash -
apt-get install --yes nodejs
npm install http-server -g

pip install -r api/requirements.txt

python api/manage.py syncdb

#python api/manage.py migrate
#python api/manage.py createsuperuser