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

function DefineKeys(line, DefKey, Count) {
    //var countFeat = 0;
    var key = new Array();
    var condition ;
    
    for(i in line) {
        
            
            if (line[i].indexOf(DefKey[0]) > -1 || line[i].indexOf(DefKey[1]) > -1){
        
                var myString =line[i];
                myString = myString.replace(/\s+/,"")
                myString = myString.replace('"','');
                myString = myString.replace('": {','');
                key.push(myString);
        
                if(line[i].indexOf(DefKey[1]) > -1 && Count == "true") {
                    countFeat = countFeat+1; // Counts all the FeatureModelInstances
                }
        
            }
            
        
            
    }
    return DefKey,key;
}


//  Select all the Keys

function SelectKeys(key, countFeat,jsonContent) {
    
    var k = 0;
    var content = [];
    
    //console.log(key);
    
    for(i in key) {
        
    
        if (i == 0){
        
                //Select the Environment Root content
                var content1 = FindKeysContent(key[i],jsonContent);
                content = repeatelem(content1,countFeat);
                countFeat = 0;
        
        }
    
        if (i>0){

            
            content[countFeat] = FindKeysContent(key[i],content[countFeat]);
            countFeat = countFeat+1;
            
        
        }
    
    }
    return content;
}

//  Select the coordinates

function SelectCoordinates(keyCoord,newcontent,CountFeat) {
    
    var n = CountFeat+CountFeat;


    var CoordFeat = FindKeysContent(keyCoord[n], newcontent);

    CoordFeat = FindKeysContent(keyCoord[n+1], CoordFeat);

    
    RA = parseFloat(FindKeysContent("coordinate__right_ascension",CoordFeat));
    DEC = parseFloat(FindKeysContent("coordinate__declination",CoordFeat));

    

    return RA, DEC
    
}




function GetFeatVal(key,content){
    
    var Data = [];
    var keyval ;
    
    
    for (var j in key){
        
        keyval = key[j];


        
        for(var exKey in content) {
            
            var jsoncont = content;
            
            
            if(exKey == keyval){
                
                Data.push(jsoncont[exKey]);
                
                
            }
        }
    }
    
    return Data
}




/*********************************/
/*********************************/


/*********************************/
/************* MAIN **************/
/*********************************/

// Call libraries
var json = require('json');
var fs   = require('fs');


//var DefKey = ["Environment Root","Feature Model Instance","World Transformation","EI 3D Location"];

var DefKey          = ["Environment Root","Feature Model Instance"];
var DefKeyCoord     = ["World Transformation","EI 3D Location"];
var DefKeyPropValue = ["Property Value"];
var DefKeyClassData = ["Classification Data"];


var key          = new Array();
var keyCoord     = new Array();
var keyPropVlue  = new Array();
var keyClassData = new Array();
var RA = [];
var DEC = [];
var countFeat = 0;
var newcontent = [];
var PropValue = [];
var ClassData = [];
var CoordData = [];

var filename = "LMBX_cat.json";
// Get content from file
var file = fs.readFileSync(filename);
// Convert String  to JSON type
var jsonContent = JSON.parse(file);
// Access to each line of the Database as string
var line = file.toString().split("\n");


//Define the keys and the number of coordinates
DefKey,key = DefineKeys(line, DefKey,"true");
DefKeyCoord,keyCoord = DefineKeys(line, DefKeyCoord,"false");
DefKeyPropValue,keyPropVlue = DefineKeys(line, DefKeyPropValue,"false");
DefKeyClassData,keyClassData = DefineKeys(line, DefKeyClassData,"false");


//Select the Environment Root content


//var content1
//var NewJson = [] ;




// Return an array which contains all the Feature Model Instances
newcontent = SelectKeys(key, countFeat,jsonContent) ;



var i = 0;

// Foe Each Feature Model Instance the related Values are selected

while(i < countFeat){
    
    ////////// Get Classification Data //////////////
    console.log("Classification Data");

    
    ClassData = GetFeatVal(keyClassData,newcontent[i]);
    console.log(ClassData);
    console.log("\n");
    
    ////////// Get Property Value //////////////
    
    console.log("Property Value");
    PropValue = GetFeatVal(keyPropVlue,newcontent[i]);
    console.log(PropValue);
    console.log("\n");
    
    
    
    ////////// Get Coordinates  //////////////
    
    console.log("Coordinates");
    
    RA,DEC = SelectCoordinates(keyCoord,newcontent[i],i);
    console.log(RA);
    console.log(DEC);
    console.log("\n");
    
     i = i+1;
    
}





/*********************************/
/*********************************/




