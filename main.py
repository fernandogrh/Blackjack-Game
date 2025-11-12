import random

def deal_a_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Check for a Blackjack (Ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # If the hand has an Ace (11) and the total is over 21, change it to 1
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw 🤝"
    elif computer_score == 0:
        return "You lose, dealer has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over 21. You lose 💀"
    elif computer_score > 21:
        return "Dealer went over 21. You win 🥳"
    elif user_score > computer_score:
        return "You win! 🎉"
    else:
        return "You lose!😤"

def play_game():
    user_cards = []
    computer_cards = []
    game_over = False

    for x in range(2):
        user_cards.append(deal_a_card())
        computer_cards.append(deal_a_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            try:
                user_choice = input("Type 'yes' to get another card or 'no' to pass: ").strip().lower()
                if user_choice == "yes":
                    user_cards.append(deal_a_card())
                elif user_choice == "no":
                    game_over = True
                else:
                    print("Please type only 'yes' or 'no'.")
            except ValueError:
                print("Please just enter 'yes' or 'no'")
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_a_card())
        computer_score = calculate_score(computer_cards)

    print("\n--- Final Results ---")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Game loop
print("==============================================")
print("        🃏SIMPLE BLACKJACK by Fernando Ramirez 🃏       ")
print("==============================================")

while True:
    try:
        play = input("Do you want to play a game of Blackjack\nPlease type in 'yes' if you do or 'no' if you do not: ").strip().lower()
        if play == "yes":
            print("\n" * 1)
            play_game()
        elif play == "no":
            print("Come back soon! Bye! 👋")
            break
        else:
            print("Please type only 'yes' or 'no'")
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye! 👋")
        break
    except ValueError:
        print("Please type only 'yes' or 'no'")
    except Exception as e:
        print(f"Unexpected error: {e}")
        break

