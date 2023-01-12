

import art
import random
cards = ["2", "3", "4", "5", "6", "7","8","9","10","Jack","Queen","King","Ace"]
#everything above is the cards; will have to edit Ace
count = {"2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11}
#this is the logic for the blackjack game
# this is logic for dealer hit
# This is first round

end_game = False
hit = False
print(art.logo)
restart = "n"
while end_game == False:
  restart = "n"
  p_count = 0
  d_count = 0
  extend_num = []
  random_choice1 = random.randint(0, len(cards))
  random_choice2 = random.randint(0, len(cards))
  random_choice3 = random.randint(0, len(cards))
  #this is players hand
  p_card_1= cards[random_choice1-1]
  p_card_2= cards[random_choice2-1]
  p_hand = [p_card_1,p_card_2]
  print(f"Your hand is {p_hand}")
  for key in p_hand:
    p_count += count[key]
  if p_count > 21 and p_hand[-1] == "Ace":
    p_count - 10
  elif p_count == 21:
    print(f"You win with a perfect hand of {p_count}!")
    end = input("Would you like to continue? Y for yes or N for no.").lower()
    if end == "n":
      end_game = True
      break
  print(p_count)
  #this is dealers hand
  d_card_1= cards[random_choice3-1]
  d_hand1 = [d_card_1]
  print(f"Dealers hand is {d_hand1}")
  for key in d_hand1:
    d_count += count[key]
  print(d_count)
  fork = input("Would you like to stay or hit? Y for hit, N for stay").lower()
  #player choice
  while fork == "y" and restart == "n":
    random_choice5 = random.randint(0, len(cards))
    p_card_3 = cards[random_choice5-1]
    print(f"You pull a {p_card_3}")
    p_hand.append(p_card_3)
    p_hand[-1] = count[p_hand[-1]]
    p_count += p_hand[-1]
    print(p_count)
    if p_count > 21 and p_hand[-1]==1:
      p_hand[-1] == 1
    elif p_count > 21:
      print(f"You bust with a {p_count}. Dealer wins.")
      end = input("Would you like to continue? Y for yes or N for no.").lower()
      if end == "n":
        end_game = True
        break
      elif end == "y":
        end_of_game = False
        restart = "y"
    elif p_count == 21:
      print(f"You win with a perfect hand of {p_count}")
      end = input("Would you like to continue? Y for yes or N for no.").lower()
      if end == "n":
        end_game = True
        break
    else:
      fork = input("Would you like to stay or hit? Y for hit, N for stay").lower()
  

  #this if you stay
  if fork == "n":
    while d_count > p_count:
      random_choice4 = random.randint(0, len(cards))
      extend_num.append(random_choice4)
      d_card_2 = cards[random_choice4-1]
      print(f"Dealer pulls a {d_card_2}")
      d_hand1.append(d_card_2)
      d_hand1[-1] = count[d_hand1[-1]]
      d_count += d_hand1[-1]
      print(d_count)
    while d_count < p_count:
      random_choice4 = random.randint(0, len(cards))
      extend_num.append(random_choice4)
      d_card_2 = cards[random_choice4-1]
      print(f"Dealer pulls a {d_card_2}")
      d_hand1.append(d_card_2)
      d_hand1[-1] = count[d_hand1[-1]]
      d_count += d_hand1[-1]
      print(d_count)
      if d_count > 21 and d_hand1[-1] == 11:
        d_hand1[-1] = 1
      if d_count > 21:
        print("Dealer busts, you win!")
        end = input("Would you like to continue? Y for yes or N for no.").lower()
        if end == "n":
          end_game = True
          break
      elif d_count == 21:
        print("The dealer wins with a perfect hand of 21")
        end = input("Would you like to continue? Y for yes or N for no.").lower()
        if end == "n":
          end_game = True
          break
      elif d_count > p_count:
        print(f"Dealer wins with a count of {d_count} over your {p_count}")
        end = input("Would you like to continue? Y for yes or N for no.").lower()
        if end == "n":
          end_game = True
          break
      elif d_count == p_count:
        print(f"Dealer wins because of a tie. Your number was {p_count} and theirs was {d_count}")
        end = input("Would you like to continue? Y for yes or N for no.").lower()
        if end == "n":
          end_game = True
          break
      else:
        while d_count> p_count:
          random_choice4 = random.randint(0, len(cards))
          extend_num.append(random_choice4)
          d_card_2 = cards[random_choice4-1]
          print(f"Dealer pulls a {d_card_2}")
          d_hand1.append(d_card_2)
          d_hand1[-1] = count[d_hand1[-1]]
          d_count += d_hand1[-1]
  
print("Thank you for trying out our BlackJack game!")