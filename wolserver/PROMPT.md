Create a webservice in python.

The service is a frontpage for a service that runs in a machine that can be on or off.

The machine is called backend and it runs an LLM.

It should have one page:

- if the backend address is reachable, assume the machine is up, and the service should behave as an http proxy
- if the backend address is not reachable, show a status page with an option to start the backend
    + the status page should ask for a password if the backend is down
    + assume we have a script ready to start the backend, only provide the webservice for now

You should use the simplest possible python script.


---------------

change this proxy function to one that:

- displays the current status of the backend using the same method as before

- offers an option to start the service only if the service is down

---------------
use PBKDF2  with 600000 iterations instead of sha256 + salt

---------------
given that the page has the following form:

```html
<form action="/stop" method="post">
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br/>
        <label for="shutdown">Also shutdown server:</label>
        <input type="checkbox" name="shutdown" >
        <br/>
        <button type="submit">Stop Service</button>
    </form>
```

implement the /stop POST call as follows:
- call the "STOP_SCRIPT"
- if the "shutdown" parameter is checked, also run the "SHUTDOWN_SCRIPT"
- return 200 on ok, 500 on error

---------------
have a look at   and create a template for the "stop" page.

The "stop" page should tell something about the "stop" method in  



Assume we will have a "success" variable , a service_link variable, and an "error_message" variable.