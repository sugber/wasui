def abc(a,b,__c={}):
    if (a,b) in __c:
        return __c[(a,b)]

    e = a + b
    print("hahah")
    __c[(a,b)] =e
    return e

print(abc(1,2))
print(abc(1,2))
print(abc(1,2))
print(abc(1,2))
print(abc(1,2))
print(abc(1,2))
print(abc(1,2))
print(abc(1,2))