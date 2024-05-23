from time import sleep

def reverse(time_number):
  if time_number <= 0:
    return
  sleep(0.6)
  print(time_number)
  time_number -= 1
  reverse(time_number)


reverse(20)