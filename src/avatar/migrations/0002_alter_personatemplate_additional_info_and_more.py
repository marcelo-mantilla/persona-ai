# Generated by Django 4.2.8 on 2023-12-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personatemplate',
            name='additional_info',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='audience',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='career',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='hobbies',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='personality',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='purpose',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='summary',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='tone',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='values',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='personatemplate',
            name='vision',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
