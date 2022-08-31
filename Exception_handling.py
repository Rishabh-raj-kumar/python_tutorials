
try : 
 numirator= int(input("Enter a number : "))
 denominator=int(input("Enter a number2 : "))
 z= numirator/denominator
 print(z)

except ValueError :
    print("ok")

except Exception:
    print("Error ;(")