from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['PGSQL_USER']
password = os.environ['PGSQL_PASSWORD']
host = os.environ['PGSQL_HOST']
database = os.environ['PGSQL_DATABASE']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}/{database}'