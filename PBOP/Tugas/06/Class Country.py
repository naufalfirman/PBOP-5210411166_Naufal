# Plymorhism
# Simple Example using len function

print(len("Polymorphism"))
print(len([1,2,3,4]))

# using class 
class jerman :
    def ibukota(self):
        print("berlin adalah ibukota negara jerman")
class jepang :
    def ibukota(self):
        print("Tokyo adalah ibukota negara jepang")

negara = jerman()
ngr = jepang()
for i in (negara, ngr):
    i.ibukota()
