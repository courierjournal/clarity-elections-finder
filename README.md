# Clarity Elections Finder

Clarity is a great resource for data on election night. You can typically find past elections hosted on Clarity by using the following endpoint: https://results.enr.clarityelections.com/{STATE_ABRV}/elections.json and by plugging the `EID` value into https://results.enr.clarityelections.com/{STATE_ABRV}/{EID}. Ex: https://results.enr.clarityelections.com/KY/95439

But what happens when you need to know the URL of upcoming election results and they haven't updated the manifest file? This simple script will attempt to find a future one by incrementing the EID and checking for a non-404 response code.

## Usage
The script has two parameters:
* STATE_ABRV (required) - state you are searching for. Ex: `python scraper.py KY`
* EID_OVERRIDE (optional) - by default the scraper will automatically find the last known good EID for you. But supplying this parameter will override that value. Ex: `python scraper.py KY 97200`


## Notes
* This can take a while to process since it increments one at a time and the span between EID's can often be in the thousands.
* Please be cool and don't DoS Clarity's website. This does a each request sequentially with a default delay of 1/4 second in between. It will stop after 4000 unsuccesful attempts. Use your best judgment here on whether to continue after 4000 if you think one exists.
* There does not appear to be a clear set time of when pages go up in advance. We have witnessed a page made available at least 11 days before election night. Obviously don't try to use this months in advance.
