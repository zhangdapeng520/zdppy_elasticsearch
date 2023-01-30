# zdppy_elasticsearch库使用
项目地址
GitHub开源地址：https://github.com/zhangdapeng520/zdppy_elasticsearch

主要看dev分支的代码。

# 版本历史
- 2023/01/30 v1.0.1 使用zdppy_requests完全重构项目

# 快速入门
## 安装
```bash
pip install zdppy_elasticsearch
```

## 创建Mapping
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
body = {
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "price": {
        "type": "double"
      },
      "author": {
        "type": "text"
      },
      "pub_date": {
        "type": "date"
      }
    }
  }
}
index = "books"
print(es.add_mapping(index, body))
```

## 查询Mapping
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
print(es.get_mapping(index))
```

## 删除Mapping
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
print(es.delete_index(index))
```

## 根据ID新增数据
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
did = 1
body = {
	"name": "《JavaScript全栈开发实战》",
	"author": "张大鹏",
	"price": 123,
	"pub_date": "2019-12-12"
}
print(es.add(index, did, body))
```

## 根据ID查询图书
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
did = 1
print(es.get(index, did))
print(es.get(index, did, is_source=True))
```

## 根据ID删除图书
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
did = 1
print(es.delete(index, did))
print(es.get(index, did, is_source=True))
```

## 批量插入数据
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
data = [
	{"index": {"_index": "books", "_type" : "_doc", "_id" : "1"}},
	{"name": "《JavaScript全栈开发实战》", "author": "张大鹏", "price": 123, "pub_date": "2019-12-12" },
	{"index": {"_index": "books", "_type" : "_doc", "_id" : "2"}},
	{"name": "《React学习手册》", "author": "张大鹏", "price": 122, "pub_date": "2019-12-12" },
	{"index": {"_index": "books", "_type" : "_doc", "_id" : "3",}},
	{"name": "《精通Go语言》", "price": 128, "pub_date": "2019-12-12" }
]

data1 = [
	{"name": "《JavaScript全栈开发实战》", "author": "张大鹏", "price": 123, "pub_date": "2019-12-12" },
	{"name": "《React学习手册》", "author": "张大鹏", "price": 122, "pub_date": "2019-12-12" },
	{"name": "《精通Go语言》", "price": 128, "pub_date": "2019-12-12" }
]


# 自定义索引和和ID
print(es.add_many(data))

# 自动生成ID
print(es.add_many(data1, index=index))
```

## 搜索所有图书
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"

# 搜索所有图书
print(es.search(index))
```

## 搜索特定价格范围的图书
```python
import zdppy_elasticsearch as ze

es = ze.ElasticSearch(password="zhangdapeng520")
index = "books"
query = {
  "query": {
    "range": {
      "price": {
        "gt": 123,
        "lte": 130
      }
    }
  }
}

# 搜索所有图书
print(es.search(index, query))
```