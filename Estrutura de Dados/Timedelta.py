from datetime import date, time, datetime, timedelta

tipo_carro = 'G' # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"Chegada: {data_atual}. Pronto às {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"Chegada: {data_atual}. Pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"Chegada: {data_atual}. Pronto às {data_estimada}")

print(date.today() - timedelta(days=1))

# Caso seja necessário manipular apenas HORA, é preciso construir uma Data junto, manipulando e extraindo apenas a Hora.
resultado = datetime(2024, 9, 17, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

# Extraindo apenas a Data atual de um Datetime.
print(datetime.now().date())