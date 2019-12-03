# from elasticsearch import Elasticsearch
# import com.zxc.get_H
# es = Elasticsearch('127.0.0.1:9200')
# mappings = {
#             "mappings": {
#                 "book": {
#                     "properties": {
#                         "id": {
#                             "type": "long",
#                             "index": "false"
#                         },
#                         "name": {
#                             "type": "text",
#                             "index": "true"
#                         },
#                         "Type": {
#                             "type": "text",
#                             "index": "true"
#                         },
#                         "msg": {
#                             "type": "object",
#                             "properties": {
#                                 "name": {"type": "text", "index": True},
#                                 "Torrent":{"type": "keyword", "index": False},
#                                 "doc": {"type": "keyword", "index": True},
#                                 "big":{"type":"integer","index": True},
#                                 "id":{"type":"keyword","index": True}
#                             }
#                         }
#                     }
#                 }
#             }
#         }
# res = es.indices.create(index = 'Film',body = mappings)