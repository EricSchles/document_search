## Summary of functionality

This is a generalized search tool built on top of elastic search.  It will ingest documents, analyze their type and then make them searchable.  At this point, only full word search with correct spelling is supported, but other features will be added to allow for fuzzy search, partial words, etc.

##How to install:

`sudo pip install -r requirements.txt`

Next you'll need ocropy - this handles OCR

I'm going to recommend my fork because it includes a little more than the original library:

https://github.com/EricSchles/ocropy

You'll need to follow the installation documentation in the README.md in that repo to finish out the installation.  Make sure to run the tests, otherwise things might not work.

You'll also need elasticsearch running locally - for that you'll need to install elastic search.  I'm going to recommend the official docs:

https://www.elastic.co/guide/en/elasticsearch/guide/master/getting-started.html

But you can also find lots of great guides, here are a few for getting set up:

https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-14-04

https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-ubuntu-14-04

For Mac OSX you'll need to follow: http://stackoverflow.com/questions/22850247/installing-elasticsearch-on-osx-mavericks

You'll also need poppler-utils:

To get this on ubuntu - https://poppler.freedesktop.org/

To get this on mac osx - brew install poppler

##Using this tool

To run this tool you'll need to do 

`python run.py` from the root directory of this repo

Then head over to [http://localhost:5000](http://localhost:5000)

Now that you have all your installation out of the way you're ready to start uploading documents for indexing.  Right now I only have a web interface for doing this, but feel free to take my code and build on it.  

Some advice:

If you're going to upload pdf's that aren't ocr'ed you'll need to upload them as .png's - the tool will take it from there.
