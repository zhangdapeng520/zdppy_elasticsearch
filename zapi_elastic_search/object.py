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
    
    def find(self, index:str=None, body:Dict=None):
        """
        查询数据
        """
        result = self.conn.search(index=index, body=body)
        return result
    
    def find_all_index(self) -> Dict:
        """
        查询所有索引
        """
        return self.conn.indices.get_alias("*")
    
    def add(self, index: str = None, doc_type=None, id: int = None, body: Dict = None):
        """
        添加数据
        """
        if id is None:
            self.conn.index(index=index, doc_type=doc_type, body=body)
        else:
            self.conn.index(index=index, id=id, doc_type=doc_type,  body=body)
    
    def add_index(self, index:str) -> None:
        """
        新增索引
        """
        return self.conn.indices.create(index=index)
    
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

    def detail(self) -> Dict:
        """
        获取集群的详细信息
        """
        return self.conn.cluster.health()

    def client_info(self) -> Dict:
        """
        查看当前客户端信息
        """
        return self.conn.cluster.client.info()

    def indexs(self) -> str:
        """
        查看所有的索引
        """
        return self.conn.cat.indices()
    
    def stats(self) -> Dict:
        """
        查看集群的更多信息
        """
        return self.conn.cluster.stats()

    def tasks_get(self):
        return self.conn.tasks.get()
    
    def tasks_list(self):
        return self.conn.tasks.list()