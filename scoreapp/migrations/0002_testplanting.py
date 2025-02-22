# Generated by Django 5.1.4 on 2025-01-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestPlanting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Region', models.CharField(choices=[('Mau', 'Mau'), ('Aberdare', 'Aberdare'), ('Mt. Kenya', 'Mt. Kenya'), ('Cherangany hills', 'Cherangany hills'), ('Mt. Elgon', 'Mt. Elgon')], default='Unknown', max_length=50)),
                ('County', models.CharField(choices=[('Kiambu', 'Kiambu'), ("Murang'a", "Murang'a"), ('Nyeri', 'Nyeri'), ('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Bomet', 'Bomet'), ('Kericho', 'Kericho'), ('Trans-Nzoia', 'Trans-Nzoia'), ('Bungoma', 'Bungoma'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Homa Bay', 'Homa Bay'), ('Kisii', 'Kisii'), ('Migori', 'Migori'), ('Meru', 'Meru'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera')], max_length=50)),
                ('Date_collected', models.DateField()),
                ('Trees_planted', models.IntegerField()),
            ],
        ),
    ]
