import json

import requests


class Handle_Api:

    def __init__(self):
        # 实例化session对象
        self.session = requests.Session()



    def api(self, method, url, data=None, headers=None, **kwargs):
        if method.upper() == "GET":
            res = self.session.get(url=url, params=data, **kwargs)
        elif method.upper() == "POST":
            res = self.session.request(method=method, url=url, data=data, headers=headers, **kwargs)
        else:
            res = None
            print("并不支持该请求方法，请检查之后，重新请求")
        return res
if __name__ == '__main__':
    # url = 'http://127.0.0.1/index.php?m=Home&c=Goods&a=dispatching'
    url = 'http://127.0.0.1/index.php?m=Home&c=Cart&a=add'

    headers = {
        # "Content-Type": "application/x-www-form-urlencoded",
        # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "Cookie":"PHPSESSID=rtjdtgt5na5e041194aoffl7d4; province_id=1; city_id=2; district_id=3; parent_region=%5B%7B%22id%22%3A3%2C%22name%22%3A%22%u4E1C%u57CE%u533A%22%7D%2C%7B%22id%22%3A14%2C%22name%22%3A%22%u897F%u57CE%u533A%22%7D%2C%7B%22id%22%3A22%2C%22name%22%3A%22%u5D07%u6587%u533A%22%7D%2C%7B%22id%22%3A30%2C%22name%22%3A%22%u5BA3%u6B66%u533A%22%7D%2C%7B%22id%22%3A39%2C%22name%22%3A%22%u671D%u9633%u533A%22%7D%2C%7B%22id%22%3A83%2C%22name%22%3A%22%u4E30%u53F0%u533A%22%7D%2C%7B%22id%22%3A105%2C%22name%22%3A%22%u77F3%u666F%u5C71%u533A%22%7D%2C%7B%22id%22%3A115%2C%22name%22%3A%22%u6D77%u6DC0%u533A%22%7D%2C%7B%22id%22%3A145%2C%22name%22%3A%22%u95E8%u5934%u6C9F%u533A%22%7D%2C%7B%22id%22%3A159%2C%22name%22%3A%22%u623F%u5C71%u533A%22%7D%2C%7B%22id%22%3A188%2C%22name%22%3A%22%u901A%u5DDE%u533A%22%7D%2C%7B%22id%22%3A204%2C%22name%22%3A%22%u987A%u4E49%u533A%22%7D%2C%7B%22id%22%3A227%2C%22name%22%3A%22%u660C%u5E73%u533A%22%7D%2C%7B%22id%22%3A245%2C%22name%22%3A%22%u5927%u5174%u533A%22%7D%2C%7B%22id%22%3A264%2C%22name%22%3A%22%u6000%u67D4%u533A%22%7D%2C%7B%22id%22%3A281%2C%22name%22%3A%22%u5E73%u8C37%u533A%22%7D%5D; is_mobile=0; CNZZDATA009=30037667-1536735; user_id=8; is_distribut=1; uname=%25E7%258E%258B%25E7%2584%25B6%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A%25E5%2595%258A; cn=2"
    }

    data = {
        "goods_id": "1",
        "spec_goods_price": '%5B%7B%22item_id%22%3A274%2C%22goods_id%22%3A1%2C%22key%22%3A%229_11_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu7ea2%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2276.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A81%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%228999999%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A275%2C%22goods_id%22%3A1%2C%22key%22%3A%229_12_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu94c2%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2256.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A67%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%228999997%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A276%2C%22goods_id%22%3A1%2C%22key%22%3A%229_13_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu6781%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2298.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A90%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A277%2C%22goods_id%22%3A1%2C%22key%22%3A%229_11_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu7ea2%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2278.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A57%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A278%2C%22goods_id%22%3A1%2C%22key%22%3A%229_12_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu94c2%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2297.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A85%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A279%2C%22goods_id%22%3A1%2C%22key%22%3A%229_13_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a3G%2B32G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu6781%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2267.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A68%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A280%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_11_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu7ea2%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2295.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A79%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A281%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_12_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu94c2%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2299.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A78%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A282%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_13_16%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu6781%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e00%22%2C%22price%22%3A%2267.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A96%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A283%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_11_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu7ea2%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2281.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A78%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A284%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_12_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu94c2%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2269.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A67%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%2C%7B%22item_id%22%3A285%2C%22goods_id%22%3A1%2C%22key%22%3A%2210_13_17%22%2C%22key_name%22%3A%22%5Cu9009%5Cu62e9%5Cu7248%5Cu672c%3A%5Cu5168%5Cu7f51%5Cu901a4G%2B64G+%5Cu9009%5Cu62e9%5Cu989c%5Cu8272%3A%5Cu6781%5Cu5149%5Cu8272+%5Cu5957%5Cu9910%5Cu7c7b%5Cu578b%3A%5Cu5957%5Cu9910%5Cu4e8c%22%2C%22price%22%3A%2285.00%22%2C%22cost_price%22%3A%220.00%22%2C%22commission%22%3A%220.00%22%2C%22store_count%22%3A86%2C%22bar_code%22%3A%22%22%2C%22sku%22%3A%22%22%2C%22spec_img%22%3A%22%22%2C%22prom_id%22%3A0%2C%22prom_type%22%3A0%7D%5D',
        "goods_prom_type": "0",
        "prom_id": "0",
        "shop_price":"56.00",
        "store_count":"67",
        "market_price":"3198.00",
        "start_time":"",
        "end_time":"",
        "activity_title":"",
        "prom_detail":"",
        "activity_is_on":"0",
        "item_id":"275",
        "exchange_integral":"0",
        "point_rate":"10",
        "is_virtual":"0",
        "virtual_limit":"0",
        "deposit_price":"",
        "balance_price":"",
        "ing_amount":"",
        "goods_spec%5B%E9%80%89%E6%8B%A9%E7%89%88%E6%9C%AC%5D":"9",
        "goods_spec%5B%E9%80%89%E6%8B%A9%E9%A2%9C%E8%89%B2%5D":"12",
        "goods_spec%5B%E5%A5%97%E9%A4%90%E7%B1%BB%E5%9E%8B%5D":"16",
        "goods_num":"1"
    }
    res = Handle_Api().api('post', url=url,data=data, headers=headers)
    print(res.json())