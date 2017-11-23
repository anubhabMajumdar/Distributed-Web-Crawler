import urllib, json

url = 'http://127.0.0.1:5000/'
response = urllib.urlopen(url)
data = json.loads(response.read())

# KAFKA
BOOTSTRAP_SERVERS = data['BOOTSTRAP_SERVERS']
GROUP_CONTENT_CONSUMER = data['GROUP_CONTENT_CONSUMER']
GROUP_URL_CONSUMER = data['GROUP_URL_CONSUMER']
CONTENT_TOPIC = data['CONTENT_TOPIC']
URL_TOPIC = data['URL_TOPIC']

# MONGODB
DATABASE_NAME = data['DATABASE_NAME']
DATABASE_IP = data['DATABASE_IP']
DATABASE_PORT = data['DATABASE_PORT']
COLLECTION_GRAPH = data['COLLECTION_GRAPH']
COLLECTION_VISITED = data['COLLECTION_VISITED']

# THREADS
THREAD = data['THREAD']