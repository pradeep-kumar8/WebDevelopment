# Generated by Django 4.2.1 on 2023-05-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_ctu_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=13)),
                ('Textarea', models.TextField(max_length=500)),
            ],
        ),
    ]
