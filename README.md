# USU
Install the following:
Python3:
https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/
then:
pip3 install fastapi
pip3 install uvicorn

from the USU repo dir:
- run uvicorn main:app --reload-dir "path to the repo directory"
- load test.html into a browser for individual test cases
    - Start from left to right by 1, Generate DB to get back to the DB original state with prepopulated 17 records
- run sh gdb.sh to generate some data in the db, about 1000 records
- load usu.html into browser to get a little better UI.
    - the button "insert" shows only when the whole table is displayed
    - the buttons "add" and "delete" shows only when the whole table is displayed and a row in table is selected

The uvicorn is configured to add origin * to work fr.om file system
There's no read in chunks, all result curso is in memory when displayed on the page.
