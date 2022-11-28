#importing itertools library to 
import itertools as its

#main characters which must contain our password list(you can change them if you know more about your victim's password)
words = "1234567890abcdefghijklmnopqrstuvwxyz" # a set of password characters
r =its.product(words,repeat=8)  # random combination of 8 characters (
dic = open("pwd.txt","a")      # store wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()


