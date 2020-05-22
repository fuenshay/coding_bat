def parrot_trouble(talking, hour):
  return(talking and (hour < 7 or hour > 20))


# def parrot_trouble(talking, hour):
#   if talking and hour < 7 or hour > 20:
#     return True
#   if talking and hour > 7 or hour < 20:
#     return False
#   return True
