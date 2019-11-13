import math

m1=float(input("Mass 1 (must be <= 1): "))
m2=float(input("Mass 2 (must be <= 1): "))
r1= float(input("Radius 1 (must be <= 1): "))
r2= float(input("Radius 2 (must be <= 1): "))
b=float(input("Impact parameter b: Must be <=1: "))

x1, v1 = [-10, b], [1, 0]
x2, v2 = [0, 0], [0, 0]

#Adds values from two lists
#[x + y for x, y in zip(first, second)]

def detection():
    distSq = (x1[0]-x2[0])*(x1[0]-x2[0])+((x1[1]-x2[1])*(x1[1]-x2[1]))
    radSumSq = (r1+r2) * (r1+r2)
    if (distSq == radSumSq) or distSq<radSumSq:
        return True
    else:
        return False



def time_of_collision():
    a = (v2[0]-v1[0])**2+(v2[1]-v1[1])**2
    b = 2*((x2[0]-x1[0])*(v2[0]-v1[0])+(x2[1]-x1[1])*(v2[1]-v1[1]))
    c = ((x2[0]-x1[0])**2)+((x2[1]-x1[1])**2)-((r1+r2)**2)
    d = b**2-4*a*c
    t=0

    if d<0:
        print("No collision")
    elif d == 0:
        t = (-b)/2*a
        print("The quadratic equation has one solutions: ", t)
    else:
        t1 = (-b+math.sqrt(d))/2*a
        t2 = (-b-math.sqrt(d))/2*a
        if t1<0 and t2<0:
            print("The particles do not collide")
        if abs(t1)>abs(t2) and t1>0:
            t = t1
        elif abs(t2)>abs(t1) and t2>0:
            t= t2
        if t1>0 and t2>0:
            t=min(t1,t2)
    return t


time = round(time_of_collision(), 2)
print("\nThe circles collide at time:", (time))

#[x + y for x, y in zip(first, second)]

while True:
    if detection() == True:
        angle = math.degrees(math.tan(b/(v1[0]**2+v1[1]**2)**(1/2)))
        print("Detection occured when the centers of the circles are at:", x1, "and", x2, "with an angle of", round(angle, 2), "degrees between the x and y components of mass 1's velocity vector")
        vf1=[v1[0]*-1,b]
        vf2=[v1[0],-1*b]
        x1=[round(x+(y*time), 2) for x, y in zip(x1, vf1)]
        x2=[round(x+(y*time), 2) for x, y in zip(x2, vf2)]

        print("position of mass 1's center after collision time has doubled from t = 0:", time, ":", x1)
        print("position of mass 2's center after collision time has doubled from t = 0:", time, ":", x2)
        break
    else:
        x1[0]+=v1[0]
        x1[1]+=v1[1]

