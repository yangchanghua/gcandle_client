from gcandle.data.se_types import SeType, SeFreq
from gcandle.objects.data_service_objects import TDX_SECURITY_DATA_UPDATE_SERVICE
from gcandle.data.SecurityDataUpdateMonitor import SecurityDataUpdateMonitor
from gcandle.utils.gcandle_config import GCANDLE_CONFIG
from gcandle.utils.date_time_utils import Date
import time


def fetch_and_update_by_tdx():
    dataService = TDX_SECURITY_DATA_UPDATE_SERVICE
    GCANDLE_CONFIG.set_mongodb_uri("'mongodb://localhost:27017'")
    GCANDLE_CONFIG.set_mongodb_name("my_gcandle_db")
    a = Date()
    dataService.update_code_list()
    dataService.update_bars(typ=SeType.Stock, freq=SeFreq.DAY)
    b = Date()
    print("time used: {} seconds".format(b.delta_to(a).seconds))


if __name__ == '__main__':
    fetch_and_update_by_tdx()