# slack_post_python

To create new app, you need to go to: https://api.slack.com/apps

Sign in/Chose Your apps/Create new app/Define app name/Chose workspace

Chose the prefered feature (i.d. incoming webhooks).

Turn on the feature.

Add new web hook to a workspace.

Chose prefered #channel to which you would like to post content and authorize.

Copy the url: https://hooks.slack.com/services/xxxxxxxxx/xxxxxxx/xxxxxxxxxxx

Paste the url to config.py
url = "https://hooks.slack.com/services/xxxxxxxxx/xxxxxxx/xxxxxxxxxxx"
secret ="xxxxxxxxx/xxxxxxx/xxxxxxxxxxx"

You are ready to go.
