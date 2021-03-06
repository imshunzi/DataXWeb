# Generated by Django 2.2.7 on 2019-11-27 13:28

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataXConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('site_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='站点名称')),
                ('site_desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='站点描述')),
                ('site_author', models.CharField(blank=True, max_length=100, null=True, verbose_name='作者')),
                ('site_company', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='公司')),
                ('address', models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='显示地址')),
                ('telephone', models.CharField(max_length=15, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('icp', models.CharField(blank=True, max_length=256, null=True, verbose_name='备案号')),
                ('remark', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='sys/%Y/%m', verbose_name='二维码')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '站点配置',
                'verbose_name_plural': '站点配置',
                'db_table': 'dx_config',
            },
        ),
        migrations.CreateModel(
            name='DataXJobScheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('name', models.CharField(max_length=200, verbose_name='作业名称')),
                ('sort', models.IntegerField(default=10000, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '作业调度',
                'verbose_name_plural': '作业调度',
                'db_table': 'dx_jobscheduler',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='DataXTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('name', models.CharField(max_length=256, verbose_name='任务名称')),
                ('from_dbtype', models.CharField(max_length=50, verbose_name='来源库类型')),
                ('from_hostname', models.CharField(max_length=16, verbose_name='来源IP')),
                ('from_port', models.SmallIntegerField(default=3306, verbose_name='来源端口')),
                ('from_username', models.CharField(max_length=50, verbose_name='来源用户名')),
                ('from_password', models.CharField(max_length=50, verbose_name='来源密码')),
                ('from_db_name', models.CharField(max_length=80, verbose_name='来源库名')),
                ('from_table_name', models.CharField(max_length=80, verbose_name='来源表名')),
                ('from_columns', models.CharField(default='*', max_length=1000, verbose_name='来源列')),
                ('from_where', models.CharField(default='', max_length=1000, verbose_name='来源条件')),
                ('from_character', models.CharField(default='utf8', max_length=10, verbose_name='来源编码')),
                ('to_dbtype', models.CharField(max_length=50, verbose_name='目标库类型')),
                ('to_hostname', models.CharField(max_length=16, verbose_name='目标IP')),
                ('to_port', models.SmallIntegerField(default=3306, verbose_name='目标端口')),
                ('to_username', models.CharField(max_length=50, verbose_name='目标用户名')),
                ('to_password', models.CharField(max_length=50, verbose_name='目标密码')),
                ('to_db_name', models.CharField(max_length=80, verbose_name='目标库名')),
                ('to_table_name', models.CharField(max_length=80, verbose_name='目标表名')),
                ('to_columns', models.CharField(default='*', max_length=1000, verbose_name='目标列')),
                ('to_pre_sql', models.CharField(default='', max_length=1000, verbose_name='前置条件')),
                ('to_post_sql', models.CharField(default='', max_length=1000, verbose_name='后置条件')),
                ('to_character', models.CharField(default='utf8', max_length=10, verbose_name='目标编码')),
                ('to_session', models.CharField(default='', max_length=256, verbose_name='目标session')),
                ('to_write_mode', models.CharField(default='insert', max_length=15, verbose_name='目标写入模式')),
                ('task_speed_channel', models.SmallIntegerField(default=5, verbose_name='速度')),
                ('task_error_limit_record', models.SmallIntegerField(default=5, verbose_name='错误记录条数')),
                ('task_error_limit_percentage', models.FloatField(default=0.02, verbose_name='错误记录百分比')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '作业任务',
                'verbose_name_plural': '作业任务',
                'db_table': 'dx_task',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='DataXNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operate_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='操作人名称')),
                ('operate_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='操作人ID')),
                ('create_username', models.CharField(auto_created=True, default='admin', max_length=30, verbose_name='创建人名称')),
                ('create_uid', models.IntegerField(auto_created=True, default=123456789, verbose_name='创建人ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('operate_time', models.DateTimeField(auto_now=True, verbose_name='操作时间')),
                ('code', models.CharField(max_length=20, verbose_name='标识')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='名称')),
                ('url', models.CharField(max_length=200, verbose_name='链接')),
                ('remark', models.CharField(blank=True, max_length=300, verbose_name='描述')),
                ('is_root', models.BooleanField(default=True, verbose_name='是否一级菜单')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否启用')),
                ('parent', models.ForeignKey(blank=True, default=0, limit_choices_to={'is_delete': False, 'is_root': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='backend.DataXNav', verbose_name='父级')),
            ],
            options={
                'verbose_name': '导航菜单管理',
                'verbose_name_plural': '导航菜单管理',
                'db_table': 'dx_nav',
                'ordering': ['sort', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='DataXUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default='avatar/default.png', max_length=200, upload_to='avatar/%Y/%m', verbose_name='用户头像')),
                ('qq', models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('nick_name', models.CharField(max_length=30, verbose_name='昵称')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'dx_userprofile',
                'ordering': ['-id'],
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
