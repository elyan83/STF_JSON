
/*Create an HTTP server which listens, i.e., waits for a request over 8081 port on the local machine.*/
/*********************************/

/* Synchronous call Output*/

var fs = require("fs");
console.log("\n *START* \n");
var content = fs.readFileSync("STFDepthOutTrial.json");
console.log("Output Content : \n"+ content);
console.log("\n *EXIT* \n");

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
/*********************************/



