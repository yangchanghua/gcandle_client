from gcandle.data.tdx.update_tdx import fetch_and_update_by_tdx
from gcandle.data.QfqTransformer import update_stock_qfq_data
from gcandle.indicator.day_fp_marks import update_all_foot_peak_marks
from gcandle.utils.date_time_utils import Date

##########################
##Update internal data for strategy
##########################
def update_indicators():
    a = Date()
    fetch_and_update_by_tdx()
    update_stock_qfq_data()
    update_all_foot_peak_marks()
    b = Date()
    print('Time used: {} seconds'.format(b.delta_to(a).seconds))

if __name__ == '__main__':
    update_indicators()
