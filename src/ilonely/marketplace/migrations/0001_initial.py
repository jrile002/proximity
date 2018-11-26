# Generated by Django 2.1.2 on 2018-11-24 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.PositiveIntegerField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('photo', models.ImageField(null=True, upload_to='product_pictures/')),
                ('location', models.CharField(blank=True, default='', max_length=150)),
                ('sold', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.Product'),
        ),
    ]
