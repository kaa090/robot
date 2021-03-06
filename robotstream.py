from openapi_client.openapi_streaming import run_stream_consumer
from openapi_client.openapi_streaming import print_event

tokenSand = "t.rscm7UMilR-xubG0ZXfkhpZbG3Yc3_aCsO37G6PDqUM_L0XMI9XSdbrUB_3UzkWS3LUrUrZfGE_lwHBuARBK9Q"
token = tokenSand

candle_subs = [{'figi': 'BBG000B9XRY4', 'interval': '1min'}, {'figi': 'BBG009S39JX6', 'interval': '1min'}]
orderbook_subs = [{'figi': 'BBG0013HGFT4', 'depth': 1}, {'figi': 'BBG009S39JX6', 'depth': 3}]
instrument_info_subs = [{'figi': 'BBG000B9XRY4'}, {'figi': 'BBG009S39JX6'}]

run_stream_consumer(token,
                    candle_subs, orderbook_subs, instrument_info_subs,
                    on_candle_event=print_event,
                    on_orderbook_event=print_event,
                    on_instrument_info_event=print_event)