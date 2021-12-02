from elasticsearch import Elasticsearch
from typing import Dict,Any

class EsClient:
    def __init__(self, ip:str = "127.0.0.1", port:int = 9200, hosts:Dict[str, Any] = None, timeout = 3600) -> None:
        """
        初始化数据
        """
        self.ip = ip
        self.port = port
        self.hosts = None
        if hosts is None:
            self.hosts = [{'host': ip, 'port': port}]
        self.conn = Elasticsearch(self.hosts, timeout = timeout)
    
    def find(self, index:str, body:Dict):
        """
        查询数据
        """
        result = self.conn.search(index = index, body = body)
        return result
    
    def add(self, index:str=None, id:int=None, body:Dict=None):
        """
        添加数据
        """
        if id is None:
            self.conn.index(index=index, body=body)
        else:
            self.conn.index(index=index, id=id,  body=body)
    
    def delete(self, index:str, id:int):
        """
        删除数据
        """
        self.conn.delete(index=index, id=id)

    def health(self) -> bool:
        """
        获取Elasticsearch集群的健康状态
        """
        return self.conn.ping()

    def info(self) -> Dict:
        """
        获取集群的基本信息
        """
        return self.conn.info()
