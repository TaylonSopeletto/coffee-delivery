# Generated by Django 4.0.6 on 2022-07-17 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_coffee_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='categories',
            field=models.ManyToManyField(to='store.category'),
        ),
    ]