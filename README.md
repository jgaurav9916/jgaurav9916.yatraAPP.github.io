# jgaurav9916.yatraAPP.github.io
A simple train route app which fetches data from train route API to show the train route of the train number entered.


Python Provides various options for developing graphical user interfaces(GUI). One of them is TKinter.
----> TKinter - Tkinter is the python module/interface to TK GUI toolkit shipped with Python.
------------>TKinter Programming........
        $ Import the Tkinter Module.
        $Create the GUI application main window.
------------> Python Requests Module............
        $ The reuests module allows you to send HTTP requests using Python .
        The HTTP requests returns a Response object with all the response data.
we have made a yatra class for creating the instance of the user who will be providing input train number
--------->The fetch method is used to call the request throughthe railway api for the given token key and foematted with the train no. provided by the user.

---------->
We have used get method in requests to obtain the data from the api.

----------->
we have then collected the information in data in json format using response.json() method.
------------> 
And finaly for every matching route in data we have retured the via stations
