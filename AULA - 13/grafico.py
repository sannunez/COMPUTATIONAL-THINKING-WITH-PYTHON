import matplotlib.pyplot as plt
import usandoPackages as formula

x = []
for i in range(101):
    x.append(i*6/100)
print(x)

yy = []
for i in x:
    yy.append(formula.y(i))
print(yy)

x = [0,1,2,3,3.5,5,6]
y = [0,1,2,2,2,3,6**2-10*]

plt.plot(x, yy, )