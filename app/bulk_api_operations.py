'''
This program is to make a bulk operation action -> to elasticsearch 

Perform actions of bulks : 
create, update, delete actions
'''

from pprint import pprint
from elasticsearch import Elasticsearch

# Import configuration
from config.development import Config

# Performed connection to elasticsearch
es = Elasticsearch(
    Config.ES_HOST,
    verify_certs=True,
    basic_auth=(Config.ES_USERNAME, Config.ES_PASSWORD)
)
client = es.info()
pprint("1. Connected to the Elasticsearch connection ✔")
pprint(client.body)
pprint("-----------------------------------------------------------")

# Test connection
es.indices.delete(index="my_index", ignore_unavailable=True)
es.indices.create(index="my_index")

# Performing bulk API for elasticsearch action
response = es.bulk(
    operations=[
        # Operation Action 1
        {
            "index": {
                "_index": "my_index",
                "_id": 1
            }
        },
        # Source
        {
            "title": "This is content of 1",
            "author": "John Wick",
            "created_on": "2025-10-01"
        },

        # Operation Action 2
        {
            "index": {
                "_index": "my_index",
                "_id": 2
            }
        },
        # Source
        {
            "title": "This is content of 2",
            "author": "Dav's",
            "created_on": "2025-10-02"
        },

        # operation Action 3
        {
            "index": {
                "_index": "my_index",
                "_id": 3,
            }
        },
        # Source
        {
            "title": "This is content of 3",
            "author": "Martin",
            "created_on": "2025-10-03"
        },

        # operation Action 4 (update)
        {
            "update": {
                "_index": "my_index",
                "_id": 2
            }
        },
        {
            "doc": {
                "title": "New title update data in second index"
            }
        },

        # operation Action 5 (update)
        {
            "update": {
                "_index": "my_index",
                "_id": 1
            }
        },
        # source
        {
            "doc": {
                "new_fields": "Updated the document guidance"
            }
        },

        # operation Action 6 (delete)
        {
            "delete": {
                "_index": "my_index",
                "_id": 3
            }
        },
    ],
)


# Response from body testing
pprint("2. Response the bulks operations : ✔")
pprint(response.body)
pprint("---------------------------------------------------")
