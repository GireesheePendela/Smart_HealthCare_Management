
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_auto_20210712_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
