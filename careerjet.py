import json
import requests
from bs4 import BeautifulSoup
from careerjet_api_client import CareerjetAPIClient

array = [
    'cs_CZ',
		'da_DK' ,
		'de_AT' ,
		'de_CH' ,
		'de_DE' ,
		'en_AE' ,
		'en_AU' ,
		'en_BD' ,
		'en_CA' ,
		'en_CN' ,
		'en_HK' ,
		'en_IE' ,
		'en_IN' ,
		'en_KW' ,
		'en_MY' ,
		'en_NZ' ,
		'en_OM' ,
		'en_PH' ,
		'en_PK' ,
		'en_QA' ,
		'en_SG' ,
		'en_GB' ,
		'en_US' ,
		'en_ZA' ,
		'en_SA' ,
		'en_TW' ,
		'en_VN' ,
		'es_AR' ,
		'es_BO' ,
		'es_CL' ,
		'es_CO' ,
		'es_CR' ,
		'es_DO' ,
		'es_EC' ,
		'es_ES' ,
		'es_GT' ,
		'es_MX' ,
		'es_PA' ,
		'es_PE' ,
		'es_PR' ,
		'es_PY' ,
		'es_UY' ,
		'es_VE' ,
		'fi_FI' ,
		'fr_CA' ,
		'fr_BE' ,
		'fr_CH' ,
		'fr_FR' ,
		'fr_LU' ,
		'fr_MA' ,
		'hu_HU' ,
		'it_IT' ,
		'ja_JP' ,
		'ko_KR' ,
		'nl_BE' ,
		'nl_NL' ,
		'no_NO' ,
		'pl_PL' ,
		'pt_PT' ,
		'pt_BR' ,
		'ru_RU' ,
		'ru_UA' ,
		'sv_SE' ,
		'sk_SK' ,
		'tr_TR' ,
		'uk_UA' ,
		'vi_VN' ,
		'zh_CN' ]

data = []

LOCALES = {
		'cs_CZ' : 'http://www.careerjet.cz' ,
		'da_DK' : 'http://www.careerjet.dk' ,
		'de_AT' : 'http://www.careerjet.at' ,
		'de_CH' : 'http://www.careerjet.ch' ,
		'de_DE' : 'http://www.careerjet.de' ,
		'en_AE' : 'http://www.careerjet.ae' ,
		'en_AU' : 'http://www.careerjet.com.au' ,
		'en_BD' : 'http://www.careerjet.com.bd' ,
		'en_CA' : 'http://www.careerjet.ca' ,
		'en_CN' : 'http://www.careerjet.com.cn' ,
		'en_HK' : 'http://www.careerjet.hk' ,
		'en_IE' : 'http://www.careerjet.ie' ,
		'en_IN' : 'http://www.careerjet.co.in' ,
		'en_KW' : 'http://www.careerjet.com.kw' ,
		'en_MY' : 'http://www.careerjet.com.my' ,
		'en_NZ' : 'http://www.careerjet.co.nz' ,
		'en_OM' : 'http://www.careerjet.com.om' ,
		'en_PH' : 'http://www.careerjet.ph' ,
		'en_PK' : 'http://www.careerjet.com.pk' ,
		'en_QA' : 'http://www.careerjet.com.qa' ,
		'en_SG' : 'http://www.careerjet.sg' ,
		'en_GB' : 'http://www.careerjet.co.uk' ,
		'en_US' : 'http://www.careerjet.com' ,
		'en_ZA' : 'http://www.careerjet.co.za' ,
		'en_SA' : 'http://www.careerjet-saudi-arabia.com' ,
		'en_TW' : 'http://www.careerjet.com.tw' ,
		'en_VN' : 'http://www.careerjet.vn' ,
		'es_AR' : 'http://www.opcionempleo.com.ar' ,
		'es_BO' : 'http://www.opcionempleo.com.bo' ,
		'es_CL' : 'http://www.opcionempleo.cl' ,
		'es_CO' : 'http://www.opcionempleo.com.co' ,
		'es_CR' : 'http://www.opcionempleo.co.cr' ,
		'es_DO' : 'http://www.opcionempleo.com.do' ,
		'es_EC' : 'http://www.opcionempleo.ec' ,
		'es_ES' : 'http://www.opcionempleo.com' ,
		'es_GT' : 'http://www.opcionempleo.com.gt' ,
		'es_MX' : 'http://www.opcionempleo.com.mx' ,
		'es_PA' : 'http://www.opcionempleo.com.pa' ,
		'es_PE' : 'http://www.opcionempleo.com.pe' ,
		'es_PR' : 'http://www.opcionempleo.com.pr' ,
		'es_PY' : 'http://www.opcionempleo.com.py' ,
		'es_UY' : 'http://www.opcionempleo.com.uy' ,
		'es_VE' : 'http://www.opcionempleo.com.ve' ,
		'fi_FI' : 'http://www.careerjet.fi' ,
		'fr_CA' : 'http://www.option-carriere.ca' ,
		'fr_BE' : 'http://www.optioncarriere.be' ,
		'fr_CH' : 'http://www.optioncarriere.ch' ,
		'fr_FR' : 'http://www.optioncarriere.com' ,
		'fr_LU' : 'http://www.optioncarriere.lu' ,
		'fr_MA' : 'http://www.optioncarriere.ma' ,
		'hu_HU' : 'http://www.careerjet.hu' ,
		'it_IT' : 'http://www.careerjet.it' ,
		'ja_JP' : 'http://www.careerjet.jp' ,
		'ko_KR' : 'http://www.careerjet.co.kr' ,
		'nl_BE' : 'http://www.careerjet.be' ,
		'nl_NL' : 'http://www.careerjet.nl' ,
		'no_NO' : 'http://www.careerjet.no' ,
		'pl_PL' : 'http://www.careerjet.pl' ,
		'pt_PT' : 'http://www.careerjet.pt' ,
		'pt_BR' : 'http://www.careerjet.com.br' ,
		'ru_RU' : 'http://www.careerjet.ru' ,
		'ru_UA' : 'http://www.careerjet.com.ua' ,
		'sv_SE' : 'http://www.careerjet.se' ,
		'sk_SK' : 'http://www.careerjet.sk' ,
		'tr_TR' : 'http://www.careerjet.com.tr' ,
		'uk_UA' : 'http://www.careerjet.ua' ,
		'vi_VN' : 'http://www.careerjet.com.vn' ,
		'zh_CN' : 'http://www.careerjet.cn' ,
}

def CareerJet(locale, loc, key):
    # Extract the locale code from the URL
    locale_code = [code for code, url in LOCALES.items() if url == locale]
    if not locale_code:
        print(f"Error: Locale code not found for URL {locale}")
        return

    try:
        cj = CareerjetAPIClient(locale_code[0])
    except Exception as e:
        print(f"Error creating CareerjetAPIClient: {e}")
        return

    result_json = cj.search({
        'location': loc,
        'keywords': key,
        'affid': 'c3fd1d19a754927bc31347c56f397b0f',
        'pagesize': '10',
        'page': 1,
        'user_ip': '192.168.0.102',
        'url': 'http://www.google.com/',
        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
    })

    max_pages = result_json['pages']
    print(max_pages)

    for value in range(1, 2):
        result_json = cj.search({
            'location': loc,
            'keywords': key,
            'affid': '213e213hd12344552',
            'pagesize': '99',
            'page': value,
            'user_ip': '11.22.33.44',
            'url': 'http://www.google.com/',
            'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
        })

        jobs = result_json['jobs']

        for job in jobs:
            id1 = job['url'].split('/')[-1].split('.')[0]
            date = job['date']
            mini_description = job['description']
            website = job['site']
            salary = job['salary']

            # Update this line to use the locale code instead of the URL
            url5 = LOCALES[locale_code[0]] + "/jobview/" + id1

            trade_spider(url5, locale, id1, date, mini_description, website, salary)

    with open("careerjet1.json", "w") as outf:
        json.dump(data, outf)


def trade_spider(url, locale, id1, date, mini_description, website, salary):
    print(url)

    try:
        source_code = requests.get(url)
        source_code.raise_for_status()

        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")

        for tag in soup.find_all("div", class_="job", limit=1):
            title = tag.find("a", class_="title_compact")
            title_compact = title.get_text()
            link = LOCALES[locale_code[0]] + title.get('href')
            company_compact = tag.find("span", class_="company_compact").get_text()
            location_compact = tag.find("span", class_="locations_compact").get_text()
            description_compact = tag.find("div", class_="advertise_compact").get_text()

            data.append({
                "id": id1,
                "date": date,
                "min_desc": mini_description,
                "website": website,
                "salary": salary,
                "apply_link": link,
                "company_name": company_compact,
                "title": title_compact,
                "location": location_compact,
                "full_desc": description_compact
            })
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")


for val in array:
    CareerJet(LOCALES[val], "", "")
