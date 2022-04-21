# USU
Install the following:
Python3:
https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/
then:
pip3 install fastapi
pip3 install uvicorn

from the USU repo dir:
- run python3 init.py to generate some data in the db
- run uvicorn main:app --reload-dir /<path to the repo directory>/
- load test.html into a browser for individual test cases
    - press Reset DB to get back to the DB original state with prepopulated 17 records

The uvicorn is configured to add origin * to work fr.om file system
