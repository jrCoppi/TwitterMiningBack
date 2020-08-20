from Data.Base import Base
from datetime import datetime

class Operation():
    base = ''

    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        self.base = Base()

    def saveSearch(self,data,term):
        termId = self.createTerm(term)
        searchId = self.createSearch(termId)

        for post in data:
            postId = self.createPost(post)
            postId = self.createSearchPost(postId,searchId)
            

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
        query = "INSERT INTO post (ds_post) VALUES (%s)"

        values = (post,)
        return self.base.insertData(query,values)
    
    
    def createSearchPost(self,postId,searchId):
        ## defining the Query
        query = "INSERT INTO pesquisa_post (id_post, id_pesquisa) VALUES (%s, %s)"

        ## storing values in a variable
        values = (postId, searchId)
        return self.base.insertData(query,values)
