
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pregnancies', models.IntegerField()),
                ('Glucose', models.IntegerField()),
                ('BloodPressure', models.IntegerField()),
                ('SkinThickness', models.IntegerField()),
                ('Insulin', models.IntegerField()),
                ('BMI', models.IntegerField()),
                ('DiabetesPedigreeFunction', models.IntegerField()),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=200)),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('restecg', models.IntegerField()),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('slope', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ImageBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageblock', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('address', models.CharField(max_length=40)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=20)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WhoPredictDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_disease', models.CharField(max_length=30)),
                ('predict_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.Profile'),
        ),
    ]
