# Generated by Django 3.0.4 on 2020-03-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0002_auto_20200313_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristattraction',
            name='kindOf',
            field=models.CharField(choices=[('วัด', 'วัด'), ('ทะเลและชายหาด', 'ทะเลและชายหาด'), ('โครงการหลวงและโครงการในพระราชดำริ', 'โครงการหลวงและโครงการในพระราชดำริ'), ('น้ำตก', 'น้ำตก'), ('สันทนาการและกีฬา', 'สันทนาการและกีฬา'), ('ธรรมชาติและสัตว์ป่า', 'ธรรมชาติและสัตว์ป่า'), ('ศิลปะ วัฒนธรรม แหล่งมรดก และสถาปัตยกรรม', 'ศิลปะ วัฒนธรรม แหล่งมรดก และสถาปัตยกรรม'), ('สถานที่เกี่ยวกับศาสนาอื่นๆ', 'สถานที่เกี่ยวกับศาสนาอื่นๆ'), ('พิพิธภัณฑ์', 'พิพิธภัณฑ์'), ('อื่นๆ', 'อื่นๆ')], default='อื่นๆ', max_length=100),
        ),
        migrations.AlterField(
            model_name='touristattraction',
            name='province',
            field=models.CharField(choices=[('เชียงใหม่', 'เชียงใหม่'), ('กรุงเทพ', 'กรุงเทพ')], default='กรุงเทพ', max_length=50),
        ),
    ]
