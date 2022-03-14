# Election Analysis
Programs Used: Python

## Overview of Election Audit:

In this election audit, we compared 3 candidates and 3 counties.  The candidates running for office were Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane.  The counties that were being audited were Jefferson County, Denver County and Arapahoe County.  

The purpose of the audit was to compare the voter turnout for each county (as a percent) and to determine which candidate won. 

## Election Audit Results:

During this audit, we were able to determine the total number of votes cast for the election and how many votes came from each county.  In doing so, we were also able to determine which county had the highest turn out. 

From there we also broke down the actual count of votes cast for each candidate and the percent of the total votes they recieved.  In doing this analysis, we were able to determine a clear winner. 

![challenge_3_terminal_results](https://user-images.githubusercontent.com/96890065/158087522-fb89db7c-53d4-4907-af80-a7042cb4405c.JPG)

* Election Results
  * Total Votes = 369,711
    * The total votes were pulled from the csv file using the following code:
       Initialize a total vote counter.
        total_votes = 0
        for row in reader:
         total_votes = total_votes + 1
         
  * County Vote breakdown
   * The counties were entered into a list (county_list = []) and the votes were entered into a dictionary (county_vote = {}). The code was writen such that if a new name or county was added, that item would be tracked.  
   ![new_item](https://user-images.githubusercontent.com/96890065/158088074-c34b387d-d355-47f9-9953-50d4b70a779f.JPG)
   
  * Largest County Turnout
    * This was determined by using a for-loop
  

  * Candidate Vote count and percentages
   * The candidates were entered into a list (candidate_options = [ ]) and their votes entered into a dictionary (candidate_votes = { }). This code was written similar to the the county tracker (as seen above). 

 * Winner Results
  * 

## Election Audit Summary:

This code can be used for furture elections, because we have written into the code, the ability to add and track new candidate names and county names:


