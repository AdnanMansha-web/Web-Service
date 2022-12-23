# Metis Linux System Stat Service


## How To Run

Python version 3.6 above is required to run this service.

The following steps are perfomed:

* setup the config parameters (i.e Host, Port) in api_server_config.ini file.
* Install required packages.
```
pip install -r requirements.txt
```
* Run the api_server.py file.
```
python api_server.py
```

## Rest API Endpoints

The service has the following endpoints:

* GET /api/v1/systemstat/all_info ->  Return all system basic information (i.e platform, architecture, host-name, mac-address, processor).
* GET /api/v1/systemstat/cpu -> Return CPU information (i.e CPU Percentage, CPU Count, CPU Time Percent, CPU stat, Max Frequency, Min Frequency, Current Frequency).
* GET /api/v1/systemstat/ram -> Return Ram information (i.e Ram Total, Ram Available, Ram Used).
* GET /api/v1/systemstat/disk -> Return Disk information (i.e Total read, Total write).

For authenication Bearer Scheme is used and Bearer Token is provided as Authorization in the Request Headers to get the response successfully.

## Testing

For API testing Tavern framework is used and to perform the tests the following command is used:
```
 pytest tests/test_mytest.tavern.yaml -v
```
