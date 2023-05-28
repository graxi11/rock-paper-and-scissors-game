# CREATING CLASS!
class Person:
  def __init__(self, name, room, age):
    self.name = name
    self.room = room
    self.age = age 

  def myfunc(self):
    print(self.name) 
    print(self.room)
    print(self.age)

  def compare(self,me):
    if self.age > me.age:
      return True
    else:
      return False
  

p2  = Person('graxi', '59', int(234))
p1 = Person('jim','105', int(59))
p1.name = 'graxi'

if p1.compare(p2):
  print('greater')
else:
  print('lesser')


#p1.myfunc()
#p2.myfunc()

#NEW ONE!
class Person:
  def __init__(self):
    self.name = 'lala'
    self.age = 28
    self.month = 'april'

  def compare(self,other):
    if self.name == other.name:
      return True
    else:
      return False

p2 = Person()
p1 = Person()
p1.name = 'james'


if p2.compare(p1):
  print('they are the same ')
else:
  print('they are not the same')

#new2
class A():
  def __init__(self, fn, lm):
    self.fn = fn
    self.lm = lm
 
  def feature2(self):
    print(self.lm, self.fn)

class B(A):
  def __init__(self, fn, lm):
    super().__init__(self, fn, lm)


al = A('lala', int(84))
ae = A('garxi', 'love')
al.feature2()
ae.feature2()

#new3
class human:
    def __init__(self, male, female):
        self.male = male
        self.female = female

    def omo(self):
        print('welcome', self.male, 'and', self.female, 'to this class ')

class Race(human):
    def __init__(self, male, female):
      super().__init__(male, female)
      self.name = 'hello', male, female 
    
p7 = human('man', 'woman')
p8 = human('tobi', 'cynthia')
p6 = Race('black', 'white')
p5 = Race('tobi', 'cynthia')

p8.omo()
print(p5.name)

#new
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#new
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 5:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
#new
x = 234

def myfunc():
  x = 'ue'
  def myinnerfunc():
    print(x)


  myinnerfunc()
myfunc()
print(x)

#import it won't work because it not the same name!
import test
greeting = {
    'name': 'jonathan',
    'age': '34',
    'country': 'nigeria'
}
y = test.greeting["age"]
print(y)
#new datetme
import datetime as dt

x = dt.datetime.now()
print('year:', x.year)
print('month', x.month)
print('day', x.day  )
print('hour', x.hour)
print('minute', x.minute)
print('second', x.second)
print('microsecond', x.microsecond) 

print(x.date())
print(x.time()) 
print(x)

#la
import datetime as dt

current = dt.datetime.now()

print(current)

string = current.strftime('%d, of %B, %Y')
print(string)

#e
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])

#loads in python
from json import load, loads

x = '{"message": "success", "timestamp": 1681218291, "iss_position": {"longitude": "23.8067", "latitude": "47.3381"}} '

print(type(x))  

y = loads(x)
print(type(y))

print(y['timestamp'])
print(y['iss_position']['latitude'])
print(y['iss_position']['longitude'])
print(y['message'])

with open('test.json') as y:
    pythonDictionary = load(y)
print(pythonDictionary)

print(pythonDictionary['timestamp'])
print()

#REGex
import re

pattern = re.compile('^[a-zA-Z]{10}[0-9]{2,6}[^a-zA-Z0-9]{2}$')

print(pattern.search('aAqweasdfg12#$'))

x = ('my back hurts hurts')

print(re.findall('m.', x))
print(re.sub('\s', 'lower', x, 1))
print(re.search('ur', x))
print(re.split('\s', x, 1))

#
txt = 'the rain in spain'

r = re.search(r"\bs\w+", txt)
print(r.string)
print(r.span())
print(r.group(), 'nam')

#raise an exception
x = input('enter a digit ')
if x.isdigit():
  x = int(x)

  if x.isdigit < 0:
    raise Exception("Sorry, no numbers below zero")


#string format
quantity = 3
itemno = 425
price = 23
myorder = 'i want {} pieces of item number {} for {:.2f} dollars.'
print(myorder.format(quantity, itemno, price))

#named index
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
