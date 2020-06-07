# Generated by Django 3.0 on 2020-06-03 14:13

from django.conf import settings
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
            name='User',
            fields=[
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descriptions', models.TextField(blank=True, max_length=500, verbose_name='описание')),
                ('name', models.CharField(blank=True, max_length=60, verbose_name='имя')),
                ('secondName', models.CharField(blank=True, max_length=60, verbose_name='отчество')),
                ('lastName', models.CharField(blank=True, max_length=60, verbose_name='фамилия')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='должность')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='дата рождения')),
                ('phone', models.CharField(max_length=30, null=True, verbose_name='телефон')),
                ('user_role', models.CharField(choices=[('guest', 'Гость'), ('operator', 'Оператор'), ('admin', 'Администратор'), ('kladovschik', 'Кладовщик')], default='guest', max_length=20, verbose_name='Роль пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Наименование')),
                ('description', models.TextField(default=None, verbose_name='Описание')),
                ('address', models.TextField(db_index=True, default=None, verbose_name='Адрес')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('unp', models.BigIntegerField(verbose_name='УНП')),
                ('dischargePoint', models.TextField(db_index=True, null=True, verbose_name='пункт разгрузки')),
                ('payer', models.TextField(db_index=True, null=True, verbose_name='плательщик')),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Агент',
                'verbose_name_plural': 'Агенты',
            },
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(db_index=True, max_length=255, verbose_name='Номер')),
                ('driver', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Водитель')),
                ('number_pricep', models.CharField(db_index=True, max_length=255, null=True, verbose_name='номер прицепа')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('last_in', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего въезда')),
                ('last_out', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего выезда')),
                ('weghtIn', models.FloatField(db_index=True, null=True, verbose_name='вес пустой')),
                ('weghtOut', models.FloatField(db_index=True, null=True, verbose_name='вес полной')),
                ('netto', models.FloatField(db_index=True, null=True, verbose_name='вес clear')),
                ('status_in', models.BooleanField(default=False, verbose_name='На территории?')),
                ('description', models.TextField(db_index=True, null=True, verbose_name='описание')),
                ('numberPassport', models.CharField(db_index=True, max_length=255, null=True, verbose_name='номер сопрводительного пасопрта')),
                ('store', models.CharField(db_index=True, max_length=255, null=True, verbose_name='склад')),
                ('discont', models.FloatField(db_index=True, null=True, verbose_name='скидка')),
                ('organization', models.CharField(db_index=True, max_length=255, null=True, verbose_name='организация')),
                ('courseDate', models.DateField(blank=True, null=True, verbose_name='дата курса ')),
                ('nakladnayaDate', models.DateField(blank=True, null=True, verbose_name='дата накладной ')),
                ('operatrion', models.IntegerField(null=True, verbose_name='operartion')),
                ('executer', models.CharField(db_index=True, max_length=255, null=True, verbose_name='исполнитель')),
                ('numberAttorney', models.CharField(db_index=True, max_length=255, null=True, verbose_name='номер доверенности')),
                ('numberSeats', models.CharField(db_index=True, max_length=255, null=True, verbose_name='количество мест')),
                ('type', models.IntegerField(db_index=True, null=True, verbose_name='тип накладной')),
                ('numberNakladnaia', models.BigIntegerField(db_index=True, null=True, verbose_name='номер в накладной')),
                ('seria', models.CharField(db_index=True, max_length=255, null=True, verbose_name='серия накладной')),
                ('price_no_nds', models.FloatField(db_index=True, null=True, verbose_name='цена  без ндс')),
                ('price_ed_iz', models.FloatField(db_index=True, null=True, verbose_name='цена ed')),
                ('price', models.FloatField(db_index=True, null=True, verbose_name='цена')),
                ('nds', models.FloatField(db_index=True, null=True, verbose_name='НДС')),
                ('ves_nakladnaya', models.FloatField(db_index=True, null=True, verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, null=True, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, null=True, verbose_name='еденицы измерения')),
                ('razreshil', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто разрешил')),
                ('pogruzka', models.CharField(db_index=True, max_length=255, null=True, verbose_name='место погрузки')),
                ('prinyal', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто принял')),
                ('putlist', models.BigIntegerField(db_index=True, null=True, verbose_name='номер путевого листа')),
                ('osnovanie', models.CharField(db_index=True, max_length=255, null=True, verbose_name='основание')),
                ('agents', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='CatalogResponsiblePerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='имя')),
                ('second_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='отчество')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='фамилия')),
                ('role', models.CharField(blank=True, max_length=100, null=True, verbose_name='должность')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Auto', models.BooleanField(default=False, verbose_name='Авто занято')),
                ('Zd', models.BooleanField(default=False, verbose_name='ЖД занято')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='название')),
                ('number', models.CharField(db_index=True, max_length=255, null=True, verbose_name='номер')),
                ('characteristicTMC', models.CharField(db_index=True, max_length=255, null=True, verbose_name='характеристика ТМЦ')),
                ('typeTMC', models.CharField(db_index=True, max_length=255, null=True, verbose_name='тип ТМЦ')),
                ('scoreTMC', models.CharField(db_index=True, max_length=255, null=True, verbose_name='счет ТМЦ')),
                ('score', models.CharField(db_index=True, max_length=255, null=True, verbose_name='счет')),
                ('typeOfAccountTMC', models.CharField(db_index=True, max_length=255, null=True, verbose_name='вид учета ТМЦ')),
            ],
        ),
        migrations.CreateModel(
            name='Vagon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(db_index=True, max_length=255, verbose_name='Номер')),
                ('nakladnaya', models.CharField(db_index=True, default=0, max_length=255, verbose_name='Накладная')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('last_in', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего въезда')),
                ('last_out', models.DateTimeField(db_index=True, null=True, verbose_name='время последнего выезда')),
                ('ves_in', models.FloatField(db_index=True, null=True, verbose_name='вес на въезде')),
                ('ves_out', models.FloatField(db_index=True, null=True, verbose_name='вес на выезде')),
                ('netto', models.FloatField(db_index=True, null=True, verbose_name='полсденее нетто')),
                ('status_in', models.BooleanField(default=False, verbose_name='На территории?')),
                ('agent_vagon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Вагон',
                'verbose_name_plural': 'Вагоны',
            },
        ),
        migrations.CreateModel(
            name='DataNakladnayaVagon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.BigIntegerField(null=True, verbose_name='номер в накладной')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='действие')),
                ('price', models.FloatField(db_index=True, verbose_name='цена')),
                ('ves_nakladnaya', models.BigIntegerField(verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, verbose_name='еденицы измерения')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ves.Vagon')),
                ('productionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Production')),
            ],
            options={
                'verbose_name': 'Данные по накладной',
                'verbose_name_plural': 'Данные по накладным',
            },
        ),
        migrations.CreateModel(
            name='DataNakladnayaAuto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(db_index=True, null=True, verbose_name='тип накладной')),
                ('number', models.BigIntegerField(db_index=True, null=True, verbose_name='номер в накладной')),
                ('seria', models.CharField(db_index=True, max_length=255, null=True, verbose_name='серия накладной')),
                ('name', models.CharField(db_index=True, max_length=255, null=True, verbose_name='наимеонвание')),
                ('price_one', models.FloatField(db_index=True, null=True, verbose_name='цена за ед')),
                ('price_no_nds', models.FloatField(db_index=True, null=True, verbose_name='цена  без ндс')),
                ('price', models.FloatField(db_index=True, null=True, verbose_name='цена')),
                ('nds', models.FloatField(db_index=True, null=True, verbose_name='НДС')),
                ('ves_nakladnaya', models.FloatField(db_index=True, null=True, verbose_name='вес по накладной')),
                ('price_ed', models.CharField(max_length=100, null=True, verbose_name='валюта')),
                ('ves_ed', models.CharField(max_length=100, null=True, verbose_name='еденицы измерения')),
                ('razreshil', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто разрешил')),
                ('pogruzka', models.CharField(db_index=True, max_length=255, null=True, verbose_name='место погрузки')),
                ('prinyal', models.CharField(db_index=True, max_length=255, null=True, verbose_name='кто принял')),
                ('putlist', models.BigIntegerField(db_index=True, null=True, verbose_name='номер путевого листа')),
                ('name_drive', models.CharField(db_index=True, max_length=255, null=True, verbose_name='имя водителя')),
                ('osnovanie', models.CharField(db_index=True, max_length=255, null=True, verbose_name='основание')),
                ('date', models.DateField(null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ves.Auto')),
                ('productionId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Production')),
            ],
            options={
                'verbose_name': 'Данные по накладной',
                'verbose_name_plural': 'Данные по накладным',
            },
        ),
        migrations.CreateModel(
            name='CatalogTrailer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tara', models.FloatField(db_index=True, null=True, verbose_name='вес')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер')),
                ('marka', models.CharField(db_index=True, max_length=255, verbose_name='Марка')),
                ('model', models.CharField(db_index=True, max_length=255, verbose_name='Модель')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Прицеп',
                'verbose_name_plural': 'Прицепы',
            },
        ),
        migrations.CreateModel(
            name='CatalogContract',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='название контракта')),
                ('date', models.DateField(blank=True, null=True, verbose_name='дата')),
                ('typeOfOperation', models.CharField(db_index=True, max_length=255, verbose_name='тип опреации')),
                ('typeOfArrival', models.CharField(db_index=True, max_length=255, verbose_name='вид прихода')),
                ('salesAccount', models.CharField(db_index=True, max_length=255, verbose_name='счет реализации')),
                ('firstPrice', models.FloatField(db_index=True, null=True, verbose_name='первичная цена')),
                ('unitPrice', models.CharField(max_length=20, null=True, verbose_name='валюта')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('parentContragentId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
                ('parentMaterialId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Production')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogAuto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tara', models.FloatField(db_index=True, null=True, verbose_name='вес')),
                ('number', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Номер')),
                ('marka', models.CharField(db_index=True, max_length=255, verbose_name='Марка')),
                ('model', models.CharField(db_index=True, max_length=255, verbose_name='Модель')),
                ('date_add', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.Agent')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.AddField(
            model_name='auto',
            name='catalog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.CatalogAuto'),
        ),
        migrations.AddField(
            model_name='auto',
            name='catalogpricep',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ves.CatalogTrailer'),
        ),
        migrations.AddField(
            model_name='auto',
            name='parentcontractid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.CatalogContract'),
        ),
        migrations.AddField(
            model_name='auto',
            name='parentresponseid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ves.CatalogResponsiblePerson'),
        ),
        migrations.AddField(
            model_name='auto',
            name='parentuserid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ActionUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(db_index=True, max_length=255, verbose_name='действие')),
                ('where', models.CharField(db_index=True, max_length=255, verbose_name='где')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('parentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
    ]
