from random import randint
#This is the main function where there are two players rolling the dice, each at a time for 5 rounds.
#The random numbers of each player are displayed and according to which player's number is greater than the other
#wins that particular round.
#After the 5 rounds are completed, the game displays the player who won the most rounds.
def main():
      player1=0
      player2=0
       
      Round=1
      player1_total_Rounds_Won=0
      player2_total_Rounds_Won=0

      for Round in range(5):
            player1_round_score, player2_round_score = play_round(Round)
            player1_total_Rounds_Won += player1_round_score
            player2_total_Rounds_Won += player2_round_score
           
      identify_winner(player1_total_Rounds_Won, player2_total_Rounds_Won)


def identify_winner(player1_total_Rounds_Won, player2_total_Rounds_Won):
      if player1_total_Rounds_Won == player2_total_Rounds_Won:
            print("It is a tie") 
      elif player1_total_Rounds_Won > player2_total_Rounds_Won:
            print(f'Player1 wins with: {player1_total_Rounds_Won} Rounds') 
      elif player2_total_Rounds_Won > player1_total_Rounds_Won:
                  print(f'Player2 wins with: {player2_total_Rounds_Won} Rounds')          
           
      
def play_round(Round):
      print(f'Round: {Round}') 
      player1 = roll_dice()
      player2= roll_dice()
      
      print(f'Player1 rolled: {player1}') 

      print(f'Player2 rolled: {player2}')

      player1_score = 0
      player2_score = 0

      if player1 > player2:
            player1_score = 1
            print('Player 1 wins')
      
      elif player1 == player2:         
            print(f'It is a Draw for all players') 
      
      elif player2 > player1 :
            player2_score = 1
            print('Player 2 wins')
      
      return player1_score, player2_score

            

#A function which uses random numbers between 1 and 6 and returns the random numbers
def roll_dice():
      diceRoll = randint(1,6)
      return diceRoll

main()      