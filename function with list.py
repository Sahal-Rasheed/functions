list=[1,2,3,4,5]
sum=0
for i in list:
    sum=sum+i

print(sum)

def pro(list):
    product=1
    for i in list:
        product=product*i
    return product

print(pro(list))



def exponent(list):
    new = []
    for i in list:
         new.append(i*i)
    return new

print(exponent(list))








