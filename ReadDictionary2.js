
/*Acces JSON file content as a Dictionary */
/*********************************/


function FindKeysContent(SearchKey, jsonFile) {
    
    for(var exKey in jsonFile) {
        if(exKey = SearchKey){
            var NewJson = jsonFile[exKey];
            
        }
    }
    
    
    
    return NewJson;
}


var repeatelem = function(elem, n){
    // returns an array with element elem repeated n times.
    var arr = [];
    for (var i=0; i< n; i++) {
        arr = arr.concat(elem);
    };
    return arr;
};



// Call JSON module
var json = require('json');

// Read Content of a file line by line

var DefKey = ["Environment Root","Feature Model Instance","World Transformation","EI 3D Location"];
var key = new Array();
var RA = [];
var DEC = [];
var countFeat = 0;



var fs = require('fs');
var filename = "STFDepthOut.json";
var line = fs.readFileSync(filename).toString().split("\n");



for(i in line) {
    if (line[i].indexOf(DefKey[0]) > -1 || line[i].indexOf(DefKey[1]) > -1 || line[i].indexOf(DefKey[2]) > -1 || line[i].indexOf(DefKey[3]) > -1 ){
        
        var myString =line[i];
        myString = myString.replace(/\s+/,"")
        myString = myString.replace('"','');
        myString = myString.replace('": {','');
        key.push(myString);
        
    if(line[i].indexOf(DefKey[1]) > -1) {
            countFeat = countFeat+1;
        }
        
    }
}



console.log(countFeat);


var fs  = require("fs");
              
// Get content from file
var file = fs.readFileSync(filename);
              
// Convert String  to JSON type
var jsonContent = JSON.parse(file);


var newcontent = [];

var k = 0;

for(i in key) {
    
    if (i == 0){
        
        var content1 = FindKeysContent(key[i],jsonContent);
        
        newcontent = repeatelem(content1,countFeat);
        countFeat = 0;
        
    }

    if (i>0){
        
        if (i > k+3){
            countFeat = countFeat+1;
            k = k+3;
            
        }
        
        newcontent[countFeat] = FindKeysContent(key[i],newcontent[countFeat]);
        
    }

}


for(i in newcontent) {
    
    console.log(newcontent[i]);
    RA.push(parseFloat(FindKeysContent("coordinate__right_ascension",newcontent[i])));
    DEC.push(parseFloat(FindKeysContent("coordinate__declination",newcontent[i])));
    
}

console.log(RA);
console.log(DEC);




/*********************************/



