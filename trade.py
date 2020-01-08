class Stock():
	def __init__(self, price_buy, price_sell, qty, fee_rate = 0.025 / 100):
		self.price_buy = price_buy
		self.price_sell = price_sell
		self.qty = qty
		self.fee_rate = fee_rate

		fee_buy = self.price_buy * self.qty * self.fee_rate
		fee_sell = self.price_sell * self.qty * self.fee_rate
		self.fee = fee_buy + fee_sell
		
		self.profit = ( self.price_sell - self.price_buy ) * self.qty - self.fee
		self.prc = ( self.price_sell - self.price_buy ) / self.price_buy * 100

		print("\tprofit = {0}\n\tfee = {1}\n\t% = {2}".format(self.profit, self.fee, self.prc))

# AMD = Stock(48.4, 48.8, 215)
# TCS = Stock(21.3, 21.35, 100)
Amazon = Stock(1903.39, 1906, 20)