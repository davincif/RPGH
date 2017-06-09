from RPGSystems.Enums.race import Race
from RPGSystems.Enums.classes import Classes

for i in Race:
	print(i.describe(), i.get_uprace())
print("\n")
for i in Classes:
	print(i.describe())
