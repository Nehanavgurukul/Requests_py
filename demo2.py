# import requests

# req = requests.get("http://saral.navgurukul.org/api/courses")

# print(req.text)  

import requests
import json
import os

req = requests.get("http://merakilearn.org/api/courses")

list_Id = []
s = json.dumps(req.json(), indent=4)
with open('Acourses.json','w') as myjsonfile:
    myjsonfile.write(s)

py_obj = open('Acourses.json','r') 
my_file = json.load(py_obj)
py_obj.close()


for i in my_file : 
    if(i == "availableCourses"):
        list = my_file[i]

j = 0
c = 0
slug_list = []
while (j<len(list)):
    dic = list[j]
    for x in dic :
        if(x == "id"):
            a = dic[x]
            list_Id.append(dic[x])
        if(x == "name"):
            print(c,":", dic[x],"-",a)
            print()
            c = c+1
    j = j + 1

print("*************LIST OF ID****************")
print()
print(list_Id)
print()
print("*************COURSE OF INDEX****************")
course_index = int(input("choose any course by index - "))
j = 0
c = 0
while (j<len(list)):
    dic = list[j]
    for x in dic :
        if(x == "name"):
            if(course_index == c):
                print()
                print(course_index,":",dic[x])
                print()
            c = c+1
    j = j + 1


print("***************PERENTS-EXERCISE*****************")
print()


reques = requests.get("http://merakilearn.org/api/courses/" + list_Id[course_index] + "/exercises")
# print(reques.text)

json_file = json.dumps(reques.json(), indent = 4)
with open ("Bcourses" +str (course_index) +".json","w") as file_json :
    file_json.write(json_file)

with open ("Bcourses" +str (course_index) +".json","r") as Obj:
    Obj_File = json.load(Obj)
    Obj.close()
    # print(Obj_File)

my_List = Obj_File["data"]

n = 1
slugList = []
for y in my_List:
    dict1 = y
    for z in dict1 :
        if(z == "name"):
            print(n , dict1[z])
            n = n + 1
        elif(z == "childExercises"):
            if(len(dict1[z]) >=1):
                child_list = dict1[z]
                for p in child_list:
                    dict2 = p 
                    for t in dict2 :
                        if(t == "name"):
                            print("   ",dict2[t])
                            print()
            else:
                print("   ",dict1[z])
        elif(z == "slug"):
            slugList.append(dict1[z])
print(slugList)
slug_index = int(input("enter the slug_index"))
slug_id = slugList[slug_index]

slug_obj = requests.get("http://saral.navgurukul.org/api/courses/"+list_Id[course_index]+"/exercise/getBySlug?slug="+slug_id)
slug_file = json.dumps(slug_obj.json(),indent = 4)
with open ("SlugFile.json","w") as file_slug:
    file_slug.write(slug_file)
    
with open ("SlugFile.json","r") as obj_slug:
    my_slug = json.load(obj_slug)
    obj_slug.close()
    for n in my_slug:
        if(n == "content"):
            print(my_slug[n])

# print(my_slug)

i = 0
tru = True
while(tru):
    user_next = input("enter your choise - /next / previous / up /stop - ")

    if(user_next == "up"):
        req = requests.get("http://merakilearn.org/api/courses")

        list_Id = []
        s = json.dumps(req.json(), indent=4)
        with open('Acourses.json','w') as myjsonfile:
            myjsonfile.write(s)

        py_obj = open('Acourses.json','r') 
        my_file = json.load(py_obj)
        py_obj.close()


        for i in my_file : 
            if(i == "availableCourses"):
                list = my_file[i]

        j = 0
        c = 0
        slug_list = []
        while (j<len(list)):
            dic = list[j]
            for x in dic :
                if(x == "id"):
                    a = dic[x]
                    list_Id.append(dic[x])
                if(x == "name"):
                    print(c,":", dic[x],"-",a)
                    print()
                    c = c+1
            j = j + 1

        print("*************LIST OF ID****************")
        print()
        print(list_Id)
        print()
        print("*************COURSE OF INDEX****************")
        course_index = int(input("choose any course by index - "))
        j = 0
        c = 0
        while (j<len(list)):
            dic = list[j]
            for x in dic :
                if(x == "name"):
                    if(course_index == c):
                        print()
                        print(course_index,":",dic[x])
                        print()
                    c = c+1
            j = j + 1


        print("***************PERENTS-EXERCISE*****************")
        print()


        reques = requests.get("http://merakilearn.org/api/courses/" + list_Id[course_index] + "/exercises")
        # print(reques.text)

        json_file = json.dumps(reques.json(), indent = 4)
        with open ("Bcourses" +str (course_index) +".json","w") as file_json :
            file_json.write(json_file)

        with open ("Bcourses" +str (course_index) +".json","r") as Obj:
            Obj_File = json.load(Obj)
            Obj.close()
            # print(Obj_File)

        my_List = Obj_File["data"]

        n = 1
        slugList = []
        for y in my_List:
            dict1 = y
            for z in dict1 :
                if(z == "name"):
                    print(n , dict1[z])
                    n = n + 1
                elif(z == "childExercises"):
                    if(len(dict1[z]) >=1):
                        child_list = dict1[z]
                        for p in child_list:
                            dict2 = p 
                            for t in dict2 :
                                if(t == "name"):
                                    print("   ",dict2[t])
                                    print()
                    else:
                        print("   ",dict1[z])
                elif(z == "slug"):
                    slugList.append(dict1[z])
        print(slugList)
        slug_index = int(input("enter the slug_index"))
        slug_id = slugList[slug_index]

        slug_obj = requests.get("http://saral.navgurukul.org/api/courses/"+list_Id[course_index]+"/exercise/getBySlug?slug="+slug_id)
        slug_file = json.dumps(slug_obj.json(),indent = 4)
        with open ("SlugFile.json","w") as file_slug:
            file_slug.write(slug_file)
            
        with open ("SlugFile.json","r") as obj_slug:
            my_slug = json.load(obj_slug)
            obj_slug.close()
            for n in my_slug:
                if(n == "content"):
                    print(my_slug[n])
        # print(my_slug)

    elif(user_next == "previous"):
        if(slug_index == 0):
            print("there no previous slug")
        else:
            slug_id = slugList[slug_index-1]

            slug_obj = requests.get("http://saral.navgurukul.org/api/courses/"+list_Id[course_index]+"/exercise/getBySlug?slug="+slug_id)
            slug_file = json.dumps(slug_obj.json(),indent = 4)
            with open ("SlugFile.json","w") as file_slug:
                file_slug.write(slug_file)
                
            with open ("SlugFile.json","r") as obj_slug:
                my_slug = json.load(obj_slug)
                obj_slug.close()
                for n in my_slug:
                    if(n == "content"):
                        print(my_slug[n])
            # print(my_slug)

    elif(user_next == "next"):
        if(slug_index == len(slugList)-1):
            print("there  no next slug")
        else:
            # print(slugList[slug_index +1])
            slug_id = slugList[slug_index+1]

            slug_obj = requests.get("http://saral.navgurukul.org/api/courses/"+list_Id[course_index]+"/exercise/getBySlug?slug="+slug_id)
            slug_file = json.dumps(slug_obj.json(),indent = 4)
            with open ("SlugFile.json","w") as file_slug:
                file_slug.write(slug_file)
                
            with open ("SlugFile.json","r") as obj_slug:
                my_slug = json.load(obj_slug)
                obj_slug.close()
                for n in my_slug:
                    if(n == "content"):
                        print(my_slug[n])
            # print(my_slug)

    elif(user_next == "stop"):
        tru = False

        

    


