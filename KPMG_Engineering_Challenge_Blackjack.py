import random
import time

class BlackJackGame:
	def __init__(self):
		self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4
		random.shuffle(self.deck)
		self.hand = []
		self.own_score = 0
		self.dealer_hand = []
		self.dealer_score = 0

	def game(self):
		print("Let's play Blackjack!")
		self.deal(self.hand)
		self.deal(self.dealer_hand)
		self.player_round()
		self.dealer_round()
		self.final_eval()
		self.play_again()

	def deal(self, hand):
		for i in range(2):
			card = self.deck.pop()
			hand.append(card)

	def player_round(self):
		ans = '1'
		while ans == '1':
			self.own_score = self.score(self.hand)
			print('\n')
			print("Your cards: " + str(self.hand))
			print("Total = " + str(self.own_score))
			if self.own_score > 21:
				self.bust()
			print("Dealer's cards: [" +  str(self.dealer_hand[0]) + ", *]\n")
			
			ans = input("Choose an option:\n1. Hit\n2. Stay\nEnter any other key to exit\n")
			if ans == '1':
				self.hit(self.hand)
			elif ans == '2':
				print("You have decided to stay.")
			else:
				print("Thanks for trying out the game!")
				exit()

	def score(self, hand):
		ace_count = 0
		score = 0
		for card in hand:
			if isinstance(card, str):
				if card == 'A':
					ace_count += 1
				else: #other face cards
					score += 10
			else:
				score += card

		#Calculate ace value last to ensure ace takes proper value
		for aces in range(ace_count):
			if aces == ace_count - 1:
				if score < 11:
					score += 11
				else:
					score += 1
			else:
				score += 1
		return score

	def hit(self, hand):
		card = self.deck.pop()
		hand.append(card)

	def bust(self):
		print("Oh no. You busted! Better luck next time.")
		self.play_again()

	def dealer_round(self):
		#real life dealer always hits if under 17
		self.dealer_score = self.score(self.dealer_hand)
		while self.dealer_score < 17:
			self.print_dealer()
			print("Dealer hits.")
			time.sleep(2)
			self.hit(self.dealer_hand)
			self.dealer_score = self.score(self.dealer_hand)
		self.print_dealer()

	def print_dealer(self):
		print('\n')
		print("Dealer's cards: " + str(self.dealer_hand))
		print("Dealer total = " + str(self.dealer_score))
		time.sleep(2)
		

	def final_eval(self):
		print('\n')
		if self.dealer_score > 21:
			print("Dealer busted. You win!")
		else:
			print("Your hand: " + str(self.hand) + "   Your score: " + str(self.own_score))
			print("Dealer's hand: " + str(self.dealer_hand) + "   Dealer's score: " + str(self.dealer_score))
			if(self.own_score > self.dealer_score):
				print("Good job! You beat the dealer!")
			else:
				print("You didn't beat the dealer. Better luck next time.")

	def play_again(self):
		again = input("\nEnter 1 to play again. Enter any other key to exit\n")
		if again == '1':
			self.__init__()
			self.game()
		else:
			exit()

		

if __name__ == "__main__":
	game = BlackJackGame()
	game.game()

