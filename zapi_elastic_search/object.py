from elasticsearch import Elasticsearch
from typing import Dict,Any,List

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
    
    def find(self, index: str = None, body: Dict = None, doc_type: str = None, id: int = None, filter_path:List=None):
        """
        查询数据
        """
        # ID不为空，调用的是get方法
        if id is not None: 
            return self.conn.get(index=index, filter_path=filter_path, doc_type=doc_type, id=id)
        
        # 查询所有数据：index不为None，body和ID为None
        if index is not None and body is None and id is None:
            return self.conn.search(index=index, filter_path=filter_path, body={"query": {"match_all": {}}})
        
        # ID为空，调用的是search方法
        result = self.conn.search(
            index=index, body=body, filter_path=filter_path, doc_type=doc_type)
        return result

    def find_count(self, index:str=None, doc_type:str=None) -> Dict:
        """
        查询数据总数
        """
        return self.conn.count(index=index, doc_type=doc_type)
    
    def find_all_index(self) -> Dict:
        """
        查询所有索引
        """
        return self.conn.indices.get_alias("*")
    
    def add(self, index: str = None, doc_type=None, id: int = None, body: Dict = None) -> Dict:
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
    
    def update(self, index:str=None, doc_type=None, id:int=None, body:Dict=None, query:Dict=None) -> Dict:
        """
        更新数据
        """
        
        # 条件更新
        if query is not None:
            return self.conn.update_by_query(index=index, doc_type=doc_type, body=query)
        
        # 单条更新
        return self.conn.update(index=index, doc_type=doc_type, id=id, body=body)
        
    def delete(self, index:str=None, doc_type:str=None, id:int=None, query:Dict=None) -> Dict:
        """
        删除数据
        """
        # 根据ID删除
        if id is not None:
            return self.conn.delete(index=index, doc_type=doc_type, id=id)
        
        # 条件查询
        if query is not None:
            return self.conn.delete_by_query(index=index, body=query)
        
        # 直接删除索引
        return self.conn.indices.delete(index)

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