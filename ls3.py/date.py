from datetime import datetime, timedelta
import locale
locale.setlocale(locale.LC_TIME, "ru_RU.utf8")

now = datetime.now()
one_week_ago = now - timedelta(days=7)
one_monte_ago = now - timedelta(days=31)


print('Сегодня -', now.strftime("%d %B %Y (%A)"))
print('Неделя назад -', one_week_ago.strftime("%d %B %Y (%A)"))
print('Месяц назад -', one_monte_ago.strftime("%d %B %Y (%A)"))
