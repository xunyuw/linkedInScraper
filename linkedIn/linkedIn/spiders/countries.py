
import unicodedata

def unicodeHandle(stuff):
	return unicodedata.normalize('NFKD', stuff).encode('ascii','ignore')



default = 'US'

countries = dict([
	('United States of America' , 'US'),
	('United States' , 'US'),
	('Estados Unidos' , 'US'),

	('Andorra' , 'AD'),
	('United Arab Emirates' , 'AE'),
	('Afghanistan' , 'AF'),
	('Antigua & Barbuda' , 'AG'),
	('Anguilla' , 'AI'),
	('Albania' , 'AL'),
	('Armenia' , 'AM'),
	('Netherlands Antilles' , 'AN'),
	('Angola' , 'AO'),
	('Antarctica' , 'AQ'),
	('Argentina' , 'AR'),
	('American Samoa' , 'AS'),
	('Austria' , 'AT'),
	('Australia' , 'AU'),
	('Aruba' , 'AW'),
	('Azerbaijan' , 'AZ'),
	('Bosnia and Herzegovina' , 'BA'),
	('Barbados' , 'BB'),
	('Bangladesh' , 'BD'),
	('Belgium' , 'BE'),
	('Burkina Faso' , 'BF'),
	('Bulgaria' , 'BG'),
	('Bahrain' , 'BH'),
	('Burundi' , 'BI'),
	('Benin' , 'BJ'),
	('Bermuda' , 'BM'),
	('Brunei Darussalam' , 'BN'),
	('Bolivia' , 'BO'),
	('Brazil' , 'BR'),
	('Brasil' , 'BR'),
	
	
	('Bahama' , 'BS'),
	('Bhutan' , 'BT'),
	('Burma ' , 'BU'),
	('Bouvet Island' , 'BV'),
	('Botswana' , 'BW'),
	('Belarus' , 'BY'),
	('Belize' , 'BZ'),
	('Canada' , 'CA'),
	('Cocos(Islands' , 'CC'),
	('Central African Republic' , 'CF'),
	('Congo' , 'CG'),
	('Switzerland' , 'CH'),
	('Cote D\'ivoire ' , 'CI'),
	('Cook Iislands' , 'CK'),
	('Chile' , 'CL'),
	('Cameroon' , 'CM'),
	('China' , 'CN'),
	('Colombia' , 'CO'),
	('Costa Rica' , 'CR'),
	('Czechoslovakia ' , 'CS'),
	('Cuba' , 'CU'),
	('Cape Verde' , 'CV'),
	('Christmas Island' , 'CX'),
	('Cyprus' , 'CY'),
	('Czech Republic' , 'CZ'),
	('German Democratic Republic ' , 'DD'),
	('Germany' , 'DE'),
	('Deutschland' , 'DE'),
	('Alemania' , 'DE'),
	
	
	('Djibouti' , 'DJ'),
	('Denmark' , 'DK'),
	('Dominica' , 'DM'),
	('Dominican Republic' , 'DO'),
	('Algeria' , 'DZ'),
	('Ecuador' , 'EC'),
	('Estonia' , 'EE'),
	('Egypt' , 'EG'),
	('Western Sahara' , 'EH'),
	('Eritrea' , 'ER'),
	('Spain' , 'ES'),
	('Espana', 'ES'),
	('Ethiopia' , 'ET'),
	('Finland' , 'FI'),
	('Fiji' , 'FJ'),
	('Falkland Islands ' , 'FK'),
	('Micronesia' , 'FM'),
	('Faroe Islands' , 'FO'),
	('France' , 'FR'),
	('France), Metropolitan' , 'FX'),
	('Gabon' , 'GA'),
	('United Kingdom' , 'GB'),
	('Grenada' , 'GD'),
	('Georgia' , 'GE'),
	('French Guiana' , 'GF'),
	('Ghana' , 'GH'),
	('Gibraltar' , 'GI'),
	('Greenland' , 'GL'),
	('Gambia' , 'GM'),
	('Guinea' , 'GN'),
	('Guadeloupe' , 'GP'),
	('Equatorial Guinea' , 'GQ'),
	('Greece' , 'GR'),
	('South Georgia and the South Sandwich Islands' , 'GS'),
	('Guatemala' , 'GT'),
	('Guam' , 'GU'),
	('Guinea-Bissau' , 'GW'),
	('Guyana' , 'GY'),
	('Hong Kong' , 'HK'),
	('Heard & McDonald Islands' , 'HM'),
	('Honduras' , 'HN'),
	('Croatia' , 'HR'),
	('Haiti' , 'HT'),
	('Hungary' , 'HU'),
	('Indonesia' , 'ID'),
	('Ireland' , 'IE'),
	('Israel' , 'IL'),
	('India' , 'IN'),
	('British Indian Ocean Territory' , 'IO'),
	('Iraq' , 'IQ'),
	('Islamic Republic of Iran' , 'IR'),
	('Iran', 'IR'),
	('Iceland' , 'IS'),
	('Italy' , 'IT'),
	('Italia', 'IT'),
	('Jamaica' , 'JM'),
	('Jordan' , 'JO'),
	('Japan' , 'JP'),
	('Kenya' , 'KE'),
	('Kyrgyzstan' , 'KG'),
	('Cambodia' , 'KH'),
	('Kiribati' , 'KI'),
	('Comoros' , 'KM'),
	('St. Kitts and Nevis' , 'KN'),
	('Korea), Democratic People\'s Republic of' , 'KP'),
	('Korea), Republic of' , 'KR'),
	('Kuwait' , 'KW'),
	('Cayman Islands' , 'KY'),
	('Kazakhstan' , 'KZ'),
	('Lao People\'s Democratic Republic' , 'LA'),
	('Lebanon' , 'LB'),
	('Saint Lucia' , 'LC'),
	('Liechtenstein' , 'LI'),
	('Sri Lanka' , 'LK'),
	('Liberia' , 'LR'),
	('Lesotho' , 'LS'),
	('Lithuania' , 'LT'),
	('Luxembourg' , 'LU'),
	('Latvia' , 'LV'),
	('Libyan Arab Jamahiriya' , 'LY'),
	('Macedonia', 'MD'),
	('Morocco' , 'MA'),
	('Maroc', 'MA'),
	('Monaco' , 'MC'),
	('Moldova, Republic of' , 'MD'),
	('Madagascar' , 'MG'),
	('Marshall Islands' , 'MH'),
	('Mali' , 'ML'),
	('Mongolia' , 'MN'),
	('Myanmar' , 'MM'),
	('Macau' , 'MO'),
	('Northern Mariana Islands' , 'MP'),
	('Martinique' , 'MQ'),
	('Mauritania' , 'MR'),
	('Monserrat' , 'MS'),
	('Malta' , 'MT'),
	('Mauritius' , 'MU'),
	('Maldives' , 'MV'),
	('Malawi' , 'MW'),
	('Mexico' , 'MX'),
	('Malaysia' , 'MY'),
	('Mozambique' , 'MZ'),
	('Namibia' , 'NA'),
	('New Caledonia' , 'NC'),
	('Niger' , 'NE'),
	('Norfolk Island' , 'NF'),
	('Nigeria' , 'NG'),
	('Nicaragua' , 'NI'),
	('Netherlands' , 'NL'),
	('Norway' , 'NO'),
	('Nepal' , 'NP'),
	('Nauru' , 'NR'),
	('Neutral Zone ' , 'NT'),
	('Niue' , 'NU'),
	('New Zealand' , 'NZ'),
	('Oman' , 'OM'),
	('Panama' , 'PA'),
	('Peru' , 'PE'),
	('French Polynesia' , 'PF'),
	('Papua New Guinea' , 'PG'),
	('Philippines' , 'PH'),
	('Pakistan' , 'PK'),
	('Poland' , 'PL'),
	('St. Pierre & Miquelon' , 'PM'),
	('Pitcairn' , 'PN'),
	('Puerto Rico' , 'PR'),
	('Portugal' , 'PT'),
	('Palau' , 'PW'),
	('Paraguay' , 'PY'),
	('Qatar' , 'QA'),
	('Reunion' , 'RE'),
	('Romania' , 'RO'),
	('Russian Federation' , 'RU'),
	('Rwanda' , 'RW'),
	('Saudi Arabia' , 'SA'),
	('Solomon Islands' , 'SB'),
	('Seychelles' , 'SC'),
	('Sudan' , 'SD'),
	('Sweden' , 'SE'),
	('Singapore' , 'SG'),
	('St. Helena' , 'SH'),
	('Slovenia' , 'SI'),
	('Svalbard & Jan Mayen Islands' , 'SJ'),
	('Slovakia' , 'SK'),
	('Sierra Leone' , 'SL'),
	('San Marino' , 'SM'),
	('Senegal' , 'SN'),
	('Somalia' , 'SO'),
	('Suriname' , 'SR'),
	('Sao Tome & Principe' , 'ST'),
	('Union of Soviet Socialist Republics ' , 'SU'),
	('El Salvador' , 'SV'),
	('Syrian Arab Republic' , 'SY'),
	('Swaziland' , 'SZ'),
	('Turks & Caicos Islands' , 'TC'),
	('Chad' , 'TD'),
	('French Southern Territories' , 'TF'),
	('Togo' , 'TG'),
	('Thailand' , 'TH'),
	('Tajikistan' , 'TJ'),
	('Tokelau' , 'TK'),
	('Turkmenistan' , 'TM'),
	('Tunisia' , 'TN'),
	('Tonga' , 'TO'),
	('East Timor' , 'TP'),
	('Turkey' , 'TR'),
	('Turkiye', 'TR'),
	('Turkei', 'TR'),
	('Trinidad & Tobago' , 'TT'),
	('Tuvalu' , 'TV'),
	('Taiwan, Province of China' , 'TW'),
	('Taiwan', 'TW'),
	('Tanzania), United Republic of' , 'TZ'),
	('Ukraine' , 'UA'),
	('Uganda' , 'UG'),
	('United States Minor Outlying Islands' , 'UM'),
	('Uruguay' , 'UY'),
	('Uzbekistan' , 'UZ'),
	('Vatican City State ' , 'VA'),
	('St. Vincent & the Grenadines' , 'VC'),
	('Venezuela' , 'VE'),
	('British Virgin Islands' , 'VG'),
	('United States Virgin Islands' , 'VI'),
	('Viet Nam' , 'VN'),
	('Vietnam', 'VN'),
	('Vanuatu' , 'VU'),
	('Wallis & Futuna Islands' , 'WF'),
	('Samoa' , 'WS'),
	('Democratic Yemen ' , 'YD'),
	('Yemen' , 'YE'),
	('Mayotte' , 'YT'),
	('Yugoslavia' , 'YU'),
	('South Africa' , 'ZA'),
	('Zambia' , 'ZM'),
	('Zaire' , 'ZR'),
	('Zimbabwe' , 'ZW'),



])



def checkCountry(x):
	return countries.get(x,default)
	
def checkLocation(x):
	if not x:
		return False
	
	location = unicodeHandle(x[0])
	
	
	if not checkCountry(location) == 'US':
		return False
	
	comma = location.find(', ')
	
	if comma == -1:
		return True
	sublocations = location.split(', ')
	country = sublocations[-1]
	
	
	if not checkCountry(country) == 'US':
		return False
	area = country.find(' Area')
	
	if area == -1:
		return True
		
	country = country.split(' Area')
	country = country[0]
	if not checkCountry(country) == 'US':
		return False 
	
	return True
		
