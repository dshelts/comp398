
// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://dshelly:abc123@ds047930.mongolab.com:47930/messaround", function(err, db) {
  if(!err) {
    console.log("We are connected");
  }
  else{
  	console.log(err);
  }

	var collection = db.collection('hw14', function(err, collection){
    	collection.remove({},function(err, removed){
    		});
		});

	// Clearing out the collection
	//collection.remove({});
	var testArray = [];
	for(i=0; i<2500; i++){
		testArray.push({myKey: i })
	}
	
	
	collection.insert(testArray, {w:1}, function(err, result) {});
	console.log("finished insert")



});
