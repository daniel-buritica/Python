import time
#import datetime
from datetime import datetime
print(time.time()) #cantidad de segundos desde 1970 UTC

fecha = datetime(2023,1,1)
fecha2 = datetime(2023,2,2)

ahora = datetime.now()
print(ahora)
print(fecha)

#Crear fecha apartir de string

fechastr = datetime.strptime("2023-01-03","%Y-%m-%d")
print(fechastr)

print(fecha.strftime("%Y.%m.%d")) #volver una fecha un string

print(fecha > fecha2)
print(
    fecha.year,
    fecha.month,
    fecha.day
)
