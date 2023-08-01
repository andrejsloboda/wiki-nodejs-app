import os
import logging
from zipfile import ZipFile
from argparse import ArgumentParser

parser = ArgumentParser(usage='python db_dump.py user_name database destination')
parser.add_argument("container", default=None, help="Destination folder")
parser.add_argument("user_name", default=None, type=str, help="user_name")
parser.add_argument("database", default=None, help="Name of the database")
parser.add_argument("destination", default=None, help="Destination folder")

args = parser.parse_args()

def run(container, user_name, database, destination):
    os.system(f"docker exec {container} pg_dump -U {user_name} {database} > {destination}/wiki_dump.sql")

    with ZipFile(f'{destination}/wiki_dump.zip', 'w') as zip_file:
        zip_file.write(f'{destination}/wiki_dump.sql')

    os.system(f"rm -f {destination}/wiki_dump.sql")

run(args.container, args.user_name, args.database, args.destination)
