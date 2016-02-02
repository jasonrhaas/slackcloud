# slackcloud

*slackcloud** generates word clouds using Slack chat history.  This application runs on a server that is reachable by Slack.  It is designed to be triggered by a Slack "Slash Command" that you set up.  It listens for the trigger from the "Slash command" and then grabs the history from the Slack channel it was called from.  Then it generates a word cloud and uploads it to the same channel.

## Quickstart

1.  Set up your custom slash command under the Slack "Custom Integrations" tab.  This is the command you will use to kick off a word cloud.
2.  Create your custom Bot under the Slack "Custom Integrations".  This bot is the user that will upload the word cloud picture.
3.  In your environment, add the following environment variables.  For Mac OSX, use **~/.bash_profile**.  For Ubuntu, use **~/.bash_aliases**.

```
# Slack bot token
export SLACK_AUTH='xxxx'
# Slack Team ID
export SLACK_TEAMID='xxxx'
# Slack command name
export SLACK_CMD1_NAME='xxxx'
# Slack command token
export SLACK_CMD1_TOKEN='xxxx'
```

4. Inside a virtualenv, run `pip install -r requirements.txt`.

### Mac OSX

- `pip install Pillow`
- If you try running the application in this state you will get an error message from Matplotlib complaining about running inside a virtualenv.  See [Virtualenv FAQ](http://matplotlib.org/faq/virtualenv_faq.html) for how to workaround this.

### Linux

Installing **Pillow** on Linux can be a little bit tricky and depends on the distribution and OS packages.  See [Pillow install instructions](http://pillow.readthedocs.org/en/3.0.x/installation.html#linux-installation)

5.  Inside the virtualenv, run `python slackcloud.py`.  You application by default runs on **localhost:8081**.  That port needs to be publicly accessible or forward out to port 80 or 443 by your webserver.

6. In a slack channel, type `/command` and you should be greeted by a bot responding with a word cloud!