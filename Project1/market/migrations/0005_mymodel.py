# Generated by Django 5.0.3 on 2024-07-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_basket_session_key_alter_basket_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
