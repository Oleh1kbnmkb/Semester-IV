from tortoise import Tortoise, fields, run_async
from tortoise.models import Model

# Define your model
class LastNews(Model):
    title = fields.TextField()
    time = fields.CharField(255, null=False)

# Tortoise ORM initialization and data insertion function
async def init():
    await Tortoise.init(
        db_url="sqlite://news.db",
        modules={"models": ["__main__"]}  # Replace '__main__' with your module name if different
    )
    await Tortoise.generate_schemas()

    # Insert data
    news_data = [
        ('Данія оголосила про оборонний пакет для України на понад €100 млн', '2024-08-19 15:38'),
        ('AFP: проросійські новинні сайти ширили фейк, що замах на Трампа організував Обама', '2024-08-19 15:32'),
        ('Премʼєр Китаю поїде в росію та Білорусь. Для чого?', '2024-08-19 15:16'),
        ('В Індії тривають масові протести через зґвалтування та вбивство лікарки на роботі', '2024-08-19 15:02'),
        ('Продовжила рятувати навіть після смерті: у Львові трансплант-координаторка стала доноркою органів', '2024-08-19 14:52'),
        ('У США заперечили, що блокують дозвіл на удари ракетами Storm Shadow по території рф', '2024-08-19 14:43'),
        ('Все буде UA!: «Укрпошта» випустила марку до Дня Незалежності', '2024-08-19 14:11'),
        ('Легалізацію медичного канабісу схвалюють понад 40% українців: найбільше — люди віком 50-60 років', '2024-08-19 14:09'),
        ('Німеччина надає Україні новий пакет військової допомоги: у ньому — IRIS-T, артснаряди та дрони', '2024-08-19 13:35'),
        ('Рівень енергоспоживання вже зріс на тлі спеки. Електрику імпортують із 5 країн — «Укренерго»', '2024-08-19 13:35')
    ]

    for title, time in news_data:
        await LastNews.create(title=title, time=time)

    await Tortoise.close_connections()

if __name__ == "__main__":
    run_async(init())
