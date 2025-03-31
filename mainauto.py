from auto_aeromexico import aeromexico
import pandas as pd

def get_reservas ():
    data_facturacion = pd.read_csv("files/reservas.csv")
    data_facturacion.head()
    clean_data = data_facturacion["reserva"]
    reserva = clean_data.dropna()

    reservas = []

    for i in reserva:
        reservas.append(i)

    return reservas

for reserva in get_reservas ():
    aeromexico(reserva)
    
get_reservas()