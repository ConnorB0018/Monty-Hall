import monty_hall as mh
import pandas as pd
import seaborn as sb 
import matplotlib.pyplot as plt


class Plot():
    """VIsualizes the data produced by the monty hall game simulations."""
    
    def __init__(self,doors,simulations):
        #Stores data from each monty hall simulation
        self.sequence = []
        
        #Stores the number of doors for the given simulation
        self.doors = doors
        
        #Number of times game is played.
        self.simulations = simulations
        
    def simulate(self):
        """Runs the simulations to collect data.
        
        Side Effects:
            Appends to the sequence list with simulation data.
        """
        #Keeps track of the amount of times the game is played
        counter = 0
        
        #Simulates the monty hall game as determined by the number of simulations
        for i in range(self.simulations):
            simulation_obj = mh.Simulation(self.doors)
            
            #If the simulation game is even the player chooses to switch doors
            if i % 2 != 0:
                
                switch_value = True
                
                #Calls the play_game method to get win percentage
                win_percentage = simulation_obj.play_game(switch_value,self.simulations)
                
                #Simulation data is appended to the sequence list
                self.sequence.append({counter:[i,win_percentage,self.doors,str(switch_value)]})
            #If the simulation iteration is odd the user does not switch doors
            else:
                switch_value = False
                #Calls the play_game method to get win percentage
                win_percentage = simulation_obj.play_game(switch_value,self.simulations)
                #Simulation data is appended to the sequence list
                self.sequence.append({counter:[i,win_percentage,self.doors,str(switch_value)]})
            #Increments the counter for each simulation
            counter += 1    
        
        
    def make_plot(self,sequence):
         """Creates the graph comparing the win percentage when keeping or changing doors.
         
         Args:
            sequence(list): List nested with dictionaries containing simulation data.
         """
         
         #Specifies what portions of the list(sequence) are going to be used
         data = [sequence[row][row] for row in range(len(sequence))]
         
         #Turns the subsetted list elements into a dataframe
         df = pd.DataFrame(data,columns=["Iterations","Win %", "Doors","Switched"])
         
         #Plots the Iterations-win percentage for games where either the user kept or changed doors
         plot = sb.lmplot(x = "Iterations",y="Win %",data = df, hue = "Switched")
         #Displays the graph
         plt.show()
         #Specifies the file name to be used for saving the graph
         file_name = "Simulations {0} Doors {1}.png".format(self.simulations,self.doors)
         #Saves the plot object 
         plt.savefig(file_name,format ="png")
         plt.close()
if __name__ == "__main__":
    
    plot_obj = Plot(5,100)
    plot_obj.simulate()
    data_frame = plot_obj.sequence
    plot_obj.make_plot(data_frame)
    