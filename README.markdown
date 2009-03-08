# django-twitter-oauth
**Live example can be seen [@fourmargins.com/labs/twitter_oauth/](http://fourmargins.com/labs/twitter_oauth/)!**


## Requirements
- Django 1.0 (or trunk)
- Twitter oAuth closed beta invite

## API Usage
Use the API resources listed on the [REST API Documentation](http://apiwiki.twitter.com/REST+API+Documentation).
I've currently implemented two functions, which you can see in the end of twitter_app/utils.py.

**Example:**

	def delete_status_message(consumer, connection, access_token, tweet_id):
		oauth_request = request_oauth_resource(consumer, 'http://twitter.com/statuses/destroy/%s.json' % tweet_id, access_token)
	    json = fetch_response(oauth_request, connection)
	    return json


## Installation
Add the 'twitter_app' directory somewhere on your 'PYTHONPATH', put it into 'INSTALLED_APPS' in your settings file.
Fill in your CONSUMER_KEY and CONSUMER_SECRET either in 'twitter_app/utils.py' or in your settings file.
Include 'twitter_app.urls' in your base 'urls.py'

You're good to go!