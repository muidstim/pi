#import the Flask library
from flask import Flask
import random

#create the app: __name__ is always "__main__"
app = Flask(__name__)

#This simply returns a random number
@app.route("/getRandomNumber")
def getRandomNumber():
    print("random function was called, this is for debugging")
    
    #whatever you return is put into the variable "data"
    myrandom = "<h1>" + str(random.randint(1, 100)) + "</h1>"
    return myrandom

#create a function that is run when the URL is opened
#type http://localhost:5000 into the browser on the pi
@app.route("/")
def home():
    #whatever you return is shown in the browser
    
    myhtml = '''
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script>
setInterval(function()
{ 
    $.ajax({
      type:"get",
      url:"/getRandomNumber",
      datatype:"html",
      success:function(data)
      {
          //Whatever is returned by app.route("/random") will be inside the variable "data"
          //All the html inside of the <div class="random"> will be replaced 
          $( ".random" ).html(data);
      }
    });
}, 500);//time in milliseconds to update the data
</script>

<h1>Ajax Example</h1>

Here is a random number:
<div class="random">
This is the HTML that will be replaced
</div>
'''
    return myhtml

#Start the app, this should be the last line
if __name__ == "__main__":
    app.run()

