import logging, time

import requests


class Requester:
  def __init__(self, logger):
    self.session = requests.session()
    self.session.headers.update({'User-Agent':
      (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/61.0.3163.100 Safari/537.36'
      )
    })

    self.logger = logger
    self.failure_count = 0

  def json(self, url):
    try:
      return self.get(url).json()
    except json.decoder.JSONDecodeError:
      return None
    except:
      self.failure_count += 1
      if self.failure_count > 10:
        self.logger.error('failed too many times, giving up')
        raise

  def get(self, *a, **kw):
    for attempt_count in range(5):
      try:
        return self.session.get(*a, **kw)
      except(
        requests.exceptions.ChunkedEncodingError,
        requests.exceptions.ConnectionError,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        requests.exceptions.TooManyRedirects,
        requests.exceptions.SSLError,
      ) as e:
        self.logger.error("e: ", e)
        self.logger.error("type: ", type(e))
        self.logger.error("args: ", e.args)
        if hasattr(e, 'errno'):
          self.logger.error("Index error({0}): {1}".format(e.errno, e.strerror))
        self.logger.debug(f'connection error, trying again, attempt_count: {attempt_count}')
        time.sleep(attempt_count)


def test():
  url = 'https://jsonplaceholder.typicode.com/todos/1'
  requester = Requester(logger=logging.getLogger())
  resp_dict = requester.json(url)
  print('resp_dict:', resp_dict)

if __name__ == '__main__':
  test()
