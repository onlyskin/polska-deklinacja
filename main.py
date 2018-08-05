#-*- coding: utf-8 -*-
import random

html_template = '''
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <div style="font-size: 2rem; font-family: 'sans-serif';">{}</div>
  </body>
</html>
'''

def execute(event, context):
    print 'in lambda'
    print event
    phrase, number, noun = get_question()
    content = '{}: {} {}'.format(phrase, number, noun)

    response = {
        "statusCode": 200,
        "body": html_template.format(content),
        "headers": {
            'Content-Type': 'text/html',
        },
    }

    return response

def get_question():
    nouns = [u'filozof', u'kot', u'dom', u'ryba', u'jezioro', u'dziecko']
    numbers = [u'1', u'2']
    phrases = [u'Jest/są', u'Widzę', u'Nie mam', u'Daj', u'Mieszkam z', u'Myślę o']
    return map(random.choice, [phrases, numbers, nouns])
