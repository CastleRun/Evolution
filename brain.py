class Axon(object):
  def __init__(self, n, w, t):
    self.n = n
    self.w = w
    self.t = t
  
  def send(self, s):
    return (n, s * w if s * w > t else 0)
