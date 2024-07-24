import requests

class Converter:
    @staticmethod
    def usd_to_uzs(usd_amount):
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        data = response.json()

        
        usd_to_uzs_rate = None
        for item in data:
            if item['Ccy'] == 'USD':
                usd_to_uzs_rate = float(item['Rate'])

        if usd_to_uzs_rate:
            uzs_amount = usd_amount * usd_to_uzs_rate
            return uzs_amount
        else:
            raise ValueError("Failed to fetch USD to UZS exchange rate")

    @staticmethod
    def uzs_to_usd(uzs_amount):
       
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
        data = response.json()

        
        usd_to_uzs_rate = None
        for item in data:
            if item['Ccy'] == 'USD':
                usd_to_uzs_rate = float(item['Rate'])

        if usd_to_uzs_rate:
            usd_amount = uzs_amount / usd_to_uzs_rate
            return usd_amount
        else:
            raise ValueError("Failed to fetch USD to UZS exchange rate")


usd_amount = 100
uzs_amount = Converter.usd_to_uzs(usd_amount)
print(f"{usd_amount} USD = {uzs_amount} UZS")


uzs_amount = 1000000
usd_amount = Converter.uzs_to_usd(uzs_amount)
print(f"{uzs_amount} UZS = {usd_amount:.2f} USD")
