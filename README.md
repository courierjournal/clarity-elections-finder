# Clarity Elections Finder

Clarity Elections is a great resource for data on election night. You can typically find past elections hosted on Clarity by using the following endpoint: https://results.enr.clarityelections.com/{STATE_ABRV}/elections.json and by plugging the `EID` value into https://results.enr.clarityelections.com/{STATE_ABRV}/{EID}.

But what happens when you need to know where upcoming election results will be and they haven't updated that manifest file? This simple script will attempt to find a future one by incrementing the EID.

## Usage
The script has two parameters:
* STATE_ABRV (required) - state you are searching for. Ex: `python scraper.py KY`
* EID_OVERRIDE (optional) - allows you to manually specify the EID to start at. Ex: `python scraper.py KY 97200`


## Notes
* This can take a while to process since it increments one at a time and the span between elections can be in the thousands.
* Be cool and please don't DoS Clarity's website. This does a request sequentially with a default pause of 1/4 second delay in between. It will stop after 4000 unsuccesful attempts. Use your best judgment here on whether to continue after 4000.
* There does not appear to be a clear set time of when pages go up in advance. We have witnessed a page made available at least 11 days before election night. Obviously don't try to use this months in advance.