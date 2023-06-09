# Generated by Django 2.2.4 on 2023-04-05 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20230405_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothorder',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothorder',
            name='cloth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothorders', to='app1.Cloth'),
        ),
    ]
