# filter() -> create a collection of element from an iterable for which a function return a statement..

#filter(function,iterable)

freinds=[("Richa",6),("Mich",7),("bitch",3),("cringe",2)];

age = lambda data:data[1] >3

drinks = tuple(filter(age,freinds))

for it in drinks:
    print(it)

#reduce() -> recycle,reduce,reuse...
#apply a function to an iterable and reduce it to a single value
#performs function on first two elements then repeat till 1 value remaining..
#reduce(function,iterable)
import functools

factorial=[5,4,3,2,1]
word = functools.reduce(lambda x,y:x*y,factorial)
print(word)


