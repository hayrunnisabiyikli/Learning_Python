MASS_MULTIPLIER = 9.8
TOO_HEAVY = 500.0
TOO_LIGHT = 100.0

weight = 0.0
mass = 0.0

mass  = float(input("enter the object's mass in kilograms: "))

weight = mass * MASS_MULTIPLIER
print("object weight: ", format(weight, ".2f"))
if weight > TOO_HEAVY:
    print("The object is too heavy. It' weight more than", TOO_HEAVY, "Newtons")
elif weight < TOO_LIGHT:
    print("The object is too light. It's weight less than", TOO_LIGHT, "Newtons")