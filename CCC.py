import requests as rq
from bs4 import BeautifulSoup as BS
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.ticker import FixedFormatter,LinearLocator
import pandas as pd

rq.get('https://google.com', verify=False)
user_text = int(input("Enter please interval in second: ")) #пользовательские настройки

#запрос api
def make_api_request():

    url_usd = 'https://ru.investing.com/currencies/usd-rub'
    url_eur = 'https://ru.investing.com/currencies/eur-rub'
    url_gbr = 'https://ru.investing.com/currencies/gbp-rub'

    text_usd = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'
    text_usd_growth = 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-negative-main'
    text_eur = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'
    text_eur_growth = 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-inv-grey-700'
    text_gbr = 'text-5xl/9 font-bold text-[#232526] md:text-[42px] md:leading-[60px]'
    text_gbr_growth = 'flex items-center gap-2 text-base/6 font-bold md:text-xl/7 rtl:force-ltr text-positive-main'

    #отправка запроса валюты
    response_usd = rq.get(url_usd)
    response_eur = rq.get(url_eur)
    response_gbr = rq.get(url_gbr)

    requests_on_usd = BS(response_usd.text, features='html.parser')
    requests_on_eur = BS(response_eur.text, features='html.parser')
    requests_on_gbr = BS(response_gbr.text, features='html.parser')

    text_usd = requests_on_usd.find(class_=text_usd)
    text_eur = requests_on_eur.find(class_=text_eur)
    text_gbr = requests_on_gbr.find(class_=text_gbr)

    #отправка запроса роста валюты
    response_usd_growth = rq.get(url_usd)
    response_eur_growth = rq.get(url_eur)
    response_gbr_growth = rq.get(url_gbr)

    requests_on_usd_growth = BS(response_usd_growth.text, features='html.parser')
    requests_on_eur_growth = BS(response_eur_growth.text, features='html.parser')
    requests_on_gbr_growth = BS(response_gbr_growth.text, features='html.parser')

    text_usd_growth = requests_on_usd_growth.find(class_=text_usd_growth)
    text_eur_growth = requests_on_eur_growth.find(class_=text_eur_growth)
    text_gbr_growth = requests_on_gbr_growth.find(class_=text_gbr_growth)

    #валюта
    USD_y = text_usd.text
    EUR_y = text_eur.text
    GBR_y = text_gbr.text

    name_text_two = ['Валюта:']

    data = ({'USD': [USD_y],
             'EUR': [EUR_y],
             'GBR': [GBR_y]})


    base_data_one = pd.DataFrame(data=data, index=[name_text_two])
    print(base_data_one)


    #рост валюты
    USD_y_growth = text_usd_growth.text
    EUR_y_growth = text_eur_growth.text
    GBR_y_growth = text_gbr_growth.text

    name_text_two_growth = ['Рост:']

    data = ({'USD-GROWTH': [USD_y_growth],
             'EUR-GROWTH': [EUR_y_growth],
             'OIL-GROWTH': [GBR_y_growth]})


    base_data_two = pd.DataFrame(data=data, index=[name_text_two_growth])
    print(base_data_two)




    USD_y = int(float(USD_y.replace(',','.')))
    EUR_y = int(float(EUR_y.replace(',','.')))
    GBR_y = int(float(GBR_y.replace(',','.')))

    fig = plt.figure(figsize=(7,4))
    ax = plt.subplot()

    x1 = np.array([1])
    y1 = np.array([USD_y])

    x2 = np.array([2])
    y2 = np.array([EUR_y])

    x3 = np.array([3])
    y3 = np.array([GBR_y])

    ax.bar(x1,y1,label='USD')
    ax.bar(x2,y2,label='EUR')
    ax.bar(x3, y3, label='GBR')

    ax.xaxis.set_major_locator(LinearLocator(3))
    ax.xaxis.set_major_formatter(FixedFormatter([USD_y_growth,EUR_y_growth,GBR_y_growth]))

    fig.suptitle('It is monitoring USD/EUR/GBR')

    ax.legend(['USD','EUR','GBR'])

    plt.show()
    plt.close(fig)



while True:

    time.sleep(user_text)  # Пауза-интервал
    print('>>Close window for update base date<<')
    make_api_request()