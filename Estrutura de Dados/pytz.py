import pytz
from datetime import datetime

# Criando datetime com timezone
data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)