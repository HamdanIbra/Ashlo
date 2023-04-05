# Generated by Django 2.2.4 on 2023-04-05 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230404_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothorder',
            fields=[
                ('cloth', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app1.Cloth')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clothorders', to='app1.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='ordercloth',
            name='cloth',
        ),
        migrations.RemoveField(
            model_name='ordercloth',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderCloth',
        ),
    ]
