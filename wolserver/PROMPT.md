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

