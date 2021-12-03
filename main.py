# 使用python操作ElasticSearch
from zdpapi_elastic_search import EsClient

# 连接ES
es = EsClient()

# 查看集群的健康状态
print(es.health())