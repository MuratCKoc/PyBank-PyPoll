# python-challenge

* Inside of each folder that you just created, add the following:

  * A `main.py`. This is the main script to run for each analysis.
  * A "Resources" folder that contains the CSV files used.
  * An "analysis" folder that contains your text file that has the results from your analysis.

## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

* Create a Python script that analyzes the records to calculate each of the following:

  - [x] The total number of months included in the dataset

  - [x] The net total amount of "Profit/Losses" over the entire period

  - [x] The average of the changes in "Profit/Losses" over the entire period

  - [x] The greatest increase in profits (date and amount) over the entire period

  - [x] The greatest decrease in losses (date and amount) over the entire period

* Analysis looks similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

- [x] In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote Counting](Images/Vote_counting.png)

* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  - [x] The total number of votes cast

  - [x] Complete list of candidates who received votes

  - [x] The percentage of votes each candidate won

  - [x] The total number of votes each candidate won

  - [x] The winner of the election based on popular vote.

* As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

- [x] In addition, your final script should both print the analysis to the terminal and export a text file with the results.


