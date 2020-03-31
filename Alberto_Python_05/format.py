phrase = "His name is {0}!".format("Arthur") #format permette di creare dei "segnaposto" da poter riempire all'occorrenza con delle parole
print(phrase)

name = "Alice"
age = 10
phrase = "I am {1} and I am {0} years old.".format(age, name)
print(phrase)
phrase = "I am {0} and I am {1} years old.".format(age, name)
print(phrase)

x = 4
y = 5
phrase = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, x, y, x * y)
print(phrase)

name1 = "Paris"
name2 = "Whitney"
name3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.1415926))
print("123456789 123456789 123456789 123456789 123456789 123456789")
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||".format(name1,name2,name3,1981))
print("The decimal value {0} converts to hex value {0:x}".format(123456))

letter = """
Dear {0} {2}.
{0}, I have an interesting money-making proposition for you!
If you deposit $10 million into my bank account, I can
double your money ...
"""

print(letter.format("Paris", "Whitney", "Hilton"))
print(letter.format("Bill", "Henry", "Gates"))