from gcandle.core.indicator_service.master_indicator_service import MasterIndicatorService

NAME = "MA_CROSS"


def calc_ma_cross(data):
    data['pc'] = data.close.shift(1)
    data['ma_20'] = data.close.rolling(20).mean()
    data['ma_60'] = data.close.rolling(60).mean()
    data['ma_jc'] = (data.ma_20 > data.ma_60) & (data.ma_20.shift(1) < data.ma_60.shift(1))
    data['ma_sc'] = (data.ma_20 < data.ma_60) & (data.ma_20.shift(1) > data.ma_60.shift(1))
    ma_cross_rows = (data.ma_jc == True) | (data.ma_sc == True)
    if len(data.loc[ma_cross_rows]) > 0:
        data.loc[ma_cross_rows, NAME] = True
        return data.loc[ma_cross_rows]
    else:
        return None


MA_CROSS_SERVICE = MasterIndicatorService(NAME, calc_ma_cross)


if __name__ == '__main__':
    start = '2020-01-01'
    end = '2020-12-31'
    MA_CROSS_SERVICE.recreate_for_all_codes(start, end)

