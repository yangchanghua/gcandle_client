from gcandle.core.buy_strategy.BuyStrategy import BuyStrategy


class MaCrossBuy(BuyStrategy):
    def __init__(self):
        super().__init__('ma cross')

    def update_buy_prices(self, data):
        pass

    def get_buy_filter_before_buy_day(self, data):
        return True

    def get_final_buy_filter_on_buy_day(self, data):
        return data.ma_jc == True

    def calc_and_forward_fill_buy_filter(self, data, extra=True):
        return data

    def get_price_func(self):
        return lambda x: x.close
