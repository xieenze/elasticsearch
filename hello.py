#coding:utf8
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


#连接elasticsearch,默认是9200
es = Elasticsearch([{'host':'192.168.1.110','port':9200}])
def create():
    #判断索引是否存在
    flag = es.exists(index="tj_xieenze",doc_type="test-type", id=1)
    if flag ==True:
        #删除索引中得数据
        #es.delete(index="test-index",doc_type="test-type", id=1)
        #删除整个索引
        es.indices.delete(index="tj_xieenze")
    else:
        #创建索引
        es.indices.create(index="tj_xieenze")
        #创建索引并插入数据
        #es.create(index="tj_xieenze", doc_type="test-type", id=1,body={"any":"data", "timestamp": datetime.now()})


def search():
    search = es.search(index='tj_xieenze')
    print search

def count():
    count = es.count(index='tj_xieenze')
    print count
def index():
    es.index(index='tj_xieenze',doc_type='test-type', id=42, body={'any': "data", "timestamp": datetime.now()})
def get():
     es.get(index='tj_xieenze', doc_type='test-type', id=42)['_source']


#index()
#批量插入数据
#for i in range(100,1000):
    #es.create(index="tj_xieenze", doc_type="test-type", id=i,body={"any":"data", "timestamp": datetime.now()})
#查询方法
def search_matchAll():
    res=es.search(
        index='tj_xieenze',
        doc_type='test-type',
        body={
          'query': {
            'match_all': {}
          }
        }
    )
    print res['hits']['hits']
def search_match_or_range():
    res = es.search(
        index='tj_xieenze',
        doc_type='test-type',
        body={
          'query': {
            'match': {
              '_id': '120'
            }
          }
        }
    )
    es.search(
        index='tj_xieenze',
        doc_type="test-type",
        body={
            'query':{
                "range":{
                    '_id':{
                        'from':"120",'to':'122'
                    }
                }
            }
        }
    )['hits']['hits']



#参考
#http://www.tuicool.com/articles/IjURvey
#http://www.cnblogs.com/letong/p/4749234.html
#http://www.jb51.net/article/63731.htm
