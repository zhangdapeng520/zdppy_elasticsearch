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

## 三、增删改查

### 3.1 增加数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 添加索引 已存在会报错
# print(es.add_index("persons"))

#index,doc_type,id都一致時會覆蓋
#插入資料
es.add(index="persons",doc_type="mytype",id=2,body={"name":"李四","age":20,"time":datetime.now()})
es.add(index="persons", doc_type="mytype", id=4, body={
       "name1": "李四", "name2": "張三", "age": 20, "time": datetime.now()})
es.add(index="persons", doc_type="mytype", id=5, body={
       "name1": "張三", "name2": "李四", "age": 20, "time": datetime.now()})
es.add(index="persons", doc_type="mytype", id=1, body={
       "name": "張三", "age": 18, "time": datetime.now()})

#沒有索引就建立
es.add(index="persons111", doc_type="mytype",id=3,body={"name":"王五","age":20,"time":datetime.now()})

# 查询所有索引
print(es.find_all_index())
print(es.indexs())

# 查询所有数据
res = es.find()
print(res)
```

### 3.2 根据ID查询数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 根据ID查询
res = es.find(index="persons", doc_type="mytype", id=1)
print(res)
```

### 3.3 查询所有数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询所有数据
res = es.find(index="persons")
print(res)
```

### 3.4 更新数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

#更新一條資料，需要指定index,doc_type,id
print(es.find(index="persons", id=1))
es.update(index="persons", doc_type="mytype", id=1, body={"doc": {"age": 10}})
print(es.find(index="persons", id=1))
print("==================")

# 条件更新
query = {"script": {
    "source": "ctx._source['age']=1"  # 改為字串時要加引號,"ctx._source['age']='張三'"
},
    'query': {
    'range': {
        'age': {
            'lt': 30
        }
    }
}
}
res = es.update(index="persons", doc_type="mytype", query=query)
print(res)
```

### 3.5 删除数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 根据ID删除
res = es.delete(index="persons", id='2')
print(res)

# 根据条件删除
res = es.delete(index="persons", query={'query': {'match': {'any': 'data'}}})
print(res)

# 删除索引
res = es.delete('persons')
print(res)
```

## 四、查询

### 4.1 查询年龄为20的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询所有数据
body = {
    "query": {
        "term": {
            "age": 20
        }
    }
}
res = es.find(index="persons", body=body)
print(res)
```

### 4.2 查询年龄为18或20的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询年龄为18或20的数据
body = {
    "query": {
        "terms": {
            "age": [
                18, 20
            ]
        }
    }
}
res = es.find(index="persons", body=body)
print(res)
```

### 4.3 查询名字包含“張”的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询名字包含“張”的数据
body = {
    "query": {
        "match": {
            "name1": "張"
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.4 查询name1和name2中都包含“四”的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询name1和name2中都包含"四"的数据
body = {
    "query": {
        "multi_match": {
            "query": "四",
            "fields": ["name1", "name2"]
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.5 查询ID为1或2的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询ID为1或2的数据
body = {
    "query": {
        "ids": {
            "values": [
                "1", "2"
            ]
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.6 查询name1=张三或者age=20的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# must(都滿足),should(其中一個滿足),must_not(都不滿足)
# 查询name1=张三或者age=20的数据
body = {
    "query": {
        "bool": {
            "should": [
                {
                    "term": {
                        "name": "張三"
                    }
                },
                {
                    "term": {
                        "age": 20
                    }
                }
            ]
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.7 查詢18<=age<=30的所有資料
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

'''
range不支援:
    eq 等於  
    neq 不等於
    
range支援:
    gt: greater than 大於
    gte: greater than or equal 大於等於
    lt: less than 小於
    lte: less than or equal 小於等於
'''
# 查詢18<=age<=30的所有資料
body = {
    "query": {
        "range": {
            "age": {
                "gte": 18,       # >=18
                "lte": 30        # <=30
            }
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.8查询年龄最小的4条数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 分页查询
body = {
    "query": {
        "match_all": {}
    },

    "sort": [{"age": {"order": "asc"}}],  # 排序,asc是指定列按升序排列，desc則是指定列按降序排列
    "from": 0,    # 开始索引
    "size": 4    # 获取4条数据
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.9 查询name1以"張"开头的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询name1以"張"开头的数据
body = {
    "query": {
        "prefix": {
            "name1": "張"
        }
    }
}
res = es.find(index="persons", body=body)
print(res)
```

### 4.10 查询name1以"三"结尾的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询name1以"三"结尾的数据
body = {
    "query": {
        "wildcard": {
            "name1": "*三"
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.11 查询所有数据并根据年龄升序
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询所有数据并根据年龄升序
body = {
    "query": {
        "match_all": {}
    },
    "sort": {
        "age": {                 # 根据年龄升序
            "order": "asc"       # asc升序，desc降序
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
```

### 4.12 查询所有数据并根据年龄升序且只获取ID
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询所有数据并根据年龄升序且只获取ID
body = {
    "query": {
        "match_all": {}
    },
    "sort": {
        "age": {                 # 根据年龄升序
            "order": "asc"       # asc升序，desc降序
        }
    }
}

res = es.find(index="persons", body=body, filter_path=["hits.hits._id"])
print(res)
```

### 4.13 查询数据总数
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

# 查询数据总数
res = es.find_count()
print(res)

res = es.find_count(index="persons")
print(res)
```

### 4.14 查询年龄最小的数据
```python
# 使用python操作ElasticSearch
from zapi_elastic_search import EsClient
from datetime import datetime

# 连接ES
es = EsClient()

'''
min:最小
max:最大
sum:求和
avg:平均值
'''
# 最小值
body = {
    "query": {
        "match_all": {}
    },
    "aggs": {                        # 聚合查詢
        "min_age": {                 # 最小值的key
            "min": {                 # 最小
                "field": "age"       # 查詢"age"的最小值
            }
        }
    }
}

res = es.find(index="persons", body=body)
print(res)
print(res['aggregations'])
```
