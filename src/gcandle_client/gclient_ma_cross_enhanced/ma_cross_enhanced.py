from gcandle.core.indicator_service.master_indicator_service import MasterIndicatorService
import numpy as np


NAME = "MA_JC"
DAYS_AFTER_JC = 10
MAX_JC_A_BUY = 3


def calc_ma_cross(data):
    data['pc'] = data.close.shift(1)
    data['ma_20'] = data.close.rolling(20).mean()
    data['ma_60'] = data.close.rolling(60).mean()
    data[NAME] = (data.ma_20 > data.ma_60) & (data.ma_20.shift(1) < data.ma_60.shift(1))

    data['day_idx'] = range(len(data))
    data['nearMAJC'] = np.nan
    data['jcA'] = np.nan
    if data.loc[data[NAME] == True].shape[0] < 1:
        return None

    data.loc[data[NAME].shift(1) == True, 'prev_jc_idx'] = data['day_idx'].shift(1)
    data['prev_jc_idx'] = data['prev_jc_idx'].fillna(method='ffill', limit=DAYS_AFTER_JC)
    data['jcA'] = data.day_idx - data.prev_jc_idx
    data.loc[(data.jcA > 0) | (data[NAME] == True), 'nearMAJC'] = True
    features_around_jc(data)
    data = data.dropna(subset=['nearMAJC']).copy()
    if data is None or len(data) < 1:
        return None
    cols_to_drop = ['amount',
                    'day_idx', 'prev_jc_idx']
    data = data.drop(columns=cols_to_drop)
    return data


def features_around_jc(data):
    on_jc = data[NAME] == True
    if len(data.loc[on_jc]) > 0:
        data.loc[on_jc, 'pre_jc_c'] = data.close
        data.loc[on_jc, 'pre_jc_h'] = data.high
    else:
        return

    for n in range(1, MAX_JC_A_BUY + 1):
        jcA_rows = data.jcA == n
        if len(data.loc[jcA_rows]) > 0:
            data.loc[jcA_rows, 'jc_after_h'] = data.high.rolling(n).max()
            data.loc[jcA_rows, 'jc_after_l'] = data.low.rolling(n).min()

    shift_jc_features(data)
    forward_fill_cols(data)


PRE_JC_COLS = ['pre_jc_c', 'pre_jc_h']
AFTER_PRE_JC_COLS = ['jc_after_h', 'jc_after_l']


def shift_jc_features(data):
    cols_to_shift = PRE_JC_COLS + AFTER_PRE_JC_COLS
    data[cols_to_shift] = data[cols_to_shift].shift(1)


def forward_fill_cols(data):
    cols_to_ffill = PRE_JC_COLS
    data[cols_to_ffill] = data[cols_to_ffill].fillna(method='ffill')


MAJC_ENHANCED_SERVICE = MasterIndicatorService(NAME, calc_ma_cross)


if __name__ == '__main__':
    start = '2018-01-01'
    end = '2020-12-31'
    MAJC_ENHANCED_SERVICE.recreate_for_all_codes(start, end)

