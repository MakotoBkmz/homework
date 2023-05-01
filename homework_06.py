from decimal import Decimal
import math

radius = float(input('Input radius here >>> '))
sphere_volume = (4/3)*math.pi*radius**3

result = Decimal(str(sphere_volume)).quantize(Decimal('0.01'))
print(result)
