from binance.client import Client
import pandas as pd

api = 'a2dcf00179c63784ae76cb7b4b3767c13564d13b45fa3f99aeaba8050d5c9710'
api_secret = '63229ef2e854e801340883d0653e4f889f8d9f64517cec91ced468a30e769cdb'

client = Client(api, api_secret, tld='com', testnet=True)

def get_balance():
    x = client.futures_account()
    df = pd.DataFrame(x['assets'])
    print(df)

client.futures_create_order(
    symbol='BTCUSDT',
    side = Client.SIDE_SELL,
    type = Client.FUTURE_ORDER_TYPE_LIMIT,
    timeInForce = Client.TIME_IN_FORCE_GTC,
    quantity = 0.01,
    price = 50000,
)

