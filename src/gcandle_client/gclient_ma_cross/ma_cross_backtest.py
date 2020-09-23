from gcandle.core.backtest.day_bar_backtest import DayBarBacktest
from gcandle.core.buy_strategy import BuyStrategy
from gcandle.core.sell_strategy.CombinedSellStrategy import CombinedSellStrategy
from gcandle.core.sell_strategy.SellAtCloseStrategy import SellAtCloseStrategy
from gcandle_client.gclient_ma_cross.ma_cross import MA_CROSS_SERVICE
from gcandle_client.gclient_ma_cross.ma_cross_buy import MaCrossBuy


MY_BUY_STRATEGY = MaCrossBuy()


MY_SELL_STRATEGY = CombinedSellStrategy("ma cross").append(
    SellAtCloseStrategy('at close').clear_exclude_rules().clear_extra_rules()
)


MA_CROSS_BACKTEST = DayBarBacktest("MA_CROSS")


if __name__ == '__main__':
    data_service = MA_CROSS_SERVICE
    start = '2020-01-01'
    end = '2020-08-30'
    codes = data_service.read_all_codes()
    data = data_service.read_with_slave_for_backtest(codes, start, end)
    MA_CROSS_BACKTEST.set_data(data)
    MA_CROSS_BACKTEST.set_buy_strategy(MY_BUY_STRATEGY)
    MA_CROSS_BACKTEST.set_sell_strategy(MY_SELL_STRATEGY)
    MA_CROSS_BACKTEST.run(2020, 2020)