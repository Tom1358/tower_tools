# Generated by Django 3.2 on 2022-01-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name_plural': 'Feedback'},
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='product',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user_profile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
