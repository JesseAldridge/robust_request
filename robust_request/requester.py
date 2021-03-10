import logging

import requests


class Requester:
  def __init__(self, logger):
    self.logger = logger
    self.failure_count = 0

  def json(self, url, session):
    try:
      return session.get(url).json()
    except json.decoder.JSONDecodeError:
      return None
    except:
      self.failure_count += 1
      if self.failure_count > 10:
        self.logger.error('failed too many times, giving up')
        raise

def test():
  url = 'https://jsonplaceholder.typicode.com/todos/1'
  session = requests.session()
  requester = Requester(logger=logging.getLogger())
  resp_dict = requester.json(url, session)
  print('resp_dict:', resp_dict)

if __name__ == '__main__':
  test()
