api_key_alphavantage = "BCM1SKF4S8DJBAPU"
api_key_news = "dd2b2952feff4f4b84b2f8c7513cef3a"

from datetime import datetime, timedelta


def yesterday(frmt='%Y-%m-%d', string=True):
    yesterday = datetime.now() - timedelta(1)
    if string:
        return yesterday.strftime(frmt)
    return yesterday

print(yesterday())