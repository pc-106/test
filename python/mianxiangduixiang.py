class Student:
    name=None
    age=None
    gender=None
    def say(self):
        print(f"我是一个学生，我的姓名是{self.name}，我的年龄是{self.age}，我的性别是{self.gender}")
    def say1(self,msg):
        print(msg)
stu_1=Student()
stu_1.name="张山"
stu_1.age=18
stu_1.gender="男"
print(stu_1.name,stu_1.age,stu_1.gender)
stu_1.say()
stu_1.say1("hello")
class Clock:
    id=None
    price=None
    def show(self):
        print(f"我是一个时钟，我的id是{self.id}")
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
clock_1=Clock() 
clock_1.id="0001"
clock_1.price=19.99
print(clock_1.id,clock_1.price)
clock_1.show()
# clock_1.ring()
class student:
    name=None
    age=None
    gender=None
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(f"我是一个学生，我的姓名是{self.name}，我的年龄是{self.age}，我的性别是{self.gender}")
    # def __str__(self):
    #     return f"我是一个学生，我的姓名是{self.name}，我的年龄是{self.age}，我的性别是{self.gender}"
    def __lt__(self,other):
        return self.age<other.age
    def __le__(self,other):
        return self.age<=other.age
    def __eq__(self,other):
        return self.age==other.age
student_1=student("张山",18,"男")
print(student_1)
student_2=student("李四",20,"男")
print(student_2<student_1)
print(student_1<student_2)
print(student_2>student_1)
print(student_1>student_2)
print(student_2>=student_1)
print(student_1==student_2)
class Phone:
    id=None
    producer="Apple"
    __current_voltage=3
    def __keep_single_core(self):
        print("我是一个单核处理器")
    def call_by_5g(self):
        if self.__current_voltage>=1.0:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法开启5g通话")
phone=Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
phone.call_by_5g()
class Phone1(Phone):
    face_id=None
    producer="xiaomi"
    def call_by_5g(self):
        # super().call_by_5g()
        Phone.call_by_5g(self)
        print("开启了5g通话")
        print(f"我是一个{super().producer}手机")
    def call_by_face_id(self):
        if self.face_id!=None:
            print("通过面部识别开启通话")
        else:
            print("未开启面部识别，无法开启通话")
phone_1=Phone1()
phone_1.id=1
phone_1.face_id="0001"
phone_1.call_by_face_id()
print(phone_1.id,phone_1.producer)
class show():
    def show_info(self):
        print(f"我是一个{self.producer}手机，我的id是{self.id}")
class NFCReader:
    nfc_type="xiaomi"
    def read_nfc(self):
        print(f"我是一个{self.nfc_type}NFC阅读器")
class RemoteControl:
    remote_type="apple"
    def control(self):
        print(f"我是一个{self.remote_type}遥控器")
class Myphone(Phone1,NFCReader,RemoteControl,show):
    pass
    def __init__(self,id,face_id,nfc_type,remote_type):
        self.id=id
        self.face_id=face_id
        self.nfc_type=nfc_type
        self.remote_type=remote_type
phone_2=Myphone(2,"0002","xiaomi","apple")
phone_2.show_info()
phone_2.read_nfc()
phone_2.control()
print(phone_2.producer)
phone_2.call_by_5g()
a:int=10   #type:int
b:float=10.0
c:str="hello"
d:bool=True
my_list:list[int,float,str,bool]=[1,2.0,"hello",True]
def add(x:int,y:int)->int:
    return x+y
print(add(1,2))
from typing import Union
my_list:list[Union[int,float,str,bool]]=[1,2.0,"hello",True,None,3]
my_dict:dict[str,Union[int,float,str,bool]]={"a":1,"b":2.0,"c":"hello","d":True}
def get_value(my_dict:dict[str,Union[int,float,str,bool]],key:str)->Union[int,float,str,bool]:
    return my_dict[key]
print(get_value(my_dict,"a"))
class Animal:
    def speak(self):
        print("动物会说话")
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
        super().speak()
class Cat(Animal):
    def speak(self):
        print("喵喵喵") 
        super().speak()
def text(animal:Animal):
    animal.speak()
dog=Dog()
text(dog)
cat=Cat()
text(cat)
