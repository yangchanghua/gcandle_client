from gcandle.data.QfqTransformer import update_stock_qfq_data, recreate_stock_qfq_data
from gcandle.data.se_types import SeType, SeFreq
from gcandle.objects.data_service_objects import TDX_SECURITY_DATA_UPDATE_SERVICE
from gcandle.utils.date_time_utils import Date
from gcandle.utils.gcandle_config import GCANDLE_CONFIG


def fetch_and_update_by_tdx():
    dataService = TDX_SECURITY_DATA_UPDATE_SERVICE
    GCANDLE_CONFIG.set_mongodb_uri('mongodb://localhost:27017')
    GCANDLE_CONFIG.set_mongodb_name('gcandle')
    a = Date()
    dataService.update_code_list()
    dataService.update_bars(typ=SeType.Index, freq=SeFreq.DAY, days_to_update=500)
    dataService.update_bars(typ=SeType.Stock, freq=SeFreq.DAY, days_to_update=500)
    codes = dataService.read_security_codes(typ=SeType.Stock)
    dataService.refetch_and_save_xdxr(codes)
    # update_stock_qfq_data()
    recreate_stock_qfq_data()
    b = Date()
    print("time used: {} seconds".format(b.delta_to(a).seconds))


if __name__ == '__main__':
    fetch_and_update_by_tdx()