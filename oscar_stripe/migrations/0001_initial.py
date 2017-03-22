# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-20 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StripeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_request', models.TextField(help_text='The raw request', max_length=750, verbose_name='Raw Request')),
                ('raw_response', models.TextField(help_text='The raw response', max_length=750, verbose_name='Raw Response')),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='The DateTime when request was made.', verbose_name='Date Created')),
                ('description', models.CharField(help_text='Description of the transaction', max_length=128, verbose_name='Description of the Transaction')),
                ('transaction_type', models.CharField(help_text='The type of transaction', max_length=12, verbose_name='Transaction Type')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, help_text='Amount', max_digits=12, null=True)),
                ('currency', models.CharField(help_text='currency', max_length=3, verbose_name='Currency')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Transaction Date')),
            ],
            options={
                'verbose_name_plural': 'Stripe Transactions',
                'abstract': False,
                'ordering': ('-date_created',),
                'verbose_name': 'Stripe Transaction',
            },
        ),
    ]