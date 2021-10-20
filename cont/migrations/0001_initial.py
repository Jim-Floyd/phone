# Generated by Django 3.2.8 on 2021-10-19 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=13)),
                ('type', models.CharField(choices=[('HOME', 'Home'), ('WORK', 'Work'), ('FAX', 'Fax'), ('OTHER', 'Other')], max_length=100)),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cont.contact')),
            ],
        ),
    ]
