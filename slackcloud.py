#! /usr/bin/env python

import os
import time
import logging

import matplotlib.pyplot as plt
from flask import Flask
from flask_slack import Slack
from slacker import Slacker
from wordcloud import WordCloud


app = Flask(__name__)

# Used for flask_slack @slack.command helper
slack = Slack(app)
app.add_url_rule('/', view_func=slack.dispatch)

# Change log level to increase or decrease verbosity
logging.basicConfig(level=logging.INFO)

# Load up custom Slack environment variables
slack_auth = os.environ.get('SLACK_AUTH')
slack_teamid = os.environ.get('SLACK_TEAMID')
slack_cmd1_name = os.environ.get('SLACK_CMD1_NAME')
slack_cmd1_token = os.environ.get('SLACK_CMD1_TOKEN')


def upload_wordcloud(channel_id, channel_name):
    slack = Slacker(slack_auth)

    # Grab last 100 messages in channel_id
    msgs = [i['text'] for i in slack.channels.history(channel_id).body['messages']]
    logging.debug(msgs)
    try:
        # Concat all the words
        text = ' '.join(msgs)
        wordcloud = WordCloud().generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.savefig('/tmp/' + channel_name)
        slack.files.upload('/tmp/' + channel_name + '.png', channels=channel_id)
        time.sleep(1.1)
    except TypeError as e:
        logging.error(e)


@slack.command(command=slack_cmd1_name, token=slack_cmd1_token,
               team_id=slack_teamid, methods=['POST'])
def parse_slash_cmd(**kwargs):
    ch_id = kwargs.get('channel_id')
    ch_name = kwargs.get('channel_name')
    upload_wordcloud(ch_id, ch_name)
    return slack.response('Generating wordcloud from the last 100 words...')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8081)
