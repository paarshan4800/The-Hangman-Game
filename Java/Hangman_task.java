import java.util.Scanner;

public class Hangman_task {
    public static void main(String[] args) {      
         char[] setstr = new char[20];
         int filled=0,tofill=0,flag;
         
         Scanner input = new Scanner(System.in);

         System.out.println("Enter the length of the word:");
         int ipsize = input.nextInt();

         System.out.println("Enter the " + ipsize + "letter word:");
         String defstr = input.next();

         System.out.println("Set the word with blanks:");
         String setstr_str = input.next();

         for(int i=0;i<ipsize;i++) {
             setstr[i] = setstr_str.charAt(i);  //We get it as a string and convert it into character array
             if(setstr[i] == '_') { //Count the number of blanks for conditional purposes
                 tofill++;
             }
         }

         System.out.println("How many lives do you want to give to your friend:");
         int life = input.nextInt();

         System.out.print("\n\nNow its time for your friend to guess the word:");

         // Should check till we have lives left and till we have found out the word
         while(life>0 && filled<tofill) {

             System.out.print(setstr);
        
             flag=0;
            
             System.out.println("\nLives left:" + life + "\nGuess a letter:");
        
             char guess = input.next().charAt(0);
            
            //  Checking whether the letter we guessed matched with the letters in the word
            for(int i=0;i<ipsize;i++) {
                if(guess == defstr.charAt(i)) {
                    if(setstr[i] == '_') {  // Overwrite the _ with the guessed letter
                    setstr[i] = guess;  //If the word matches, fill the blank
                    filled++; //Increment the no. of blanks filled
                    flag = 1;
                    }
                }
            }

            if(flag==0) {
                life--;
            }
        }

         if(life>0) {
             System.out.println("You have found out the word(" + defstr + "). Enjoy your day!!!\n");
         }
         else {
             System.out.println("You havent found the word. The word was " + defstr + "\n");
         }
    }
}
