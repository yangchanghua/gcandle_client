from gcandle.core.backtest.day_bar_backtest import DayBarBacktest
from gcandle_client.gclient_ma_cross.ma_cross import MA_CROSS_SERVICE

MA_CROSS_BACKTEST = DayBarBacktest("MA_CROSS")

if __name__ == '__main__':
    data_service = MA_CROSS_SERVICE
    start = '2020-01-01'
    end = '2020-08-30'
    codes = data_service.read_all_codes()
    data = data_service.read_with_slave_for_backtest(codes, start, end)
    MA_CROSS_BACKTEST.set_data(data)
    MA_CROSS_BACKTEST.run(2020, 2020)