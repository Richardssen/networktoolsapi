import os
import logging

LOG_LEVEL = logging.DEBUG

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')

CITY_MMDB_LOCATION = os.path.join(APP_STATIC, 'data/GeoIPCity.dat')
ISP_MMDB_LOCATION = os.path.join(APP_STATIC, 'data/GeoIPISP.dat')

ALLOWED_IPS = []
LIMITER_GLOBAL_LIMITS = ["10000 per second"]

DEFAULT_NAMESERVERS = ['8.8.8.8', '8.8.4.4']