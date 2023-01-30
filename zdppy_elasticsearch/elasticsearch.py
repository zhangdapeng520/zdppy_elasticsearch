import uuid
import json
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth
from typing import Union

class ElasticSearch:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 9200,
        username: str = "elastic",
        password: str = "elastic",
    ):

        self.host = host
        self.port = port
        self.url = f"http://{host}:{port}"
        self.username = username
        self.password = password
        self.auth = HTTPBasicAuth(username, password)
    
    def add_mapping(self, index:str, mapping:dict) -> bool:
        """添加索引映射"""
        try:
            response = zr.put(f"{self.url}/{index}", json=mapping, auth=self.auth)
            if response.status_code != 200:
                print(response.text)
                return False
        except Exception as e:
            print(e)
            return False
        return True
    
    def get_mapping(self, index:str) -> dict:
        """查询索引映射"""
        try:
            response = zr.get(f"{self.url}/{index}/_mapping?pretty", auth=self.auth)
            return response.json()
        except Exception as e:
            print(e)
            return {"msg":"连接ElasticSearch服务失败"}
    
    def delete_index(self, index:str) -> bool:
        """删除索引"""
        try:
            response = zr.delete(f"{self.url}/{index}", auth=self.auth)
            return True
        except Exception as e:
            print(e)
            return False
    
    def add(self, index:str, did:Union[str, int], document:dict) -> bool:
        """新增数据"""
        target = f"{self.url}/{index}/_doc/{did}"
        try:
            response = zr.put(target, json=document, auth=self.auth)
            if response.status_code not in (200, 201):
                print(response.text)
                return False
        except Exception as e:
            print(e)
            return False
        return True
    
    def get(self, index:str, did:Union[str, int], is_source:bool = False) -> dict:
        """根据ID获取数据"""
        target = f"{self.url}/{index}/_doc/{did}"
        try:
            response = zr.get(target, auth=self.auth)
            data = response.json()
            if data["found"]:
                if is_source:
                    return data["_source"]
                else:
                    return data
        except Exception as e:
            print(e)
        return {}
    
    def delete(self, index:str, did:Union[str, int]) -> bool:
        """根据ID删除数据"""
        target = f"{self.url}/{index}/_doc/{did}"
        try:
            response = zr.delete(target, auth=self.auth)
            return response.status_code == 200
        except Exception as e:
            print(e)
        return False
    
    def add_many(self, data:list, index:str=None) -> bool:
        """批量添加数据"""
        # 校验数据
        if not data or len(data) == 0:
            return False
        
        # 添加索引和ID
        if index is not None:
            if not index:
                return False

            new_data = []
            for doc in data:
                _id = str(uuid.uuid4())
                index_doc = {"index": {"_index": index, "_type" : "_doc", "_id" : _id}}
                new_data.append(index_doc)
                new_data.append(doc)
            data = new_data

        # 准备参数
        target = f"{self.url}/_bulk"
        payload = '\n'.join([json.dumps(line) for line in data]) + '\n'
        headers = {           
            'Content-Type': 'application/x-ndjson'
        }

        # 添加数据
        try:
            response = zr.post(target, data=payload, auth=self.auth, headers=headers)
            if response.status_code != 200:
                print(response.text)
                return False
        except Exception as e:
            print(e)
            return False
        
        return True
    
    def search(self, index:str, query:dict=None, is_source=True) -> dict:
        """批量添加数据"""
        # 校验数据
        if query is None:
            query = {
                "query": {
                    "match_all": { }
                }
            }
        
        # 搜索
        target = f"{self.url}/{index}/_search"
        try:
            response = zr.get(f"{self.url}/{index}/_search", json=query, auth=self.auth)
            data = response.json()
            if is_source:
                return [v["_source"] for v in data["hits"]["hits"]]
            else:
                return data
        except Exception as e:
            print(e)
        
        return {}
    