import random

print ("Heads or Tails\n")

heads = 0
tails = 0
count = 0

# Main Loop
while count <= 9999:
  coinflip = random.randint(1,2)
  if coinflip == 1:
    heads += 1
    count += 1
  else:
    tails += 1
    count += 1

  print ("%s heads, %s tails, %s flips" % (heads, tails, count))

