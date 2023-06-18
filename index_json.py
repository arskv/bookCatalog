# import pandas as pd

import json
import uuid
from elasticsearch import Elasticsearch


es = Elasticsearch("http://localhost:9200",http_auth= ('elastic', 'password'))


with open('data.json', encoding="utf-8") as f:
  data = json.load(f)
  for item in data['dataset']:
    # print(item)
    item['contactName'] = item['contactPoint']['fn']
    # for v in item.values():
      # print(v)
    print(item['contactName'])
    print('______________________________________')
    es.index(index='catalog_index', id=uuid.uuid1(), body=item)
    # break    

 # es.search(index='catalog', body={'query': {'match': {'title': 'california'}}})

