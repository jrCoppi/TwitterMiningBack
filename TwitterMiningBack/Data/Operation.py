from Data.Base import Base
from Data.Mongo import Mongo
from datetime import datetime

class Operation():
    base = ''
    mongo = ''

    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        self.base = Base()
        self.mongo = Mongo()

    def saveSearch(self,data,term):
        termId = self.createTerm(term)
        searchId = self.createSearch(termId)

        for post in data:
            postId = self.createPost(post)
            postId = self.createSearchPost(postId,searchId)
        
        return searchId
            

    def createTerm(self,term):
        query = "SELECT id_termo FROM termo WHERE ds_termo = '" + term + "'"
        currentTerm = self.base.selectData(query)
        
        if len(currentTerm) > 0:
            return currentTerm[0][0]
        
        ## defining the Query
        query = "INSERT INTO termo (ds_termo) VALUES (%s)"

        ## storing values in a variable
        values = (term,)

        return self.base.insertData(query,values)

    def createSearch(self,termId):
        ## defining the Query
        query = "INSERT INTO pesquisa (dt_pesquisa, id_termo) VALUES (%s, %s)"

        ## storing values in a variable
        today = datetime.now()
        values = (today.strftime("%Y-%m-%d %H:%M:%S"), termId)

        return self.base.insertData(query,values)
    
    def createPost(self,post):
        ## defining the Query
        query = "INSERT IGNORE INTO post (ds_post) VALUES (%s)"

        values = (post,)
        return self.base.insertData(query,values)
    
    
    def createSearchPost(self,postId,searchId):
        ## defining the Query
        query = "INSERT IGNORE INTO pesquisa_post (id_post, id_pesquisa) VALUES (%s, %s)"

        ## storing values in a variable
        values = (postId, searchId)
        return self.base.insertData(query,values)

    def getResults(self,searchId):
        query = "SELECT po.ds_post FROM pesquisa p INNER JOIN pesquisa_post pp ON ( pp.id_pesquisa = p.id_pesquisa) INNER JOIN post po ON ( pp.id_post = po.id_post) where p.id_pesquisa = '" + searchId + "'"
        result = self.base.selectData(query)
        return result
    
    def getMostSearched(self):
        query = "SELECT t.ds_termo, COUNT(t.id_termo) as nr_ocorrencia FROM termo t INNER JOIN pesquisa p ON ( p.id_termo = t.id_termo ) GROUP BY t.id_termo desc  ORDER BY nr_ocorrencia desc LIMIT 10"
        result = self.base.selectData(query)
        return result
    
    def getLatestSearchs(self):
        query = "SELECT p.id_pesquisa, t.ds_termo FROM pesquisa p inner join termo t ON (t.id_termo = p.id_termo) order by p.dt_pesquisa desc limit 10"
        result = self.base.selectData(query)
        return result

    def logSearch(self,term,data):
        ## storing values in a variable
        today = datetime.now()

        item = {
            "term" : term,
            "data" : today.strftime("%Y-%m-%d %H:%M:%S"),
            "log" : {
                "log" : data
            }
        }

        self.mongo.insertData('search',item)

    def getLog(self,term):
        item = {
            "term" : term
        }

        return self.mongo.findMany('search',item)