import random

class Simulation():
    """Creates and simulates the monty hall game. """
    
    def __init__(self,num_doors):
        
        #Sets the number of doors used to play the game
        self.num_doors = num_doors
        
        
        
    def set_doors(self):
        """Determines location of zonks and car, along with user choosen door and alternative. 
        
        Side Effects:
            zonks_list(list): Appends the zonks_list with car and zonks.
            
        Returns:
            user_choice(string): The door choosen by the user.
            alternative_choice(string): The alternative door that user can choose.
        """
        
        #Create the list of doors containing either a zonk or a car behind them
        doors_list = []
        
        #Appends to the list n number of zonks (n = number of doors)
        for door in range(self.num_doors):
            
            doors_list.append("zonk")
            
        #At random replace one of the zonks with the car
        doors_list[random.randint(0,self.num_doors-1)] = "car"

        #"User" chooses a door
        user_choice = doors_list[random.randint(0,self.num_doors-1)]
        
        #Remove the users choice
        doors_list.remove(user_choice)
        
        #Remove a door with a zonk
        doors_list.remove("zonk")
        
        #Alternative door choice
        alternative_choice = doors_list[random.randint(0,len(doors_list)-1)]

        #Returns the values of the users choice and the alternative choice
        return (user_choice,alternative_choice)
        
    def play_game(self,switch = False ,iterations = 1 ):
        """Determines and returns the number of times user wins the game.
        
        Args:
            switch(boolean): Choice to switch doors.
            iterations(int): Number of times game is played.
        
        Returns:
            Win percentage(float): Percentage of games won.
        """
        
        #Number of games won
        win_counter = 0
        
        #Number of games lost 
        loss_counter = 0
        
        #Keeps track of the number of games played
        game_counter = 1
        
        #Simulates games being played along with the outcome
        for i in range(iterations):
            
            #Calls the set_doors() function to get the users and alternative choices
            current_choice,alternative_choice = self.set_doors()
            
            #Specifies conditions where user has won that game
            if (current_choice == "car" and switch == False) or (alternative_choice == "car" and switch == True):
                win_counter += 1
            
            else:
                loss_counter += 1

        #print("Wins {0} Loses {1}".format(win_counter,loss_counter))
        
        #Calculates the win percentage        
        win_percentage = win_counter /iterations
        
        #Returns the win percentage of the game(s)
        return win_percentage
        
        
if __name__ == "__main__":
    simulation = Simulation(3)
    
    #simulation.set_doors()
    
    
    simulation.play_game(True,1000)