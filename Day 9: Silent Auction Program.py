print("Welcome to the Silent Auction Program!")


def bids_submitted(name, bid):
  bids_record = {}
  bids_record[name] = bid


def highest_bid(name, bid):
  highest_bid = 0
  if bid > highest_bid:
    highest_bid = bid
  print(f"{name} won with a bid of ${bid}.")


start_again = True
while start_again:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: "))

  bids_submitted(name, bid)

  other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

  if other_bidder == "yes":
    start_again = True

  elif other_bidder == "no":
    start_again = False
    highest_bid(name, bid)

