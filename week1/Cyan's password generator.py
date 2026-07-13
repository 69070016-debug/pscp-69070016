"""this is password generator"""
name = input()
sur = input()
age = input()
if len(name) >= 5 and len(sur) >= 5:
    password = name[0:2]+sur[-1]+age[-1]
else:
    password = name[0]+age+sur[-1]
print(password)
