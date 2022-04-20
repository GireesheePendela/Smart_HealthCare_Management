

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('department', models.CharField(max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=50)),
                ('doctorID', models.CharField(max_length=50, unique=True)),
                ('education_college', models.CharField(max_length=100)),
                ('education_degree', models.CharField(max_length=100)),
                ('education_year', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
