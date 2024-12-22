def my_decorator(func):
  def wrapper(*args, **kwargs):
    print("Перед виконанням функції")
    result = func(*args, **kwargs)
    print("Після виконання функції")
    return result

  return wrapper


@my_decorator
def my_function():
  print("Основна функція")


my_function()
