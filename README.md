# zapi_elastic_search
python快速操作ElasticSearch的组件

## 快速入门案例
安装
```shell
pip install zapi_elastic_search
```

增删改查案例
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient

# 连接ES
es = EsClient()
print(es.conn)

# 查询
query = {
  "query": {
    "match_all": {}
  }
}
result = es.find(index="megacorp", body=query)
print(result)

# 新增
# 不指定id 自动生成
es.add(index="megacorp",body={"first_name":"xiao","last_name":"xiao", 'age': 25, 'about': 'I love to go rock climbing', 'interests': ['game', 'play']})
# 指定IDwu
es.add(index="megacorp",id=4,body={"first_name":"xiao","last_name":"wu", 'age': 66, 'about': 'I love to go rock climbing', 'interests': ['sleep', 'eat']})

# 根据ID删除
es.delete(index='megacorp', id=4)
```
