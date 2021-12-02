# zapi_elastic_search
python快速操作ElasticSearch的组件

## 一、快速入门案例
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

## 二、常用功能

### 2.1 查看集群的健康状态
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient

# 连接ES
es = EsClient()

# 查看集群的健康状态
print(es.health())
```

### 2.2 查看集群的基本信息
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient

# 连接ES
es = EsClient()

# 查看集群的基本信息
print(es.info())
```

### 2.3 查看集群其他信息
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient

# 连接ES
es = EsClient()

# 查看集群的详细信息
print(es.detail())

# 查看当前客户端信息
print(es.client_info())

# 查看所有的索引
print(es.indexs())

# 查看集群的更多信息
print(es.stats())
```

### 2.4 查看集群的任务
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient

# 连接ES
es = EsClient()

# 查看集群的任务
print(es.tasks_get())

# 查看集群的列表
print(es.tasks_list())
```
