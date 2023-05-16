# Generated by Django 4.2.1 on 2023-05-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide_image', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Слайды',
                'verbose_name_plural': 'Слайд',
            },
        ),
    ]