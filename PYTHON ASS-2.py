Python 3.9.8 (tags/v3.9.8:bb3fdcf, Nov  5 2021, 20:48:33) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= int(input("ENTER THE SIDE OF SQUARE ="))
ENTER THE SIDE OF SQUARE = 10
>>> area= a*a
>>> print("AREA OF SQUARE =",area)
AREA OF SQUARE = 100
>>> 
>>> 
>>> l=int(input("ENTER THE LENGTH OF RECTANGLE ="))
ENTER THE LENGTH OF RECTANGLE = 5
>>> b=int(input("ENTER THE BREADTH OF RECTANGLE ="))
ENTER THE BREADTH OF RECTANGLE = 7
>>> AREA=l*b
>>> print(" AREA OF RECTANGLE =",AREA)
 AREA OF RECTANGLE = 35
>>> 
>>> 
>>> r= int(input("ENTER THE RADIUS OF CIRCLE ="))
ENTER THE RADIUS OF CIRCLE = 6
>>> area= 3.14* r*r
>>> print("AREA OF CIRCLE =", area)
AREA OF CIRCLE = 113.03999999999999
>>> 
>>> 
>>> m= int(input("ENTER THE MASS OF AN OBJECT ="))
ENTER THE MASS OF AN OBJECT =
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    m= int(input("ENTER THE MASS OF AN OBJECT ="))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> 
>>>  m= int(input("ENTER THE MASS OF AN OBJECT ="))
 
SyntaxError: unexpected indent
>>> 
>>> m= int(input("ENTER THE MASS OF AN OBJECT ="))
ENTER THE MASS OF AN OBJECT = 12 KG
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    m= int(input("ENTER THE MASS OF AN OBJECT ="))
ValueError: invalid literal for int() with base 10: ' 12 KG'
>>> m=int(input("ENTER THE MASS OF AN OBJECT ="))
ENTER THE MASS OF AN OBJECT = 15
>>> #MASS IN KG
>>> #GIVEN THAT THE VALUE OF G=9.8 m/s
>>> #GIVEN THAT THE VALUE OF G=9.8 m/s
>>> force= m* 9.8
>>> print("GRAVITATIONAL FORCE OF AN OBJECT HAVING MASS OF 15kg =",force)
GRAVITATIONAL FORCE OF AN OBJECT HAVING MASS OF 15kg = 147.0
>>> 
>>> 
>>> c=int(input("ENTER THE TEMPERATURE IN CELSIUS ="))
ENTER THE TEMPERATURE IN CELSIUS = 25
>>> F=(c*9/5)+32
>>> PRINT("TEMPERATURE IN FAHRENHEIT =",F)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    PRINT("TEMPERATURE IN FAHRENHEIT =",F)
NameError: name 'PRINT' is not defined
>>> print("TEMPERATURE IN FAHRENHEIT =",F)
TEMPERATURE IN FAHRENHEIT = 77.0
>>> 
>>> 
>>> 
>>> P=int(Input("ENTER THE PRINCIPAL VALUE ="))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    P=int(Input("ENTER THE PRINCIPAL VALUE ="))
NameError: name 'Input' is not defined
>>> 
>>> 
>>> 
>>> 
>>> P=int(input("ENTER THE PRINCIPAL VALUE ="))
ENTER THE PRINCIPAL VALUE = 100000
>>> R=int(input("ENTER THE RATE AT WHICH PRINCIPAL IS TAKEN ="))
ENTER THE RATE AT WHICH PRINCIPAL IS TAKEN = 10
>>> T=int(input("ENTER THE TIME PERIOD FOR WHICH THE AMOUNT IS PAID BACK ="))
ENTER THE TIME PERIOD FOR WHICH THE AMOUNT IS PAID BACK = 5
>>> S.I. = (P*R*T)/100
SyntaxError: invalid syntax
>>> S.I.=(P*R*T)/100
SyntaxError: invalid syntax
>>> S.I=(P*R*T)/100
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    S.I=(P*R*T)/100
NameError: name 'S' is not defined
>>> SI=(P*R*T)/100
>>> print("INTEREST TO BE PAID FOR THE AMOUNT OF 100000 FOR THE TIME PERIOD OF 5 YEARS AT RATE OF 10% PER ANNUM =",SI)
INTEREST TO BE PAID FOR THE AMOUNT OF 100000 FOR THE TIME PERIOD OF 5 YEARS AT RATE OF 10% PER ANNUM = 50000.0
>>> 