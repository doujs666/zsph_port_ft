# Generated by Django 2.1.7 on 2019-08-27 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='db_assert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assert_input', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('select_assert', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('assert_type', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('assert_input1', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='host_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('host', models.GenericIPAddressField()),
                ('port', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='mongodb_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('host', models.CharField(max_length=50)),
                ('port', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='page_base_mysql',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('host', models.CharField(max_length=50)),
                ('port', models.CharField(max_length=20)),
                ('user', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='port_manage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=20)),
                ('port_name', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=100)),
                ('request_raw', models.CharField(max_length=10)),
                ('key', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Precondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_status', models.CharField(blank=True, default=None, max_length=5, null=True)),
                ('mobile', models.CharField(blank=True, default=None, max_length=11, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=6, null=True)),
                ('project_url', models.CharField(max_length=100)),
                ('select_port', models.CharField(max_length=20)),
                ('port_url', models.CharField(max_length=50)),
                ('key', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('value', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='project_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('versions', models.CharField(max_length=10)),
                ('update_time', models.DateField(verbose_name='events time')),
                ('port_count', models.IntegerField()),
                ('create_time', models.DateField(auto_now=True)),
                ('host', models.CharField(max_length=30)),
                ('sql_address', models.CharField(max_length=10)),
                ('mongodb_address', models.CharField(max_length=10)),
                ('explain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='test_case',
            fields=[
                ('id', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('test_case_name', models.CharField(max_length=15)),
                ('login_status', models.CharField(max_length=5)),
                ('mobile', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=6)),
                ('project_id', models.CharField(max_length=100)),
                ('select_port', models.CharField(max_length=20)),
                ('port_url', models.CharField(max_length=50)),
                ('key', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('value', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='precondition',
            name='test_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.test_case'),
        ),
        migrations.AddField(
            model_name='port_manage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.project_message'),
        ),
        migrations.AddField(
            model_name='db_assert',
            name='test_case',
            field=models.ForeignKey(max_length=36, on_delete=django.db.models.deletion.CASCADE, to='sign.test_case'),
        ),
    ]
