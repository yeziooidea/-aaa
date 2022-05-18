# Generated by Django 4.0.3 on 2022-04-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='姓名')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('dongjie', models.IntegerField()),
                ('email', models.CharField(max_length=25, verbose_name='邮箱')),
                ('tel', models.CharField(max_length=25, verbose_name='联系电话')),
                ('dizhi', models.CharField(max_length=100, verbose_name='地址')),
                ('youbian', models.CharField(max_length=25, verbose_name='邮编')),
                ('truename', models.CharField(max_length=25, verbose_name='真实姓名')),
                ('regtime', models.CharField(max_length=25)),
                ('lastlogintime', models.CharField(max_length=25)),
                ('logincishu', models.IntegerField(verbose_name=4)),
            ],
        ),
    ]