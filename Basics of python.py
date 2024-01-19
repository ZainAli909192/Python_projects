# dictionary
# Syntax:  variable={"keys":"values","keys":"values"}
dict={"zain":"ali",
      "set":"Wel defined object "}
# print(dict)
# key=input("Enter key: ")
# print(dict[key])

# dict.clear()
# dic=dict.keys()         #to get keys of dictionary
# dic=dict.values()       #to get values of dictionary
# dict2=dict.copy()       #to copy one dictionary to other
# print(dict2.items())
# print(type(dict))

# import time
# # x = time.asctime(time.localtime(time.time()))
# x=10
# x=time.sleep(4)
# print(x)

# list
list=["zain","ali"]
# list=list*2;    # making copy of same data
# list.insert(2,"ahmed")
# print(list)
# list2=list.copy()
# list.append("malik")
# list.sort()
# print(list);

# if list.__contains__("zain"):
#     print(list)
# print(list.__delitem__(0))
# print(list)
# print(type(list))

# tuple
dict=("Ali","Awon")
# print(dict)
# print(type(dict))

            # ---try catch----
# try:
#   x=["malik","zain"]
#   print(x[7])
# except Exception as e:
#   print("Error: ",e)
# finally:
#   print("The 'try except' is finished")

            # ---join function--
# Syntax: variable=" through which u want to jon? e.g and or comma".join(list/dict)
# set={"zain","ali","ahmed"}
# print(type(set))
# a=" hi ".join(list)
# print(a)

        # --encapsulation (private,public,protected)
# class a():
#      __name="a"    # private variable
# class b(a):
#     _name="b"       # protected variable
# class c(b,a):
#         name="c"
# A=a()
# B=b()
# # C=c()
# print(B._name)         # calling protected variable
# print(A._a__name)      # calling private variable

#
# class student():
#     name="";
#     course=[];
#     marks=[];
#     grade=[];
#     cgpa="";

   #constructor
#     def __int__(self,name):
#         self.name=name;
#     # storing data
#     def store(self,course,marks):
#         self.course.append(course);
#         self.marks.append(marks);
#         if(marks>80):
#             self.grade="A";
#         elif(marks>70):
#             self.grade="B";
#         elif(marks>60):
#             self.grade="C";
#         else:
#             self.grade="F";
#     def gpa(self):
#         marks
#     def show(self):
#         print("Name is: "+self.name)
# st=student();
# st.show();

# name = "";
# course = ["SE","CS"];
# marks = [90,90];
# grade = [];
# cgpa = 0.0;
# allotedmarks=[];
# gpa=0.0;
#
# name=input("enter name: ");
# currentcgpa=input("Enter your current cgpa: ");
# try:
#     for i in marks:
#         if (i>=90):
#             allotedmarks.append(4);
#         elif (i >= 80):
#             allotedmarks.append(3);
#         elif (i >= 70):
#             allotedmarks.append(2);
#     list=0;
#     for j in allotedmarks:
#         list+=j;
#     inn=len(marks);
#     gpa=list/inn;
#     i=0;
#     while(i<len(marks)):
#         print("You got ",marks[i] ," in  ", course[i])
#         i+=1;
#     print(name,"your gpa is", gpa)
#     cgpa=(currentcgpa+gpa)/2;
    # print(name,"your cgpa is",cgpa)

# except Exception as e:
#   print("error",e)

marks=[75,67,80,90,95]
# marks={75:67,80:90,95:34}
try:
    for i in marks:
        if i>=78:
            print(i)
except Exception as e:
    print(e)