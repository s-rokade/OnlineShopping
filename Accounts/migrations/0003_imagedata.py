# Generated by Django 3.0.7 on 2020-09-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_placeorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgname', models.CharField(max_length=30)),
                ('img', models.ImageField(default='', upload_to='imges')),
            ],
        ),
    ]