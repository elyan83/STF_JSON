
/*********************************/
/********* FUNCTIONS *************/
/*********************************/

// Find all keys in de dictionary and return the dictionary selected.
function FindKeysContent(SearchKey, jsonFile) {
    
    for(var exKey in jsonFile) {
        if(exKey = SearchKey){
            var NewJson = jsonFile[exKey];
            
        }
    }
    
    
    return NewJson;
}

// returns an array with element elem repeated n times.
var repeatelem = function(elem, n){
    var arr = [];
    for (var i=0; i< n; i++) {
        arr = arr.concat(elem);
    };
    return arr;
};

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


//  Select all the Keys

function SelectKeys(key, countFeat,jsonContent) {
    
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
    return newcontent;
}

//  Select the coordinates

function SelectCoordinates(newcontent) {
   
    for(i in newcontent) {
        
        RA.push(parseFloat(FindKeysContent("coordinate__right_ascension",newcontent[i])));
        DEC.push(parseFloat(FindKeysContent("coordinate__declination",newcontent[i])));
        
    }
    
    return RA, DEC
    
}


/*********************************/
/*********************************/


/*********************************/
/************* MAIN **************/
/*********************************/

// Call libraries
var json = require('json');
var fs   = require('fs');


var DefKey = ["Environment Root","Feature Model Instance","World Transformation","EI 3D Location"];
var key = new Array();
var RA = [];
var DEC = [];
var countFeat = 0;

var filename = "STFDepthOut.json";
// Get content from file
var file = fs.readFileSync(filename);
// Access to each line of the Database as string
var line = file.toString().split("\n");


//Define the keys and the number of coordinates
DefKey,key = DefineKeys(line, DefKey);


// Convert String  to JSON type
var jsonContent = JSON.parse(file);

var newcontent = [];

newcontent = SelectKeys(key, countFeat,jsonContent);


//  Get Coordinates (Floating)
RA, DEC = SelectCoordinates(newcontent);


console.log(RA);
console.log(DEC);
console.log(countFeat);


/*********************************/
/*********************************/




