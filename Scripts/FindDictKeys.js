
/*********************************/
/********* FUNCTIONS *************/
/*********************************/


// Read Content of a file line by line and define all the keys contained in DefKey

function DefineKeys(line, DefKey) {
    //var countFeat = 0;
    var key = new Array();
    
    for(i in line) {
        if (line[i].indexOf(DefKey[0]) > -1 || line[i].indexOf(DefKey[1]) > -1 || line[i].indexOf(DefKey[2]) > -1 || line[i].indexOf(DefKey[3]) > -1 ){
        
            var myString =line[i];
            myString = myString.replace(/\s+/,"")
            myString = myString.replace('"','');
            myString = myString.replace('": {','');
            key.push(myString);
        
            if(line[i].indexOf(DefKey[1]) > -1) {
                countFeat = countFeat+1; // Counts all the FeatureModelInstances
            }
        
        }
    }
    return DefKey,key;
}


/*********************************/
/************* MAIN **************/
/*********************************/

// Call libraries

//var browserify = require('browserify');
var fs = require('fs');

//var b = browserify('example/main.js');
//b.transform('brfs');

//b.bundle().pipe(fs.createWriteStream('bundle.js'));

//var fs   = require('fs');

var DefKey = ["Environment Root","Feature Model Instance","World Transformation","EI 3D Location"];
var key = new Array();
var countFeat = 0;

// Get content from file
var file = fs.readFileSync("/Users/Elisa/Documents/MagnetarGame/JSONtrial/STFDepthOut.json");
// Access to each line of the Database as string
var line = file.toString().split("\n");


//Define the keys and the number of coordinates
DefKey,key = DefineKeys(line, DefKey);

console.log(key)
content = JSON.stringify(key);
/*
var http = require("http");

http.createServer(function (request, response) {
                  // Send the HTTP header
                  // HTTP Status: 200 : OK
                  // Content Type: text/plain
                  response.writeHead(200, {'Content-Type': 'text/plain'});
                  
                  // Send the response body as "Hello World"
                  //response.end('Hello World\n');
                  response.end(content);
                  }).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
/*

/*********************************/
/*********************************/




