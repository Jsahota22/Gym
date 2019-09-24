from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
      migrations.CreateModel(
        name='Reviews',
        fields=[
           ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
           ('name', models.CharField(max_length=100)),
           ('body', models.TextField()),
           ('date', models.DateTimeField(auto_now_add=True)),
          ],
        ),
      ]