mdv = input("Choose one to calculate(mass, density, volume): ")

if mdv == 'mass':
    d = float(input("Density: "))
    v = float(input("Volume: "))
    result = d * v #This is for mass
elif mdv == 'density':
    m = float(input("Mass: "))
    v = float(input("Volume: "))
    result = m / v #This is for density
elif mdv == 'volume':
    m = float(input("Mass: "))
    d = float(input("Density: "))
    result = m / d

print("%.2f" % result)