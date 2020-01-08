from openapi_client import openapi
from datetime import datetime, timedelta
from pytz import timezone

tokenSand = "t.rscm7UMilR-xubG0ZXfkhpZbG3Yc3_aCsO37G6PDqUM_L0XMI9XSdbrUB_3UzkWS3LUrUrZfGE_lwHBuARBK9Q"
token = tokenProd
figiAMZN = 'BBG000BVPV84'

client = openapi.api_client(token)
now = datetime.now(tz=timezone('Europe/Moscow'))
yesterday = now - timedelta(days=1)

# order_response = client.market.market_candles_get(figi=figiAMZN,
#                                                   _from=yesterday.isoformat(),
#                                                   to=now.isoformat(),
#                                                   interval='30min')
# print(order_response.payload.candles[0].h)

# order_response = client.operations.operations_get(_from=yesterday.isoformat(),
#                                                   to=now.isoformat())
# print(order_response)

# order_response = client.orders.orders_limit_order_post(figi=figiAMZN,
#                                                        limit_order_request={"lots": 1,
#                                                                             "operation": "Buy",
#                                                                             "price": 1845})
# print(order_response)

print(client.portfolio.portfolio_get())