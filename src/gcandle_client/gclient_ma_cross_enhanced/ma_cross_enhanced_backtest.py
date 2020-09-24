from gcandle.core.backtest.day_bar_backtest import DayBarBacktest
from gcandle.core.buy_strategy.BuyStrategy import BuyStrategy
from gcandle.core.sell_strategy.CombinedSellStrategy import CombinedSellStrategy
from gcandle.core.sell_strategy.SellAtCloseStrategy import SellAtCloseStrategy
from gcandle.core.sell_strategy.TargetPriceSellStrategy import TargetPriceSellStrategy

from gcandle_client.gclient_ma_cross_enhanced.ma_cross_enhanced import MAJC_ENHANCED_SERVICE
from gcandle_client.gclient_ma_cross_enhanced.majc_enhanced_buy import MajcEnhancedBuy


MY_BUY_STRATEGY = MajcEnhancedBuy()


MY_SELL_STRATEGY = CombinedSellStrategy("ma cross").append(
    TargetPriceSellStrategy().set_higher_than_bpr(1.2).set_hold_range(1, 2)
).append(
    SellAtCloseStrategy("totalLoss").set_hold_range(1, 2).add_extra_filter(
        lambda data: (data.close / data.bpr < 0.95)
    )
).append(
    SellAtCloseStrategy('AtClose').set_hold_range(2, 3)
).append(
    SellAtCloseStrategy('MaxDays').clear_exclude_rules().clear_extra_rules().set_hold_range(3)
)



MA_CROSS_BACKTEST = DayBarBacktest("MA_CROSS")


if __name__ == '__main__':
    data_service = MAJC_ENHANCED_SERVICE
    start = '2018-01-01'
    end = '2020-08-30'
    codes = data_service.read_all_codes()
    data = data_service.read_with_slave_for_backtest(codes, start, end)
    MA_CROSS_BACKTEST.set_data(data)
    MA_CROSS_BACKTEST.set_buy_strategy(MY_BUY_STRATEGY)
    MA_CROSS_BACKTEST.set_sell_strategy(MY_SELL_STRATEGY)
    MA_CROSS_BACKTEST.run(2020, 2020)