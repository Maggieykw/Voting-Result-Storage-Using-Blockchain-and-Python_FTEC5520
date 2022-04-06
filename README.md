# Voting-Result-Storage-Using-Blockchain_FTEC5520
This application allows electron organizer to store multiple voting result securely using Blockchain
In order to run this application, 
1. Download all the files in this folder (Can ignore "Demo.mov" which is for demostration only)
2. Run "blockchain.ipynb"
3. It will show URL and open it

Assumption:
- Considering proof of concept as a consensus algorithm to avoid high computation power
- Using a centralised flask server to avoid dealing with multiple nodes unnecessarily
- Multiple election with same frequency (e.g. daily, monthly) in a day are not supported
- Voting result (i.e. elected or unchosen) of each candidate is stored only 
- Candidate numbers are started from 1 for each election

Application contains the following five functions:
- Block Identification
- Block Creation
- Block Addition
- Block Searching
- Blockchain Integrity Verification

For demo, please refer to "Demo.mov"

Reference: https://github.com/adeen-s/Blockendance
(Further updated and enhanced the code inside the reference)
