# Generated by Django 3.1.3 on 2020-12-18 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pdapi', '0002_auto_20201218_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='User',
            new_name='user',
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('commoninfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pdapi.commoninfo')),
                ('regNum', models.CharField(max_length=15)),
                ('officePhone', models.IntegerField()),
                ('speciality', models.CharField(choices=[('GP', 'General practitioner'), ('OB/GYN', 'Obstetrician and Gynaecologist'), ('PSY', 'Psychiatrist'), ('DN', 'Dentist'), ('GS', 'General surgeon'), ('DM', 'Dermatologist')], max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('pdapi.commoninfo',),
        ),
    ]
