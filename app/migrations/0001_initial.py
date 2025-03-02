# Generated by Django 5.1.6 on 2025-03-02 15:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.FileField(blank=True, null=True, upload_to='img/', verbose_name='Картинка')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, blank=True, null=True, verbose_name='Дата')),
                ('adres', models.CharField(max_length=1000, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('tel', models.CharField(max_length=15, verbose_name='Телефон')),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Итог')),
                ('zakaz', models.TextField(verbose_name='Заказ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.status')),
                ('tovars', models.ManyToManyField(to='app.tovar')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1, verbose_name='Количество')),
                ('summa', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Сумма')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tovar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tovar')),
            ],
        ),
    ]
