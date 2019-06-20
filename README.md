# myBlockchain

To add a new transaction to the next block to be mined:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;POST http://localhost:5000/transactions/new<br/>
&nbsp;&nbsp;&nbsp;&nbsp;Add a 'raw' body of JSON from the output of getjson.py<br/>
 
To mine the next block:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;GET http://localhost:5000/mine<br/>
 
To view the chain:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;http://localhost:5000/chain<br/>
