# Generated by Django 5.0.4 on 2024-05-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='last_name',
            new_name='password',
        ),
        migrations.AddField(
            model_name='teacher',
            name='additional_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='contact_number',
            field=models.CharField(default='No contact number provided', max_length=20),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='qualifications',
            field=models.TextField(default='No adderss provided'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects_teaching',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='years_of_experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='No address provided', max_length=254),
        ),
    ]