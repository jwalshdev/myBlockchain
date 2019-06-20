# myBlockchain

To add a new transaction to the next block to be mined:<br/>
  POST http://localhost:5000/transactions/new<br/>
  Add a 'raw' body of JSON from the output of getjson.py<br/>
 
To mine the next block:<br/>
  GET http://localhost:5000/mine<br/>
 
To view the chain:<br/>
  http://localhost:5000/chain<br/>
