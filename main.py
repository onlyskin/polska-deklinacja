#-*- coding: utf-8 -*-
import random
from dictionary import Dictionary
from constants import (SINGULAR, PLURAL, NOMINATIVE, ACCUSATIVE, GENITIVE,
DATIVE, INSTRUMENTAL, LOCATIVE)

word_dict = Dictionary()

html_template = u'''
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <div style="font-size: 2rem; font-family: 'sans-serif';">{}</div>
    <button onclick="function() {{ document.getElementbyId('answer').style['font-size'] = '2rem';}}"
    <div id="answer" style="font-size: 0rem; font-family: 'sans-serif';">{}</div>
  </body>
</html>
'''

def execute(event, context):
    case, number, noun = get_question()
    declined_number, declined_noun = get_answer(case, number, noun)

    print case, number, noun
    print declined_number, declined_noun

    question = u'{}: {} {}'.format(
            phrase_for_case(case),
            string_for_number(number),
            noun,
            )

    answer = u'{}, {}'.format(declined_number, declined_noun)

    response = {
        u'statusCode': 200,
        u'body': html_template.format(question, answer),
        u'headers': {
            u'Content-Type': u'text/html',
        },
    }

    return response

def get_question():
    phrases = [u'Jest/są', u'Widzę', u'Nie mam', u'Daj', u'Mieszkam z', u'Myślę o']
    
    case = random_case()
    number = random_number()
    word = word_dict.random_word()

    return [case, number, word]

def random_number():
    return random.choice([SINGULAR, PLURAL])

def random_case():
    return random.choice([
            NOMINATIVE,
            ACCUSATIVE,
            GENITIVE,
            DATIVE,
            INSTRUMENTAL,
            LOCATIVE,
            ])

def get_answer(case, number, noun):
    declined_noun = word_dict.decline(noun, case, number)
    gender = word_dict.gender_for_word(noun)
    declined_number = word_dict.decline(word_for_number(number), case, number, gender)
    return [declined_number, declined_noun]

def check_plurality(numeral):
    if numeral == u'1':
        return SINGULAR
    else:
        return PLURAL

def phrase_for_case(case):
    phrases = {
            NOMINATIVE: u'Jest/są',
            ACCUSATIVE: u'Widzę',
            GENITIVE: u'Nie mam',
            DATIVE: u'Daj',
            INSTRUMENTAL: u'Mieszkam z',
            LOCATIVE: u'Myślę o',
            }
    return phrases.get(case)

def string_for_number(number):
    if number == u's':
        return u'1'
    else:
        return u'2'

def word_for_number(number):
    if number == u's':
        return u'jeden'
    else:
        return u'dwa'
