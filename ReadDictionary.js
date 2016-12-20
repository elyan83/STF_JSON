
/*Acces JSON file content as a Dictionary */
/*********************************/

// Call JSON module
var json = require('json');

// Define JSON File
var fs   = require("fs");
console.log("\n *STARTING* \n");

// Get content from file
var file = fs.readFileSync("STFDepthOutTrial.json");

// Convert String  to JSON type
 var jsonContent = JSON.parse(file);

// Get Value from JSON

console.log("minor_EDCS_version:", jsonContent.minor_EDCS_version); // THIS WORKS WELL AND PRINT 4 VALUE
console.log("\n");
console.log("Declination :", jsonContent.coordinate__declination); // THIS DESN'T GENERATE ERROR, BUT THE CONTENT IS 'UNDEFINED'
console.log("\n");
//console.log(RightAscension :", jsonContent.coordinate->right_ascension); THIS GENERATE ERROR BECAUSE OF THE ' ->' CHARACTER
console.log("\n *EXIT* \n");


// Access to every element of a JSON object
// ONLY THE TRANSMITTAL_ROOT LEVEL IS TAKEN INTO ACCOUNT, THEN STOPS

for(var exKey in jsonContent) {
      console.log("key:"+exKey+", value:"+ jsonContent[exKey]);
 }


//Checking whether the JSON object has a specific key

console.log("\n");

if(jsonContent.hasOwnProperty('minor_EDCS_version')){
    console.log('minor_EDCS_version',jsonContent.minor_EDCS_version); // THIS WORKS
}

if(jsonContent.hasOwnProperty('coordinate__declination')){
    console.log('coordinate__declination',jsonContent.coordinate__declination); // NEVER SHOWS THIS
}

/*if(jsonContent.hasOwnProperty('coordinate->right_ascension')){
    console.log('coordinate->right_ascension',jsonContent.coordinate->right_ascension); // THIS DOES'T WORK BECAUSE OF THE -> STRING
}*/
console.log("\n");

/*********************************/



