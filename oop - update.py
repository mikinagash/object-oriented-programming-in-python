#q1
# class Circle:
#     def __init__(self,area=25,color="blue"):
#         self.__area = area
#         self.__color = color
#         self.__radius= 4
#
#     def getArea(self):
#          return self.__area
#
#     def setColor(self,color):
#         self.__color = color
#
#     def getColor(self):
#         return self.__color
#     def __str__(self):
#         return str(self.__area) + '  '+ self.__color
#
#     def setArea(self):
#         self.__area = 3.14*self.__radius**2
#         return self.__area
#
#
# class Square:
#     def __init__(self,area = 30,color= "black"):
#         self.__area = area
#         self.__color = color
#         self.__left_side = 5
#
#     def setArea(self):
#         self.__area =  4 * self.__left_side * 4
#         return self.__area
#
#     def getArea(self):
#          return self.__area
#
#     def setcolor(self,color):
#         self.__color = color
#
#     def getcolor(self):
#         return self.__color
#
#
#     def __str__(self):
#         return str(self.__area) + '  '+ self.__color
#
# circle = Circle()
# square = Square()
# # square.setArea(20)
# # print(square.getArea())
# print(circle.setArea())
# print(square.setArea())

#q2
# class Apartment:
#     def __init__(self,addrass,aprtmentNumber,sellPrice,rentPrice):
#         self.__addrass = addrass
#         self.__aprtmentNumber = aprtmentNumber
#         self.__sellPrice = sellPrice
#         self.__rentPrice = rentPrice
#
#     def getyieldd(self):
#         yieldd = self.__rentPrice * 12 / self.__sellPrice
#         return yieldd
#
#     def __str__(self):
#         return  self.__addrass + '  '+ str(self.__aprtmentNumber) + '  '+ str(self.__sellPrice)+ ' '+ str(self.__rentPrice)
#
# aprtment1 = Apartment("haifa",5,1000,10)
# print("apartment details :",aprtment1,"\nthe yield is :",aprtment1.getyieldd())

#Q3

# class Cat:
#     def __init__(self,name,age,hairColor):
#         self.__name = name
#         self.__age = age
#         self.__hairColor = hairColor
#     def getsound(self):
#         sound = "mio mio"
#         return sound
#     def getmustach(self):
#         if self.__age >5:
#          return "yes!"
#
# class Dog:
#     def __init__(self,name,type,color):
#         self.__name = name
#         self.__type = type
#         self.__color = color
#     def getsound(self):
#         sound = "how how"
#         return  sound
#     def getbarking(self):
#         if self.__type == "pitbull":
#             return "yes"
#
#
# cat1 = Cat("mizi",6,"rad")
# cat2 = Cat("nizi",2,"black")
# dog1 = Dog("fasil","pitbull","black")
# dog2 = Dog("yosef","lavrador","rad")
# print(cat1.getsound())
# print(cat2.getsound())
# print(dog1.getbarking())
# print(dog2.getbarking())
# print(dog1.getsound())
# print(dog2.getsound())



# q4
# class Cars:
#     def __init__(self,price,year,model,wheels):
#         self.__price = price
#         self.__year = year
#         self.__model = model
#         if wheels < 4:
#             print("impossible")
#             self.__wheels =4
#         else:
#             self.__wheels = wheels
#     def getwheels(self):
#         return self.__wheels
#
#     def getprice(self):
#         return self.__price
#
#     def setwheels(self,wheels):
#         self.__wheels = wheels
#
#     def __str__(self):
#         return str(self.__price)+'  '+str(self.__year)+'  '+self.__model+'  '+str(self.__wheels)
#
# car1 = Cars(300000,2022,"lambo",4)
# car2 = Cars(200000,2021,"rrari",4)
# car3 = Cars(100000,2020,"banz",2)
# print(car3.setwheels(4))
#
# cars = [car1,car2,car3]
# def maxcar(list_name):
#     max_num = 0
#     for i in range(len(cars)):
#         if cars[i].getprice() > cars[i+1].getprice():
#             max_num = cars[i]
#         else:
#             max_num = cars[i+1]
#         return  max_num
# a = maxcar(cars)
# print(a)

# Q5
# class Student:
#     def __init__(self,name,id,mathScore,historyScore,literature,classs,dateOfBirth):
#         self.__name = name
#         self.__id = id
#         self.__mathScore = mathScore
#         self.__historyScore = historyScore
#         self.__literature = literature
#         self.__classs = classs
#         self.__dateOfBirth = dateOfBirth
#
#     def getage(self):
#         age = 2022 - self.__dateOfBirth
#         return age
#
#     def getavgscore(self):
#         averag = self.__mathScore + self.__historyScore + self.__literature // 3
#         return averag
#
#     def getdiploma(self):
#         avg = (self.__mathScore + self.__historyScore + self.__literature) // 3
#         a = (self.__name,self.__id,self.__mathScore,self.__historyScore,self.__literature,avg)
#         if avg >90:
#             print("NAME:",a[0],"\tID:",a[1],"\nMath score: ",a[2],"\nHistory score:",a[3],"\nLiterature score:",a[4])
#             print("*********************")
#             print("averag:",a[5] ,"\npassed with distinction !!!")
#         elif avg < 60:
#             print("NAME:", a[0], "\tID:", a[1], "\nMath score: ", a[2], "\nHistory score:", a[3], "\nLiterature:", a[4])
#             print("*********************")
#             print("averag:", a[5], "dident passed")
#         else:
#             print("NAME:", a[0], "ID:", a[1], "Math score: ", a[2], "History score:", a[3], "Literature:", a[4])
#             print("*********************")
#             print("averag:", a[5], "\npassed")
#
#
#     def __str__(self):
#         return self.__name +'  '+str(self.__id)+'  '+str(self.__mathScore)+'  '+str(self.__historyScore)+'  '+str(self.__literature)+'  '+self.__classs+'  '+str(self.__dateOfBirth)
#
# studens1 = Student("miki",1,85,95,100,"qa",1997)
# studens2 = Student("fasil",2,54,90,82,"qa",1996)
# studens3 = Student("daniel",3,100,98,100,"fullstuck",20000)
# studens4 = Student("eli",4,100,10,10,"qa",1979)
# studens3.getdiploma()
#
# students = [studens1,studens2,studens3,studens4]
# def maxaverag(list_name):
#     max_avg = 0
#     for i in range(len(students)):
#         if students[i].getavgscore() > students[i+1].getavgscore():
#             max_num = students[i]
#         else:
#             max_num = students[i+1]
#         return  max_num
# a = maxaverag(students)
# print(a)
