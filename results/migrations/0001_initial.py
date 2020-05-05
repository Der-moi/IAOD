# Generated by Django 2.0.4 on 2020-05-05 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agamp4',
            fields=[
                ('short_seq', models.CharField(blank=True, max_length=42, null=True)),
                ('tax_name', models.CharField(blank=True, max_length=30, null=True)),
                ('com_name', models.CharField(blank=True, max_length=20, null=True)),
                ('genome', models.CharField(blank=True, max_length=15, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('intron_class', models.CharField(blank=True, max_length=20, null=True)),
                ('intron_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('chromosome', models.CharField(blank=True, max_length=20, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('stop', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('strand', models.CharField(blank=True, max_length=1, null=True)),
                ('intron_rank', models.IntegerField(blank=True, null=True)),
                ('phase', models.IntegerField(blank=True, null=True)),
                ('tds', models.CharField(blank=True, max_length=4, null=True)),
                ('up_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('branch_seq', models.CharField(blank=True, max_length=50, null=True)),
                ('down_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('full_seq', models.TextField(blank=True, null=True)),
                ('gene_symbol', models.TextField(blank=True, null=True)),
                ('gene_id', models.CharField(blank=True, max_length=30, null=True)),
                ('trans_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'AgamP4',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grch38',
            fields=[
                ('short_seq', models.CharField(blank=True, max_length=42, null=True)),
                ('tax_name', models.CharField(blank=True, max_length=30, null=True)),
                ('com_name', models.CharField(blank=True, max_length=20, null=True)),
                ('genome', models.CharField(blank=True, max_length=15, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('intron_class', models.CharField(blank=True, max_length=20, null=True)),
                ('intron_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('chromosome', models.CharField(blank=True, max_length=20, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('stop', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('strand', models.CharField(blank=True, max_length=1, null=True)),
                ('intron_rank', models.IntegerField(blank=True, null=True)),
                ('phase', models.IntegerField(blank=True, null=True)),
                ('tds', models.CharField(blank=True, max_length=4, null=True)),
                ('up_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('branch_seq', models.CharField(blank=True, max_length=50, null=True)),
                ('down_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('full_seq', models.TextField(blank=True, null=True)),
                ('gene_symbol', models.TextField(blank=True, null=True)),
                ('gene_id', models.CharField(blank=True, max_length=30, null=True)),
                ('trans_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'GRCh38',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orthologs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orthologs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tair10',
            fields=[
                ('short_seq', models.CharField(blank=True, max_length=42, null=True)),
                ('tax_name', models.CharField(blank=True, max_length=30, null=True)),
                ('com_name', models.CharField(blank=True, max_length=20, null=True)),
                ('genome', models.CharField(blank=True, max_length=15, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('intron_class', models.CharField(blank=True, max_length=20, null=True)),
                ('intron_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('chromosome', models.CharField(blank=True, max_length=20, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('stop', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('strand', models.CharField(blank=True, max_length=1, null=True)),
                ('intron_rank', models.IntegerField(blank=True, null=True)),
                ('phase', models.IntegerField(blank=True, null=True)),
                ('tds', models.CharField(blank=True, max_length=4, null=True)),
                ('up_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('branch_seq', models.CharField(blank=True, max_length=50, null=True)),
                ('down_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('full_seq', models.TextField(blank=True, null=True)),
                ('gene_symbol', models.TextField(blank=True, null=True)),
                ('gene_id', models.CharField(blank=True, max_length=30, null=True)),
                ('trans_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'TAIR10',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='U12S',
            fields=[
                ('short_seq', models.CharField(blank=True, max_length=42, null=True)),
                ('tax_name', models.CharField(blank=True, max_length=30, null=True)),
                ('com_name', models.CharField(blank=True, max_length=20, null=True)),
                ('genome', models.CharField(blank=True, max_length=15, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
                ('intron_class', models.CharField(blank=True, max_length=20, null=True)),
                ('intron_id', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('chromosome', models.CharField(blank=True, max_length=20, null=True)),
                ('start', models.IntegerField(blank=True, null=True)),
                ('stop', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('strand', models.CharField(blank=True, max_length=1, null=True)),
                ('intron_rank', models.IntegerField(blank=True, null=True)),
                ('phase', models.IntegerField(blank=True, null=True)),
                ('tds', models.CharField(blank=True, max_length=4, null=True)),
                ('up_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('branch_seq', models.CharField(blank=True, max_length=50, null=True)),
                ('down_seq', models.CharField(blank=True, max_length=80, null=True)),
                ('full_seq', models.TextField(blank=True, null=True)),
                ('gene_symbol', models.TextField(blank=True, null=True)),
                ('gene_id', models.CharField(blank=True, max_length=30, null=True)),
                ('trans_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'u12s',
                'managed': False,
            },
        ),
    ]
