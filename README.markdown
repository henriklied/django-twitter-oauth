# django-twitter-oauth
**Live example can be seen [@fourmargins.com/labs/twitter_oauth/](http://fourmargins.com/labs/twitter_oauth/)!**

([Original snippet](http://www.djangosnippets.org/snippets/1353/) based on [Simon Willison's Fire Eagle views](http://www.djangosnippets.org/snippets/655/) )

## Requirements
- Django 1.0 (or trunk)
- Twitter oAuth closed beta invite

## Installation
Add the 'twitter_app' directory somewhere on your 'PYTHONPATH', put it into 'INSTALLED_APPS' in your settings file.
Fill in your CONSUMER_KEY and CONSUMER_SECRET either in 'twitter_app/utils.py' or in your settings file.
Include 'twitter_app.urls' in your base 'urls.py'

You're good to go!

## API Usage
Use the API resources listed on the [REST API Documentation](http://apiwiki.twitter.com/REST+API+Documentation).
I've currently implemented two functions, which you can see in the end of twitter_app/utils.py.

Here's how you might implement a delete method:

	def delete_status_message(consumer, connection, access_token, tweet_id):
		oauth_request = request_oauth_resource(consumer, 'http://twitter.com/statuses/destroy/%s.json' % tweet_id, access_token)
	    json = fetch_response(oauth_request, connection)
	    return json


Then, in your views.py, you could define a simplistic function like so:
	def delete_tweet(request, tweet_id):
		access_token = request.session.get('access_token', None)
	    if not access_token:
	        return HttpResponse("You need an access token!")
	    token = oauth.OAuthToken.from_string(access_token)   
	    
		message = delete_status_message(CONSUMER, CONNECTION, token, tweet_id)
		if message:
			message = simplejson.loads(message)
		return return render_to_response('twitter_app/delete_tweet.html', {'message': message})

