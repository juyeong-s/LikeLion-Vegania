# Generated by Django 3.2.4 on 2021-07-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_auto_20210703_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='f1',
            field=models.TextField(default='샐러드'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='f2',
            field=models.TextField(default='건강식'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='f3',
            field=models.TextField(default='계란'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='f4',
            field=models.TextField(default='바지락'),
        ),
        migrations.AlterField(
            model_name='product',
            name='f1',
            field=models.TextField(default='샐러드'),
        ),
        migrations.AlterField(
            model_name='product',
            name='f2',
            field=models.TextField(default='프로틴'),
        ),
        migrations.AlterField(
            model_name='product',
            name='f3',
            field=models.TextField(default='찌개'),
        ),
        migrations.AlterField(
            model_name='product',
            name='f4',
            field=models.TextField(default='저칼로리'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='f1',
            field=models.TextField(default='단백질'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='f2',
            field=models.TextField(default='탄수화물'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='f3',
            field=models.TextField(default='반찬가게'),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='f4',
            field=models.TextField(default='다이어트 식단'),
        ),
        migrations.AlterField(
            model_name='vegan',
            name='f1',
            field=models.TextField(default='밀가루'),
        ),
        migrations.AlterField(
            model_name='vegan',
            name='f2',
            field=models.TextField(default='돼지고기'),
        ),
        migrations.AlterField(
            model_name='vegan',
            name='f3',
            field=models.TextField(default='닭가슴살'),
        ),
        migrations.AlterField(
            model_name='vegan',
            name='f4',
            field=models.TextField(default='채소'),
        ),
    ]
