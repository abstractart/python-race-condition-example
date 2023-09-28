import threading

class Counter:
  def __init__(self):
    self.val = 0

  def change(self):
    self.val += 1

class CounterWithConversion:
  def __init__(self):
    self.val = 0

  def change(self):
    self.val += int(1)

class ThreadSafeCounter:
  def __init__(self):
    self.val = 0
    self.lock = threading.Lock()

  def change(self):
    with self.lock:
      self.val += 1

# each thread change state x times
def work(state, operationsCount):
  for _ in range(operationsCount):
      state.change()

def run_threads(state, threadsCount, operationsPerThreadCount):
  threads = []
  for _ in range(threadsCount):
    t = threading.Thread(target=work, args=(state, operationsPerThreadCount))
    t.start()
    threads.append(t)
  
  for t in threads:
    t.join()
  
if __name__ == "__main__":  
  threadsCount = 10
  operationsPerThreadCount = 100000
  expectedCounterValue = threadsCount * operationsPerThreadCount
  

  counters = [Counter(), CounterWithConversion(), ThreadSafeCounter()]
  for counter in counters:
    run_threads(counter, threadsCount, operationsPerThreadCount)
    print(f"{counter.__class__.__name__}: expected val: {expectedCounterValue}, actual val: {counter.val}")
