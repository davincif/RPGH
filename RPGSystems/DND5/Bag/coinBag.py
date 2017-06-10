#Standard Python Imports
#

#Internal Imports
#


coin_exchange = {
				"platinum":
					{"copper": 1000,
					"silver": 100,
					"electrum": 20,
					"gold": 10,
					"platinum": 1
					},
				"gold":
					{"copper": 100,
					"silver": 10,
					"electrum": 2,
					"gold": 1,
					"platinum": 1/10
					},
				"electrum":
					{"copper": 50,
					"silver": 5,
					"electrum": 1,
					"gold": 1/2,
					"platinum": 1/20
					},
				"silver":
					{"copper": 10,
					"silver": 1,
					"electrum": 1/5,
					"gold": 1/10,
					"platinum": 1/100
					},
				"copper":
					{"copper": 1,
					"silver": 1/10,
					"electrum": 1/50,
					"gold": 1/100,
					"platinum": 1/1000
					}
				}


class CoinBag:
	platinum = 0
	gold = 0
	electrum = 0
	silver = 0
	copper = 0

	def __init__(self):
		pass
