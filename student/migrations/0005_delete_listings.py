# Generated by Django 4.1.7 on 2023-04-04 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_address_alter_student_birthday_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Listings',
        ),
    ]
