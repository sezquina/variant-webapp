# variant-webapp
Testing a basic web application to display genetic variants from a VCF file.

```
# move pipeline vcf2 to clean db vcf2
cut -f 1-43 AbraOM-hg19-test.vcf2 > purged.csv # remove patients
#head -1 purged.csv | tr "\t" "\n" # get headers for database

# convert TSV to CSV
gsed -i 's/\t/","/g' purged.csv # switch tabs to commas
gsed -i 's/^/"/g' purged.csv # add a leading quote
gsed -i 's/$/"/g' purged.csv # add a trailing quote

# docker stuff
sudo docker kill $(sudo docker ps -q) # flush the system, kill all running containers
sudo docker-compose build && sudo docker-compose up -d # build the containers and run in daemon mode

# find the IP of the running postgres database
sudo docker network inspect bridge # usually 172.17.0.3

# postgres db creation and import scripts
psql -h 172.17.0.3 -p 5432 -U postgres postgres -f abraom-dbonly.sql # provisions the database, drops it and the table if existing previously (purge)
sudo docker-compose run wsgi /usr/local/bin/python create_db.py # creates the "variants" table within the "abraom" database

psql -h 172.17.0.3 -p 5432 -U postgres postgres -f abraom-import.sql # imports the data called purved.csv

# manually log in to postgres db and do a test query
psql -h 172.17.0.3 -p 5432 -U postgres postgres

# test query once you're logged into the database
\c abraom;
select * from variants where Chr='1' and "Start" > 17000 and "End" < 17300;
```