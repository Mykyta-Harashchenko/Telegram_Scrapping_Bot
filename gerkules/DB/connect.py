from mongoengine import connect
import certifi

from config.config import config
mongo_user = config.get('user')
mongodb_pass = config.get('pass')
db_name = config.get('db_name')
domain = config.get('domain')
port = config.get("port")
MONGO_URI = config.get("MONGO_URI")

# connect to cluster on AtlasDB with connection string
db_url = f"""mongodb://{mongo_user}:{mongodb_pass}@{domain}:{port}/{db_name}?retryWrites=true&w=majority"""
# print(db_url)
connect(host=MONGO_URI, ssl=True, db=db_name, tlsCAFile=certifi.where(), alias=db_name)

'''tlsCAFile=certifi.where()'''

