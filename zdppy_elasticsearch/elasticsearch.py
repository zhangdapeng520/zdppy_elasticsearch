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
    