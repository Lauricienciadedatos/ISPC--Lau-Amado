# Determinar según el género, la mesa de votación asignada
genero = input("Ingrese el género al que pertenece: 'f' (femenino) o 'm' (masculino)")
if genero == 'f' :
    print("Será asignada a la mesa de votación femenina")
elif genero == 'm' :
    print("Será asignado a la mesa de votación masculina")
else:
    print("Por favor ingresar solo 'f' o 'm', vuelva a intentar")