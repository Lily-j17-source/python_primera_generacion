# Generated by Django 3.1.7 on 2021-03-27 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=50)),
                ('zip_code', models.TextField(max_length=10)),
                ('address', models.TextField(max_length=1000, unique=True)),
                ('longitude', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='petdate',
            name='branch_office',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='dates', to='vet.branchoffice'),
        ),
    ]
