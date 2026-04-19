import datetime
from datetime import datetime

date_string = "1956-10-12"
date_object = datetime.strptime(date_string, "%Y-%m-%d").date()

print(date_object)