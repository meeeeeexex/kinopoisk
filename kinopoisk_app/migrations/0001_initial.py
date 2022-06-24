# Generated by Django 4.0.4 on 2022-06-17 16:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('country', models.CharField(choices=[('Aruba', 'Aruba'), ('Afghanistan', 'Afghanistan'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Åland Islands', 'Åland Islands'), ('Albania', 'Albania'), ('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('American Samoa', 'American Samoa'), ('Antarctica', 'Antarctica'), ('French Southern Territories', 'French Southern Territories'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Burundi', 'Burundi'), ('Belgium', 'Belgium'), ('Benin', 'Benin'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Burkina Faso', 'Burkina Faso'), ('Bangladesh', 'Bangladesh'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Bahamas', 'Bahamas'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Bermuda', 'Bermuda'), ('Bolivia, Plurinational State of', 'Bolivia, Plurinational State of'), ('Brazil', 'Brazil'), ('Barbados', 'Barbados'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Central African Republic', 'Central African Republic'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Switzerland', 'Switzerland'), ('Chile', 'Chile'), ('China', 'China'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Cameroon', 'Cameroon'), ('Congo, The Democratic Republic of the', 'Congo, The Democratic Republic of the'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Cabo Verde', 'Cabo Verde'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cayman Islands', 'Cayman Islands'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Denmark', 'Denmark'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('Eritrea', 'Eritrea'), ('Western Sahara', 'Western Sahara'), ('Spain', 'Spain'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('France', 'France'), ('Faroe Islands', 'Faroe Islands'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Gabon', 'Gabon'), ('United Kingdom', 'United Kingdom'), ('Georgia', 'Georgia'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Gambia', 'Gambia'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('French Guiana', 'French Guiana'), ('Guam', 'Guam'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Ireland', 'Ireland'), ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'), ('Iraq', 'Iraq'), ('Iceland', 'Iceland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Macao', 'Macao'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Maldives', 'Maldives'), ('Mexico', 'Mexico'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Myanmar', 'Myanmar'), ('Montenegro', 'Montenegro'), ('Mongolia', 'Mongolia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Mozambique', 'Mozambique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Martinique', 'Martinique'), ('Mauritius', 'Mauritius'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mayotte', 'Mayotte'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Niue', 'Niue'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Pitcairn', 'Pitcairn'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Palau', 'Palau'), ('Papua New Guinea', 'Papua New Guinea'), ('Poland', 'Poland'), ('Puerto Rico', 'Puerto Rico'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Portugal', 'Portugal'), ('Paraguay', 'Paraguay'), ('Palestine, State of', 'Palestine, State of'), ('French Polynesia', 'French Polynesia'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Senegal', 'Senegal'), ('Singapore', 'Singapore'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Solomon Islands', 'Solomon Islands'), ('Sierra Leone', 'Sierra Leone'), ('El Salvador', 'El Salvador'), ('San Marino', 'San Marino'), ('Somalia', 'Somalia'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Serbia', 'Serbia'), ('South Sudan', 'South Sudan'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Suriname', 'Suriname'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Sweden', 'Sweden'), ('Eswatini', 'Eswatini'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Seychelles', 'Seychelles'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Chad', 'Chad'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Timor-Leste', 'Timor-Leste'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Uruguay', 'Uruguay'), ('United States', 'United States'), ('Uzbekistan', 'Uzbekistan'), ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Venezuela, Bolivarian Republic of', 'Venezuela, Bolivarian Republic of'), ('Virgin Islands, British', 'Virgin Islands, British'), ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Not specified', max_length=100, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=158, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('country', models.CharField(choices=[('Aruba', 'Aruba'), ('Afghanistan', 'Afghanistan'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Åland Islands', 'Åland Islands'), ('Albania', 'Albania'), ('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('American Samoa', 'American Samoa'), ('Antarctica', 'Antarctica'), ('French Southern Territories', 'French Southern Territories'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Burundi', 'Burundi'), ('Belgium', 'Belgium'), ('Benin', 'Benin'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Burkina Faso', 'Burkina Faso'), ('Bangladesh', 'Bangladesh'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Bahamas', 'Bahamas'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Bermuda', 'Bermuda'), ('Bolivia, Plurinational State of', 'Bolivia, Plurinational State of'), ('Brazil', 'Brazil'), ('Barbados', 'Barbados'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Central African Republic', 'Central African Republic'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Switzerland', 'Switzerland'), ('Chile', 'Chile'), ('China', 'China'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Cameroon', 'Cameroon'), ('Congo, The Democratic Republic of the', 'Congo, The Democratic Republic of the'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Cabo Verde', 'Cabo Verde'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cayman Islands', 'Cayman Islands'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Denmark', 'Denmark'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('Eritrea', 'Eritrea'), ('Western Sahara', 'Western Sahara'), ('Spain', 'Spain'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('France', 'France'), ('Faroe Islands', 'Faroe Islands'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Gabon', 'Gabon'), ('United Kingdom', 'United Kingdom'), ('Georgia', 'Georgia'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Gambia', 'Gambia'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('French Guiana', 'French Guiana'), ('Guam', 'Guam'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Ireland', 'Ireland'), ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'), ('Iraq', 'Iraq'), ('Iceland', 'Iceland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Macao', 'Macao'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Maldives', 'Maldives'), ('Mexico', 'Mexico'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Myanmar', 'Myanmar'), ('Montenegro', 'Montenegro'), ('Mongolia', 'Mongolia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Mozambique', 'Mozambique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Martinique', 'Martinique'), ('Mauritius', 'Mauritius'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mayotte', 'Mayotte'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Niue', 'Niue'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Pitcairn', 'Pitcairn'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Palau', 'Palau'), ('Papua New Guinea', 'Papua New Guinea'), ('Poland', 'Poland'), ('Puerto Rico', 'Puerto Rico'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Portugal', 'Portugal'), ('Paraguay', 'Paraguay'), ('Palestine, State of', 'Palestine, State of'), ('French Polynesia', 'French Polynesia'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Senegal', 'Senegal'), ('Singapore', 'Singapore'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Solomon Islands', 'Solomon Islands'), ('Sierra Leone', 'Sierra Leone'), ('El Salvador', 'El Salvador'), ('San Marino', 'San Marino'), ('Somalia', 'Somalia'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Serbia', 'Serbia'), ('South Sudan', 'South Sudan'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Suriname', 'Suriname'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Sweden', 'Sweden'), ('Eswatini', 'Eswatini'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Seychelles', 'Seychelles'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Chad', 'Chad'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Timor-Leste', 'Timor-Leste'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Uruguay', 'Uruguay'), ('United States', 'United States'), ('Uzbekistan', 'Uzbekistan'), ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Venezuela, Bolivarian Republic of', 'Venezuela, Bolivarian Republic of'), ('Virgin Islands, British', 'Virgin Islands, British'), ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Not specified', max_length=100, verbose_name='Страна')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=158, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('country', models.CharField(choices=[('Aruba', 'Aruba'), ('Afghanistan', 'Afghanistan'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Åland Islands', 'Åland Islands'), ('Albania', 'Albania'), ('Andorra', 'Andorra'), ('United Arab Emirates', 'United Arab Emirates'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('American Samoa', 'American Samoa'), ('Antarctica', 'Antarctica'), ('French Southern Territories', 'French Southern Territories'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Burundi', 'Burundi'), ('Belgium', 'Belgium'), ('Benin', 'Benin'), ('Bonaire, Sint Eustatius and Saba', 'Bonaire, Sint Eustatius and Saba'), ('Burkina Faso', 'Burkina Faso'), ('Bangladesh', 'Bangladesh'), ('Bulgaria', 'Bulgaria'), ('Bahrain', 'Bahrain'), ('Bahamas', 'Bahamas'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Belarus', 'Belarus'), ('Belize', 'Belize'), ('Bermuda', 'Bermuda'), ('Bolivia, Plurinational State of', 'Bolivia, Plurinational State of'), ('Brazil', 'Brazil'), ('Barbados', 'Barbados'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bhutan', 'Bhutan'), ('Bouvet Island', 'Bouvet Island'), ('Botswana', 'Botswana'), ('Central African Republic', 'Central African Republic'), ('Canada', 'Canada'), ('Cocos (Keeling) Islands', 'Cocos (Keeling) Islands'), ('Switzerland', 'Switzerland'), ('Chile', 'Chile'), ('China', 'China'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Cameroon', 'Cameroon'), ('Congo, The Democratic Republic of the', 'Congo, The Democratic Republic of the'), ('Congo', 'Congo'), ('Cook Islands', 'Cook Islands'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Cabo Verde', 'Cabo Verde'), ('Costa Rica', 'Costa Rica'), ('Cuba', 'Cuba'), ('Curaçao', 'Curaçao'), ('Christmas Island', 'Christmas Island'), ('Cayman Islands', 'Cayman Islands'), ('Cyprus', 'Cyprus'), ('Czechia', 'Czechia'), ('Germany', 'Germany'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Denmark', 'Denmark'), ('Dominican Republic', 'Dominican Republic'), ('Algeria', 'Algeria'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('Eritrea', 'Eritrea'), ('Western Sahara', 'Western Sahara'), ('Spain', 'Spain'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Finland', 'Finland'), ('Fiji', 'Fiji'), ('Falkland Islands (Malvinas)', 'Falkland Islands (Malvinas)'), ('France', 'France'), ('Faroe Islands', 'Faroe Islands'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Gabon', 'Gabon'), ('United Kingdom', 'United Kingdom'), ('Georgia', 'Georgia'), ('Guernsey', 'Guernsey'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Guinea', 'Guinea'), ('Guadeloupe', 'Guadeloupe'), ('Gambia', 'Gambia'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Greenland', 'Greenland'), ('Guatemala', 'Guatemala'), ('French Guiana', 'French Guiana'), ('Guam', 'Guam'), ('Guyana', 'Guyana'), ('Hong Kong', 'Hong Kong'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Honduras', 'Honduras'), ('Croatia', 'Croatia'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('Indonesia', 'Indonesia'), ('Isle of Man', 'Isle of Man'), ('India', 'India'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Ireland', 'Ireland'), ('Iran, Islamic Republic of', 'Iran, Islamic Republic of'), ('Iraq', 'Iraq'), ('Iceland', 'Iceland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Japan', 'Japan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Cambodia', 'Cambodia'), ('Kiribati', 'Kiribati'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Korea, Republic of', 'Korea, Republic of'), ('Kuwait', 'Kuwait'), ("Lao People's Democratic Republic", "Lao People's Democratic Republic"), ('Lebanon', 'Lebanon'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Saint Lucia', 'Saint Lucia'), ('Liechtenstein', 'Liechtenstein'), ('Sri Lanka', 'Sri Lanka'), ('Lesotho', 'Lesotho'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Latvia', 'Latvia'), ('Macao', 'Macao'), ('Saint Martin (French part)', 'Saint Martin (French part)'), ('Morocco', 'Morocco'), ('Monaco', 'Monaco'), ('Moldova, Republic of', 'Moldova, Republic of'), ('Madagascar', 'Madagascar'), ('Maldives', 'Maldives'), ('Mexico', 'Mexico'), ('Marshall Islands', 'Marshall Islands'), ('North Macedonia', 'North Macedonia'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Myanmar', 'Myanmar'), ('Montenegro', 'Montenegro'), ('Mongolia', 'Mongolia'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Mozambique', 'Mozambique'), ('Mauritania', 'Mauritania'), ('Montserrat', 'Montserrat'), ('Martinique', 'Martinique'), ('Mauritius', 'Mauritius'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Mayotte', 'Mayotte'), ('Namibia', 'Namibia'), ('New Caledonia', 'New Caledonia'), ('Niger', 'Niger'), ('Norfolk Island', 'Norfolk Island'), ('Nigeria', 'Nigeria'), ('Nicaragua', 'Nicaragua'), ('Niue', 'Niue'), ('Netherlands', 'Netherlands'), ('Norway', 'Norway'), ('Nepal', 'Nepal'), ('Nauru', 'Nauru'), ('New Zealand', 'New Zealand'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Pitcairn', 'Pitcairn'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Palau', 'Palau'), ('Papua New Guinea', 'Papua New Guinea'), ('Poland', 'Poland'), ('Puerto Rico', 'Puerto Rico'), ("Korea, Democratic People's Republic of", "Korea, Democratic People's Republic of"), ('Portugal', 'Portugal'), ('Paraguay', 'Paraguay'), ('Palestine, State of', 'Palestine, State of'), ('French Polynesia', 'French Polynesia'), ('Qatar', 'Qatar'), ('Réunion', 'Réunion'), ('Romania', 'Romania'), ('Rwanda', 'Rwanda'), ('Saudi Arabia', 'Saudi Arabia'), ('Sudan', 'Sudan'), ('Senegal', 'Senegal'), ('Singapore', 'Singapore'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Svalbard and Jan Mayen', 'Svalbard and Jan Mayen'), ('Solomon Islands', 'Solomon Islands'), ('Sierra Leone', 'Sierra Leone'), ('El Salvador', 'El Salvador'), ('San Marino', 'San Marino'), ('Somalia', 'Somalia'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Serbia', 'Serbia'), ('South Sudan', 'South Sudan'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Suriname', 'Suriname'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Sweden', 'Sweden'), ('Eswatini', 'Eswatini'), ('Sint Maarten (Dutch part)', 'Sint Maarten (Dutch part)'), ('Seychelles', 'Seychelles'), ('Syrian Arab Republic', 'Syrian Arab Republic'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Chad', 'Chad'), ('Togo', 'Togo'), ('Thailand', 'Thailand'), ('Tajikistan', 'Tajikistan'), ('Tokelau', 'Tokelau'), ('Turkmenistan', 'Turkmenistan'), ('Timor-Leste', 'Timor-Leste'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Tuvalu', 'Tuvalu'), ('Taiwan, Province of China', 'Taiwan, Province of China'), ('Tanzania, United Republic of', 'Tanzania, United Republic of'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United States Minor Outlying Islands', 'United States Minor Outlying Islands'), ('Uruguay', 'Uruguay'), ('United States', 'United States'), ('Uzbekistan', 'Uzbekistan'), ('Holy See (Vatican City State)', 'Holy See (Vatican City State)'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Venezuela, Bolivarian Republic of', 'Venezuela, Bolivarian Republic of'), ('Virgin Islands, British', 'Virgin Islands, British'), ('Virgin Islands, U.S.', 'Virgin Islands, U.S.'), ('Viet Nam', 'Viet Nam'), ('Vanuatu', 'Vanuatu'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Samoa', 'Samoa'), ('Yemen', 'Yemen'), ('South Africa', 'South Africa'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], default='Not specified', max_length=100, verbose_name='Страна')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Biography', 'Biography'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Thriller', 'Thriller'), ('Western', 'Western')], default='Not specified', max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Информация о фильме')),
                ('user_rating', models.IntegerField(default=0, verbose_name='Рейтинг пользователя')),
                ('critique_rating', models.IntegerField(default=0, verbose_name='Рейтинг критика')),
                ('picture_blob', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('actor_squad', models.ManyToManyField(related_name='movies', to='kinopoisk_app.actor', verbose_name='Актеры')),
                ('film_director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='kinopoisk_app.director', verbose_name='Режиссер')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinopoisk_app.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('headline', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('review_text', models.TextField(verbose_name='Отзыв')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='kinopoisk_app.movie', verbose_name='Фильм')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(choices=[('Multiplex', 'Multiplex'), ('Butterfly', 'Butterfly'), ('Planeta kino', 'Planeta kino'), ('Oskar', 'Oskar'), ('Sputnik', 'Sputnik'), ('Liniya kino', 'Liniya kino'), ("Kievskaya Rus'", "Kievskaya Rus'")], default='Not specified', max_length=100, verbose_name='Название')),
                ('city', models.CharField(choices=[('Kyiv', 'Kyiv'), ('Vinnitsa', 'Vinnitsa'), ('Uman', 'Uman'), ('Zaporozhje', 'Zaporozhje'), ('Kharkov', 'Kharkov'), ('Lvov', 'Lvov'), ('Poltava', 'Poltava'), ('Zhitomir', 'Zhitomir'), ('Dnepr', 'Dnepr'), ('Lutsk', 'Lutsk'), ('Chernovrtsi', 'Chernovrtsi'), ('Uzhgorod', 'Uzhgorod'), ('Kherson', 'Kherson')], default='Not specified', max_length=100, verbose_name='Город')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('movies', models.ManyToManyField(related_name='in_cinema', to='kinopoisk_app.movie')),
            ],
            options={
                'verbose_name': 'Кинотеатр',
                'verbose_name_plural': 'Кинотеатры',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, to='kinopoisk_app.genre', verbose_name='Любимые жанры'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_movies',
            field=models.ManyToManyField(blank=True, to='kinopoisk_app.movie', verbose_name='Избранные фильмы'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
