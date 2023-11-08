def plus(a,b):
  try:
    result = a + b
    return result
  except:
    print(f"더하기 에러 발생")
    return None

def minus(a,b):
  try:
    result = a - b
    return result
  except:
    print(f"빼기 에러 발생")
    return None

def multi(a,b):
  try:
    result = a * b
    return result
  except:
    print(f"곱하기 에러 발생")
    return None
