# myBlockchain

To add a new transaction to the next block to be mined:
  POST http://localhost:5000/transactions/new
  Add a 'raw' body of JSON from the output of getjson.py
 
To mine the next block:
  GET http://localhost:5000/mine
 
To view the chain:
  http://localhost:5000/chain
