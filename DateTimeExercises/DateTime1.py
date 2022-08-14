"""
Print current date and time in Python
"""
from datetime import datetime
hoy = datetime.today().strftime('%m/%d/%y')
print(hoy)

