import json
from azure.cosmos import CosmosClient, PartitionKey
COSMOS_URI = "="
COSMOS_KEY = "="

client = CosmosClient(url=COSMOS_URI, credential=COSMOS_KEY)
database = client.create_database_if_not_exists(id="videos")
partitionKeyPath = PartitionKey(path="/id")
container = database.create_container_if_not_exists(
        id="video", partition_key=partitionKeyPath
)
QUERY = "SELECT * FROM video"
items = container.query_items(
        query=QUERY, enable_cross_partition_query=True
)
for item in items:
        print(json.dumps(item, indent=True))

with open('/var/www/uploads/emailurile_kober.txt', 'r') as suleyman:
        emailul_necesar = suleyman.read()



from uuid import uuid4
video_id = str(uuid4())
new_video = {
        "id": video_id,
        "email": emailul_necesar
                }
container.create_item(new_video)