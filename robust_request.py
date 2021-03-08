import time, logging

import requests


def get(*a, **kw):
  for attempt_count in range(5):
    try:
      return requests.get(*a, **kw)
    except(
      requests.exceptions.ChunkedEncodingError,
      requests.exceptions.ConnectionError,
      requests.exceptions.ConnectTimeout,
      requests.exceptions.ReadTimeout,
      requests.exceptions.TooManyRedirects,
      requests.exceptions.SSLError,
    ) as e:
      print("e: ", e)
      print("type: ", type(e))
      print("args: ", e.args)
      if hasattr(e, 'errno'):
        print("Index error({0}): {1}".format(e.errno, e.strerror))
      logging.debug(f'connection error, trying again, attempt_count: {attempt_count}')
      time.sleep(attempt_count)
