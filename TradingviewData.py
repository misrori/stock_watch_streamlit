import requests
import pandas as pd
import json

headers = {
    'authority': 'scanner.tradingview.com',
    'accept': 'text/plain, */*; q=0.01',
    'accept-language': 'hu-HU,hu;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'device_t=b3hrMjow.RizbtKug5ptWbNFgxGA_c_OS_4iw26dOeJ77H8vJp5A; sessionid=ceiec3s6wc9xphkm5mqo3nvh1ghvu8jd; cachec=undefined; etg=undefined; cookiesSettings={"analytics":true,"advertising":true}; cookiePrivacyPreferenceBannerProduction=accepted; _ga=GA1.2.2035191602.1664531277; _gid=GA1.2.794318526.1672824644; sessionid_sign=v1:B5ywf3++JLkbbj3AkPZY5Igp3qw2wZ2ND6Wia3Nzt+I=; _sp_ses.cf1a=*; _sp_id.cf1a=d43510cb-badc-4073-8503-f67ac9df0b05.1667582080.158.1673080966.1673041374.1d2ff23b-c64a-411d-b0a8-d92ad89b0086',
    'origin': 'https://www.tradingview.com',
    'referer': 'https://www.tradingview.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

data = '{"filter":[{"left":"type","operation":"in_range","right":["stock","dr","fund"]},{"left":"subtype","operation":"in_range","right":["common","foreign-issuer","","etf","etf,odd","etf,otc","etf,cfd"]},{"left":"exchange","operation":"in_range","right":["AMEX","NASDAQ","NYSE"]},{"left":"is_primary","operation":"equal","right":true},{"left":"active_symbol","operation":"equal","right":true}],"options":{"lang":"en"},"markets":["america"],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["logoid","name","close","market_cap_basic","price_earnings_ttm","price_revenue_ttm","earnings_per_share_basic_ttm","last_annual_eps","enterprise_value_ebitda_ttm","enterprise_value_fq","total_shares_outstanding_fundamental","description","type","subtype","update_mode","pricescale","minmov","fractional","minmove2","currency","fundamental_currency_code"],"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},"range":[0,8000]}'

response = requests.post('https://scanner.tradingview.com/america/scan',  headers=headers, data=data)

t = response.json()

df = pd.DataFrame( [n['d'] for n in t['data']])

df.columns = json.loads(data)['columns']

df.dtypes