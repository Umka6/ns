# Generated by Django 3.0 on 2020-09-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('mail', models.CharField(max_length=200, verbose_name='Почта')),
                ('comment', models.CharField(max_length=200, verbose_name='Коммент')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Заявка cо страницы контактов',
                'verbose_name_plural': 'Заявка со страницы контактов',
            },
        ),
    ]
