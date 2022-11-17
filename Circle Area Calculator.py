try:
    print("Hello... How big is the radius of the circle you want to measure????")
    Ca = input()
    print("So the area of the circle is ", int(Ca) * int(Ca) * 3.14, "cm²", sep="")
except ValueError:
    print("You Can't Multiply Letters, or Decimal Numbers (Im Sure You Could But Im Too Lazy To Do That) ·_·")
except :
    print("N O")