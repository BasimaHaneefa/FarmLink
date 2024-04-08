# Generated by Django 4.2.7 on 2024-04-03 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FarmerApp', '0001_initial'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.CharField(default=0, max_length=10)),
                ('booking_totalamount', models.CharField(default=0, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=300)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(default=0, max_length=10)),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_content', models.CharField(max_length=300)),
                ('complaint_reply', models.CharField(default='Not replied', max_length=100)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.CharField(max_length=50)),
                ('cart_status', models.CharField(default=0, max_length=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FarmerApp.tbl_product')),
            ],
        ),
    ]
