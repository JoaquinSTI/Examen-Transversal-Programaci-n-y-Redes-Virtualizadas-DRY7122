def determinar_rango_vlan(vlan):
	if 1 <= vlan <= 1005:
		return "VLAN de rango normal"
	elif 1006 <= vlan <= 4094:
		return "VLAN de rango extendido"
	else:
		return "Numero de Vlan fuera de rango"

try:
	vlan = int(input("Introduce el numero de Vlan:  "))
	print(determinar_rango_vlan(vlan))
except ValueError:
	print("Por favor, elige un numero entero")
