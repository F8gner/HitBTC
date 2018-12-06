import requests

class HitBTC:

    def Currency(currency = None):
        url = 'https://api.hitbtc.com/api/2/public/currency'
        if currency == None:
            data = requests.get(url)
            return data.json()
        else:
            url = url+'/'+currency
            data = requests.get(url)
            return data.json()

    def Symbols(symbol = None):
        url = 'https://api.hitbtc.com/api/2/public/symbol'
        if symbol == None:
            data = requests.get(url)
            return data.json()
        else:
            url = url+'/'+ symbol
            data = requests.get(url)
            return data.json()

    def Tickers(symbol = None):
        url = 'https://api.hitbtc.com/api/2/public/ticker'
        if symbol == None:
            data = requests.get(url)
            return data.json()
        else:
            url = url+'/'+ symbol
            data = requests.get(url)
            return data.json()

    def Trades(symbol):
        url = 'https://api.hitbtc.com/api/2/public/trades'
        url = url+'/'+ symbol
        data = requests.get(url)
        return data.json()

    def Orderbook(symbol):
        url = 'https://api.hitbtc.com/api/2/public/orderbook'
        url = url + '/' + symbol
        data = requests.get(url)
        return data.json()

    def Candles(symbol,period):     # periods: M3, M5, M15, M30, H1, H4, D1, D7, 1M
        url = 'https://api.hitbtc.com/api/2/public/candles'
        url = url + '/{}?period={}'.format(symbol,period)
        data = requests.get(url)
        return data.json()

    def SetAuth(public_key,secret_key):
       try:
           f_keys_w= open('hitbtc_keys.txt', "w")
           f_keys_w.write('\n'.join([public_key,secret_key]))
           f_keys_w.close()
           return 1
       except:
           return 0

    def GetAuth():
        try:
            f_keys_r = open('hitbtc_keys.txt', "r")
            data = f_keys_r.readlines()
            f_keys_r.close()
            return data[0][0:-1],data[1]
        except:
            return 0

    def TradingBalance():
        url = 'https://api.hitbtc.com/api/2/trading/balance'
        data = requests.get(url,auth=HitBTC.GetAuth())
        return data.json()

    def GetActiveOrders():
        url = 'https://api.hitbtc.com/api/2/order'
        data = requests.get(url, auth=HitBTC.GetAuth())
        return data.json()

    def GetActiveOrderByClientOrderId(clientOrderId):
        url = 'https://api.hitbtc.com/api/2/order' + clientOrderId
        data = requests.get(url, auth=HitBTC.GetAuth())
        return data.json()

    def CreateNewOrder(symbol,side,quantity,price,clientOrderId=None):
        url = 'https://api.hitbtc.com/api/2/order'
        if clientOrderId != None:
            url = url + '/' + clientOrderId
        data = requests.put\
                (url,
                data = {
                    'symbol':symbol,
                    'side':side,
                    'quantity':quantity,
                    'price':price
                },
                auth = HitBTC.GetAuth())
        return data.json()

    def CancelOrder():
        url = 'https://api.hitbtc.com/api/2/order'
        data = requests.delete(url,auth = HitBTC.GetAuth())
        return data.json()

    def CancelOrderByClientOrderId(clientOrderId):
        url = 'https://api.hitbtc.com/api/2/order/'+clientOrderId
        data = requests.delete(url,auth = HitBTC.GetAuth())
        return data.json()

    def GetTradingCommission(symbol):
        url = 'https://api.hitbtc.com/api/2/trading/fee/'+symbol
        data = requests.get(url,auth = HitBTC.GetAuth())
        return data.json()

    def OrdersHistory(symbol = None):
        url = 'https://api.hitbtc.com/api/2/history/order'
        if symbol != None:
            url = url + '?symbol=' + symbol
        data = requests.get(url, auth = HitBTC.GetAuth())
        return data.json()

    def TradesHistory(symbol = None):
        url = 'https://api.hitbtc.com/api/2/history/trades'
        if symbol != None:
            url = url + '?symbol=' + symbol
        data = requests.get(url, auth = HitBTC.GetAuth())
        return data.json()

    def TradesByOrder(orderId):
        url = 'https://api.hitbtc.com/api/2/history/order/' + orderId +'/trades'
        data =requests.get(url,auth=HitBTC.GetAuth())
        return data.json()

    def AccountBalance():
        url = 'https://api.hitbtc.com/api/2/accaunt/balance'
        data = requests.get(url, auth = HitBTC.GetAuth())
        return data.json()

    def DepositCryptoAddress(currency, method):
        url = 'https://api.hitbtc.com/api/2/account/crypto/address/'
        if currency:
            url = url + currency
            if method == 'GET':
                data = requests.get(url, auth=HitBTC.GetAuth())
                return data.json()
            elif method == 'POST':
                data = requests.post(url, auth = HitBTC.GetAuth())
                return data.json()
            else:
                return 'error'
        else:
            return 'error'

    def WithdrawCrypto(currency,amount,address,paymentId=None,networkFee=None,includeFee=False,autoCommit=True):
        url = 'https://api.hitbtc.com/api/2/account/crypto/withdraw'
        data = requests.post\
        (
            url,
            json={
                'currency':currency,
                'amount':amount,
                'address':address,
                'paymentId':paymentId,
                'networkFee':networkFee,
                'includeFee':includeFee,
                'autoCommit':autoCommit
            },
            auth = HitBTC.GetAuth()
        )
        return data.json()

    def WithdrawCryptoCommitOrRollback(id, method):
        url = 'https://api.hitbtc.com/api/2/account/crypto/withdraw/'
        url = url + id
        if method == 'Commit':
            data = requests.put(url,auth = HitBTC.GetAuth())
            return data.json()
        elif method == 'Rollback':
            data = requests.delete(url,auth = HitBTC.GetAuth())
            return data.json()
        else:
            return 'error'

    def TransferMoneyBetweenTradingAndAccount(currency, amount, type):
        url = 'https://api.hitbtc.com/api/2/account/transfer'
        if type == 'bankToExchange' or type == 'exchangeToBank':
            data = requests.post\
                (
                    url,
                    json={
                        'currency':currency,
                        'amount':amount,
                        'type':type
                    },
                    auth = HitBTC.GetAuth()
                )
            return data.json()
        else:
            return 'error'

    def GetTransactionsHistory(Currency, From, Till, Offset, Sort = 'DESC', By = 'timestamp', Limit = 100, Id = None):
        url = 'https://api.hitbtc.com/api/2/account/transactions'
        if Id != None:
            url = url + '/' + Id
        if Sort == 'DESC' or Sort == 'ASC':
            data = requests.get\
                (
                    url,
                    params={
                        'currency':Currency,
                        'sort':Sort,
                        'by':By,
                        'from':From,
                        'till':Till,
                        'limit':Limit,
                        'offset':Offset
                    },
                    auth = HitBTC.GetAuth()
                )
            return data.json()