import pandas as pd
import os

# 1. Load your specific dataset
df = pd.read_csv("generation_analysis.csv")

# Store valid answers and rows flagged for deletion
user_answers = {}
rows_to_delete = []

for index, row in df.iterrows():
    while True:
        # Clear the terminal screen entirely
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Print the outputs from your specific columns
        print(f"--- Row {index + 1} of {len(df)} ---")
        
        # Using \n adds a line break, making long text prompts easier to read
        print(f"True Prompt:\n{row['truth_responce']}\n")
        print(f"Sycophantic Prompt:\n{row['syco_responce']}\n")
        
        print("-" * 40)
        print("(Enter 0 or 1 to save. Enter any other number to DELETE this row.)")
        
        raw_input = input("\nEnter your answer: ")
        
        try:
            # Force the input to be an integer
            ans = int(raw_input)
            
            if ans in [0, 1]:
                # If 0 or 1, save the answer using the row's index
                user_answers[index] = ans
            else:
                # If any other number, flag this index for deletion
                rows_to_delete.append(index)
            
            # Break out of the while loop to move to the next row
            break 
            
        except ValueError:
            # Catches cases where you accidentally type a letter or symbol
            print("\nInvalid input! You must enter a number.")
            input("Press Enter to try again...")

# Optional: Clear the screen one final time after the loop is done
os.system('cls' if os.name == 'nt' else 'clear')

# 2. Drop the rows you flagged for deletion
df = df.drop(index=rows_to_delete)

# 3. Store the collected answers in your new column
df['close_baseline'] = df.index.map(user_answers)

# 4. Save your progress to a new CSV so you don't lose your manual work!
df.to_csv("generation_analysis.csv", index=False)

print("Process complete. Your work has been saved to 'generation_analysis.csv'.\n")
