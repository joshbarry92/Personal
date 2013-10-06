	/*******************************************************************************
	*Inputs: None
	*Outputs: A unique 20 character First Name, Last Name, and Address. Will also 
	*		output a unique email by taking the last name and adding an email extension. 
	*Author: Joshua Barry
	*Date: 6/19/13
	********************************************************************************/
	
	#include <stdio.h>
	#include <stdlib.h>
	#include <time.h>	
	#include <sys/timeb.h>
	
	int main()
	{
		//Seed Random Number Gen using MS * SEC
		struct timeb tmb;
		ftime(&tmb);
		srand(tmb.millitm * tmb.time);
		//Call Function to create Random Names
		rName();
		//End Program
		return 0;
		
	}
	
	int rName ()
	{
		
		//Declare Indexing Numbers
		int i;
		int ct;
		
		//Declare and Preallocate space for Strings
		char firstname[21];
		char lastname[21];
		char email[30];
		char address[21];
		
		//Declare Temp Variables 
		char randChar = ' ';
        int randNum = 0;

		
		//CT Loop runs through values 0-2 that will determine which name the random letters will fill.
		//0=firstname; 1=lastname; 2=address
		for (ct=0; ct<3; ct++)
		{
			//i loop to fill each string with 20 random letters. 
			for (i=0; i<20; i++)
			{
				//Get random number between 1 and 26. 
				randNum = 26 * (rand() / (RAND_MAX + 1.0));
				//Add 97 to that value to match it up with the beginning of the ASCII chart.  
				randNum = randNum + 97;
				//Cast the number into a char.
				randChar = (char)randNum;		
				//Statements to determine which string is being added too. 
				if (ct == 0)
					firstname[i] = randChar;
				else if (ct == 1)
					lastname[i] = randChar;
				else if (ct == 2) 
					address[i] = randChar;	
			} //End I For Loop
		} //End CT For Loop
		
		//Add null value to the end of the strings
		firstname[20] = NULL;
		lastname[20] = NULL;
		address[20] = NULL;
		
		//Copy the first name and concat @qqqqq.edu to the end of it. 
		strcpy(email,firstname);
		strcat(email,"@qqqqq.edu");
		
		/************************************************************/
		//COMMENT ME OUT DURING LOADRUNNER EXECUTION//
		//Print each of the strings to the terminal window. 
		printf("First Name: %s\n",firstname);
		printf("Last Name: %s\n", lastname);
		printf("Email: %s\n", email);
		printf("Address: %s\n", address);
		/***********************************************************/
		
		/*********************************************************
		//UNCOMMENT DURING LOADRUNNER EXECUTION//
		//Save variables to LOADRUNNER//
		lr_save_string(firstname,"firstname")
		lr_save_string(lastname,"lastname")
		lr_save_string(email,"email")
		lr_save_string(address,"address")
		/**********************************************************/	

		//End Program
		return 0;
	}