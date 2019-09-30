# Flask App To Display - force-directed-graph
This is a simple flask app that serves a Force Directed graph visualization of a given dataset.
The visualization is done with D3.js library.
The application gives you an option to upload and display json file in form of a graph.
It has a search fuctionality at the left - sidebar, to search from graph and highlight searched data.
It also have a connection to Neo4j

More info about force directed graph drawing: https://en.wikipedia.org/wiki/Force-directed_graph_drawing


### Prerequisites

You only need to install flask to be able to run my app.
```
pip3 install flask
```
### Running the server

After installing flask, and cloning the repository, cd inside the directory where app.py is and run app.py:

```
python3 app.py
```
if you face any problems please refer to <a href="http://flask.pocoo.org/docs/0.12/quickstart/">flask documentation</a>

After you run app.py you should see the following:
![image](https://user-images.githubusercontent.com/20475053/45429730-28312000-b6a4-11e8-9eff-b567c55f4332.png)

which means that the local server is running, now you should open the browser and open the local server with the specified port and see the following:

![image](https://camo.githubusercontent.com/a7398bbf8bf2294ef4e5980fc0a440c7cf2d7d27/687474703a2f2f676973742e6769746875622e636f6d2f76617374757269616e6f2f30326166666533303663653434356534323366393932666165656131333532312f7261772f707265766965772e706e67)


## Providing your own dataset

I've wrote a very handy script that doesn't make assumptions about your data, you have to provide it with a set of vectors, a set of labels for each vector, a set of titles for each vector, and it will populate the graphFile.json which the D3 library uses to draw the nodes and conections between the nodes in the graph.

![image](https://user-images.githubusercontent.com/20475053/45431638-64ff1600-b6a8-11e8-9875-dbe63a4c6396.png)

in the above script, salaries.csv is a sample of vectors, their labels, and their associated titles of some news articles that i've prepared for this example.

then in the last line i call the function pipe which calculates the distances between the vectors, and outputs the graph connections to graphFile.json or otehr .json files which will be used by d3 to render the graph.

pipe is a VERY general tool that doesn't make assumptions about your data, you only provide it a set of vectors and a set of labels, in my example i provided it with data from salaries.csv, but you can provide your own data and labels, and it will calculate the distances and output the result in graphFile.json, and the visulaization is ready to be served by the flask server.


## Connecting To  Databases

This app is not limited to a specific database, I have intergrated Neo4j API and codes to call and query the DB. The Neo4j button at the header enables you to trigar the call and run Neo4J API files. 

## Application Upgrading

More features and functionalities can be added on this app. Any thought or imagination for the future appearance of the graphical user interface or technical functionalities can be suggested by emailing us 
<a href="ibrahim@bluemarblegraphics.co.ke">MAIL IBRAHIM</a>

## GOOD LUCK!!!

## Author

* **IBRAHIM_MALOBA**  

