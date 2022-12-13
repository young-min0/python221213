# DemoList.py
strA = "abcdefghijk"
print( strA )
print( len(strA) )
print( strA[0:3] )
print( strA[:3] )
print( strA[-3:] )

print("---list---")
colors = ["red", "blue", "green"]
print( len(colors) )
print( colors[0] )
colors.append("black")
colors.insert(1,"white")
print( colors )
#카운트
print( colors.count("blue") )
#방번호
print( colors.index("green") )
colors.remove("green")
print( colors )
colors.extend( ["red", "yellow", "black"])
print( colors )


print("---set---")
a = {1,2,3,3}
b = {3,4,4,5}
print( a )
print( b )
print( type(a) )
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )
