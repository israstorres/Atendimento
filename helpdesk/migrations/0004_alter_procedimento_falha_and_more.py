# Generated by Django 4.0.4 on 2022-05-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_procedimento_falha_procedimento_sucesso_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedimento',
            name='falha',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='passo_a_passo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='sucesso',
            field=models.TextField(blank=True, null=True),
        ),
    ]
