# python_challenge 

# PyBank ---

- Challenge description : To begin the assignment, I created a repository on my Git-Hub named "python-challnge." In the repository, I created a folder for each task naming them "PyBank" and "PyPoll." Each folder contains a "main.py" file, respective CSV files in the "Resource" folder and a results text box in the "Analysis" folder.   

- PyBank Assignment : I was tasked to develop a Python script that interprets financial data of a company using a CSV file that includes the profits, losses, and their dates.

- Solution : For the PyBank challenge, I scheduled a tutoring session with Fred Logan to help explain the homework and assist me with the proper codes to complete the tasks using PasteBin with the following link, "https://pastebin.com/vfmTk8y5." First, I imported the modules needed to properly run my code. We organized the budget_data CSV into a Tuple using string, integer, and float.

- Total_months : The CSV file was opened using csv_reader and skipping the header row, then processing each row in the data set. Next the total months were calculated using the function "total_months +=1" and net total sum of profits and losses over the period as a whole.  

- Changes in Profits / Losses : To determine the changes in profits and losses, the function 
"if prev_profit_loss is not None:
  change = profit_loss - prev_profit_loss
  changes.append(change)" was used.

- Calculating Avergage of Protfit / Losses changes : I used the function average_change = sum(changes) / len(changes) if changes else 0
 dividing the total amount of changes by the length of changes in the data set.

 - Greatest Increase and Decrease : This was calculated using the function 
 "if change > greatest_increase[1]:
                        greatest_increase = (date, change)
                    if change < greatest_decrease[1]:
                        greatest_decrease = (date, change)
                    prev_profit_loss = profit_loss"

- Return statement : This was used to return the results calculated with the previous functions used and updating variable values. 

- Handling Errors : My tutor assisted me in using a function to take care of any errors the code we worked on might encounter. 

- Printing financial analysis in terminal : To generate the evaluated financial report, the variables used were defined using the function 
"def generate_financial_report(total_months: int, net_total: int, average_change: float, 
                              greatest_increase: Tuple[str, int], greatest_decrease: Tuple[str, int]) -> List[str]:" 
To print the results in the terminal, the following function was used
"report_lines = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {total_months}",
        f"Total: ${net_total}",
        f"Average Change: ${average_change:.2f}",
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    ]
    return report_lines"

- Printing financial analysis in results txt file : Input and output variables were created with paths relative to the CSV file used and the results txt file. The function "os.makedirs(os.path.dirname(output_txt), exist_ok=True)" was used to ensure the output directory exists. The data was then analyzed, generated, printed, and saved into the report in results txt file using the functions 
" result = analyze_financial_data(input_csv)
    if result is None:
        print("Failed to analyze financial data. Please check the error messages above.")
        return

 - Unpack the analysis results
    total_months, net_total, average_change, greatest_increase, greatest_decrease = result
 
- Generate the financial report
    report = generate_financial_report(total_months, net_total, average_change, greatest_increase, greatest_decrease)
 
 - Save and print the report
    save_and_print_report(report, output_txt)
    print(f"\nFinancial analysis results saved to: {output_txt}")."
 
 # PyPoll ---

- Challenge description : Create a python scrput that best interprets the votes using poll data provided in "election_data" CSV file, composed of "Voter ID", "County", and "Candidate".
 
- Solution : To begin, I imported modules "os and csv" to help properly run my code. I created a path for the CSV file under the variable "election_data_csv." Next, I created variables to store the election data values and respective to figures I will calculate. I used the previous code my tutor assisted me with as well as another code for reference from the following link "https://github.com/4Reference/python-challenge/blob/master/PyPoll/main.py."

- Total votes cast: I usedd the function next(csvreader) to skip the header and counted the total number of votes using "election_data = list(csvreader)
    row_count = len(election_data)"

- Create a list of candidates who obtained votes : To make a complete list of contenders that received votes, the code "list_of_candidates = list()
    ballots = list()
    for i in range (0,row_count):
        candidates = election_data[i][2]
        ballots.append(candidates)
        if candidates not in list_of_candidates: 
            list_of_candidates.append(candidates)
    total_candidates = len(list_of_candidates)" was used to do so.

- Ballot total and percentage of votes candidate gained : To calculate the total number of ballots and the percentage of which each runner received, I used the code
   "total_votes = list()
    percentage_votes_won = list()
    for v in range (0,total_candidates):
        name = list_of_candidates[v]
        total_votes.append(ballots.count(name))
        vote_percentage = total_votes[v]/row_count
        percentage_votes_won.append(vote_percentage)"

- Winner by most votes : To determine the winner, I calculated the most votes recieved by a candidate using the code
  "winner = total_votes.index(max(total_votes))"    

- Return results in terminal :
  " print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,total_candidates): 
        print(f"{list_of_candidates[k]}: {percentage_votes_won[k]:.3%} ({total_votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {list_of_candidates[winner]}")
    print("----------------------------") "

  -Create a variable for results text file : 
 results_txt = r"C:\Users\jasmi\OneDrive\Documents\python-challenge\PyPoll\analysis\results.txt"

-Print data analysis in results text file :
"print("Election Results", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    print(f"Total Votes: {row_count:,}", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    for t in range (0,total_candidates): 
        print(f"{list_of_candidates[t]}: {percentage_votes_won[t]:.3%} ({total_votes[t]:,})", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))
    print(f"Winner: {list_of_candidates[winner]}", file=open(results_txt,"a"))
    print("----------------------------", file=open(results_txt,"a"))"
    
