![Plot](/plot.png?raw=true)

For ethical reasons I have excluded all of the raw data.
To use this repo you will have to obtain it yourself, which you can do like so:

Go to the Crunchbase page for each company you are interested in.
Press select-all, copy, and paste the page content into
data_collection/crunchbase_dumps/<company-name>.txt

Then you should be able to run the data pipeline by running each python file:

```
python3 _1_parse_crunchbase.py
python3 _2_merge.py
python3 _3_numbers.py
```

Finally insert `const companies =` at the beginning of the final json file and save as
`companies.js` in the root directory.
