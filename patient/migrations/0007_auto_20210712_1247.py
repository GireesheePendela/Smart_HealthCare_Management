
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20210712_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
