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
       
       
## Election Audit Summary:

This code can be used for furture elections, because we have written into the code, the ability to add and track new candidate names and county names:
   # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_vote[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_vote[county_name] +=1
