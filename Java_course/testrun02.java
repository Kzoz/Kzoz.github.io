
public class testrun02 {
 
    public static void main(String[] args) {
        
        int goalsHomeBarc = 2;
		int goalsAwayBarc = 1;
		int goalsHomeMad = 2;
		int goalsAwayMad = 1;
		int totalGoalsMad = goalsHomeMad + goalsAwayMad;
		int totalGoalsBarc = goalsHomeBarc + goalsAwayBarc;
		
		if(totalGoalsMad == totalGoalsBarc){
		    // When the overall result is even,
		    //goals scored away cound doulbe
		    // so we update the goals away for 
		    //each team and compare again.
		    goalsAwayBarc = goalsAwayBarc *2;
		    // The 'variable *= X' operator means 
		    //the same as 'variable = variable * X'
		    goalsAwayMad *=2;
		}
		
		// We calculate again the overall result
		totalGoalsMad = goalsHomeMad + goalsAwayMad;
		totalGoalsBarc = goalsHomeBarc + goalsAwayBarc;
		
		// We show the result
		System.out.println("Overall Result is ");
		System.out.print("Barcelona "+totalGoalsBarc);
		System.out.println(" - Madrid "+totalGoalsMad);
		
		if(totalGoalsMad > totalGoalsBarc){
		    System.out.println("Madrid passes the round!");
		}else if(totalGoalsMad < totalGoalsBarc){
		    System.out.println("Barcelona passes the round!");
		}else{
		    System.out.println("They have to play extra time!");
		}
    } 
}