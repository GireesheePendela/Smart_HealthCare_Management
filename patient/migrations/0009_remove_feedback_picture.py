
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20210714_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='picture',
        ),
    ]
