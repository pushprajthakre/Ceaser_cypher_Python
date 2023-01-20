#function 
def ceaser(ps,n):
    result = ""
    for i in range(len(ps)):
      if (ps[i].isupper()):
          result+=chr((ord(ps[i])+(n-65))%26+65)+chr(ord(ps[i])-60)
      else:
          result+=chr((ord(ps[i])+(n-97))%26+97)+chr(ord(ps[i])-60)
    return result
# Code starts from here
ps = input("Enter Any password: ")
n = int(input("Enter pattern: "))
# Output screen code start
print("\nReport of Ceaser Cypher")
print("*************************")
print("Plain Password is : "+ ps)
print("Pattern is : "+ str(n))
print("Cipher Password is : " + ceaser(ps,n))
# Created By Raj pawar
