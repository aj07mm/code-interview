FROM mongo

COPY init.json /init.json
CMD mongoimport --host $MONGO_HOST --db hellofresh --collection user --type json --file /init.json --jsonArray --mode upsert
