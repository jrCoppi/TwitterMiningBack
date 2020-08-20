#Import reading module
#From Folder.File import Class
from Reader.Read import Read
from Filter.Filtering import Filtering
from Data.Operation import Operation

term = 'hamilton'

#Initialize all the class
operation = Operation()
read = Read()
filtering = Filtering()

#Executes the reading
inputData = read.execute(term)
inputData = filtering.execute(inputData)

operation.saveSearch(inputData,term)