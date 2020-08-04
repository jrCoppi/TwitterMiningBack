#Import reading module
#From Folder.File import Class
from Reader.Read import Read
from Filter.Filtering import Filtering

#Initialize all the class
read = Read()
filtering = Filtering()

#Executes the reading
inputData = read.execute("nvidia")
inputData = filtering.execute(inputData)