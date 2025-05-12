from datetime import datetime

now = datetime.now()
date = now.strftime('%d %B %Y')
print(f'{date} года') 