import os
class cmd:
  def __init__(self,comm):
      self.commend=comm
  def exec(self):
      result = os.popen(self.commend)
      results = result.readlines()
      return results
