from gcandle.core.buy_strategy.BuyStrategy import BuyStrategy
from gcandle_client.gclient_ma_cross_enhanced.ma_cross_enhanced import NAME


buy_key = 'after_jc_buy'
MAX_JC_A_BUY = 5


class MajcEnhancedBuy(BuyStrategy):
    def __init__(self, train=True):
        super().__init__('majc enhanced')

    def update_buy_prices(self, data):
        data['bpr'] = data.pre_jc_c * 0.97

    def get_buy_filter_before_buy_day(self, data):
        f = (data[buy_key] == True)
        f &= (data.jcA >= 4) & ((data.jcA <= 5))
        f &= (data.jc_after_l / data.pre_jc_c > 0.97)
        return f

    def get_final_buy_filter_on_buy_day(self, data):
        f = self.get_buy_filter_before_buy_day(data)
        f &= (data.low < data.bpr)
        return f

    def calc_and_forward_fill_buy_filter(self, data, extra=True):
        def _fill(data):
            data[buy_key] = data[buy_key].shift(1)
            data[buy_key] = data[buy_key].fillna(method='ffill', limit=MAX_JC_A_BUY)
            return data

        data.loc[data[NAME] == True, buy_key] = True
        data = data.groupby(level=1).apply(_fill).sort_index(level=0)
        return data

    def get_price_func(self):
        return lambda x: min(x.bpr, x.open)
