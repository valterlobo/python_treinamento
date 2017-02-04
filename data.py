
from datetime import datetime

now = datetime.now()

#data dd/mm/aaaa
print ('data : {dia}/{mes}/{ano} - {hora}:{minuto}'.format(ano=now.year, mes=now.month, dia=now.day, hora=now.hour, minuto=now.minute,) )