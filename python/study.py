print("hello world")
my_set={1,2,3,4,5}
print(my_set)
my_set.add("python")
print(my_set)
my_set.remove(1)
print(my_set)
element=my_set.pop()
print(element)
print(my_set)
my_set.clear()
print(my_set)
set_1={1,2,3}
set_2={1,4,5}
set_3=set_1.difference(set_2)
print(set_3)
set_1.difference_update(set_2)
print(set_1)
set3=set_1.union(set_2)
print(set3)
num=len(set3)
print(num)
for i in set3:
    print(i,end=" ")
print("")
my_list=["a","b","c","d","e"]
set_4=set()
for i in my_list:
    set_4.add(i)
print(set_4)
dict3={
    "python":3,
    "java":2,
    "c++":1
}
dict1={}
dict2=dict()
print(dict3,dict2,dict1)
print(dict3["python"],dict3["java"],dict3["c++"])
dict_1={
    "python":{
        "version":"3.10",
        "release_date":"2021-10-04"
    },
    "java":{
        "version":"17",
        "release_date":"2021-09-14"
    },
    "c++":{
        "version":"17",
        "release_date":"2021-09-14"
    }
}
print(dict_1["python"]["version"])
print(dict_1["java"]["release_date"])
print(dict_1["c++"]["version"])
dict3["python"]=3.11
print(dict3)
source=dict3.pop("c++")
print(source)
print(dict3)
for key in dict3.keys():
    print(key,":",dict3[key])
for i in dict3:
    print(i,":",dict3[i])
len_dict3=len(dict3)
print(len_dict3)