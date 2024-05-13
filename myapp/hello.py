import fire

def hello(name="World"):
  print("in develop branch")
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
