
"""
Created on January 2020 for Python 2.7
Should work also for Python 3, maybe not the last line
@author: carlopasquinucci : carlo.a.pasquinucci (at) gmail.com
"""

print("\n")
print("#########################################################")
print("######                                            #######")
print("######      Calculus of k epsilon omega           #######")
print("######                                            #######")
print("#########################################################")
print("\n")

Velocity = float(input("- Velocity [m/s]: "))
TurbuLevel = float(input("- Turbulence Level: "))
TurbuLength = float(input("- Turbulent Length Scale [m]: "))


k=(3/2)**(1/2)*(Velocity*TurbuLevel*TurbuLength)
epsilon=3/2*(Velocity*TurbuLevel)**2
omega=epsilon**(1/2)*TurbuLength 

print("\n")
print("#########################################################")
print("######                                            #######")
print("######                 Results                    #######")
print("######                                            #######")
print("#########################################################")
print("\n")

print("\n")
print("k [m^2/s^2]= "+str(k)+"\n")
print("epsilon [m^2/s^3]= "+str(epsilon)+"\n")
print("omega [1/s]= "+str(omega)+"\n")
print("\n")

a = raw_input("Press any key to close")
