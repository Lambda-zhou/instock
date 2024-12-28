#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import logging
import os.path
import sys

cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current, os.pardir))
sys.path.append(cpath)
import instock.lib.run_template as runt
import instock.core.tablestructure as tbs
import instock.core.stockfetch as stf
import data_fetcher
import push



# 每日股票大宗交易
def save_after_close_stock_blocktrade_data(date):
    try:
        data = stf.fetch_stock_blocktrade_data(date)
        if data is None or len(data.index) == 0:
            return

        push.strategy(f"Blocktrade data for {date}: {data}")
    except Exception as e:
        logging.error(f"basic_data_other_daily_job.save_stock_blocktrade_data处理异常：{e}")


def main():
    runt.run_with_args(save_after_close_stock_blocktrade_data)


# main函数入口
if __name__ == '__main__':
    main()
