#-*- coding: utf-8 -*-
import random
import requests
from constants import (SINGULAR, PLURAL, NOMINATIVE, ACCUSATIVE, GENITIVE,
        DATIVE, INSTRUMENTAL, LOCATIVE)

GENDER = u'gender'
M_HUMAN = u'mh'
M_ANIMATE = u'ma'
M_INANIMATE = u'mi'
FEMININE = u'f'
NEUTER = u'n'
MIXED = u'mix'

class Dictionary:
    def __init__(self):
        self._gendered_dictionary = {
                u'jeden': {
                    M_HUMAN: {
                        SINGULAR: {
                            NOMINATIVE: u'jeden',
                            ACCUSATIVE: u'jednego',
                            GENITIVE: u'jednego',
                            DATIVE: u'jednemu',
                            INSTRUMENTAL: u'jednym',
                            LOCATIVE: u'jednym',
                            },
                        },
                    M_ANIMATE: {
                        SINGULAR: {
                            NOMINATIVE: u'jeden',
                            ACCUSATIVE: u'jednego',
                            GENITIVE: u'jednego',
                            DATIVE: u'jednemu',
                            INSTRUMENTAL: u'jednym',
                            LOCATIVE: u'jednym',
                            },
                        },
                    M_INANIMATE: {
                        SINGULAR: {
                            NOMINATIVE: u'jeden',
                            ACCUSATIVE: u'jeden',
                            GENITIVE: u'jednego',
                            DATIVE: u'jednemu',
                            INSTRUMENTAL: u'jednym',
                            LOCATIVE: u'jednym',
                            },
                        },
                    FEMININE: {
                        SINGULAR: {
                            NOMINATIVE: u'jedna',
                            ACCUSATIVE: u'jedną',
                            GENITIVE: u'jednej',
                            DATIVE: u'jednej',
                            INSTRUMENTAL: u'jedną',
                            LOCATIVE: u'jednej',
                            },
                        },
                    NEUTER: {
                        SINGULAR: {
                            NOMINATIVE: u'jedno',
                            ACCUSATIVE: u'jedno',
                            GENITIVE: u'jednego',
                            DATIVE: u'jednemu',
                            INSTRUMENTAL: u'jednym',
                            LOCATIVE: u'jednym',
                            },
                        },
                    MIXED: {
                        SINGULAR: {
                            NOMINATIVE: u'jedno',
                            ACCUSATIVE: u'jedno',
                            GENITIVE: u'jednego',
                            DATIVE: u'jednemu',
                            INSTRUMENTAL: u'jednym',
                            LOCATIVE: u'jednym',
                            },
                        },
                    },
                u'dwa': {
                    M_HUMAN: {
                        PLURAL: {
                            NOMINATIVE: u'dwaj',
                            ACCUSATIVE: u'dwóch',
                            GENITIVE: u'dwóch',
                            DATIVE: u'dwom',
                            INSTRUMENTAL: u'dwoma',
                            LOCATIVE: u'dwóch',
                            },
                        },
                    M_ANIMATE: {
                        PLURAL: {
                            NOMINATIVE: u'dwa',
                            ACCUSATIVE: u'dwa',
                            GENITIVE: u'dwóch',
                            DATIVE: u'dwom',
                            INSTRUMENTAL: u'dwoma',
                            LOCATIVE: u'dwóch',
                            },
                        },
                    M_INANIMATE: {
                        PLURAL: {
                            NOMINATIVE: u'dwa',
                            ACCUSATIVE: u'dwa',
                            GENITIVE: u'dwóch',
                            DATIVE: u'dwom',
                            INSTRUMENTAL: u'dwoma',
                            LOCATIVE: u'dwóch',
                            },
                        },
                    FEMININE: {
                        PLURAL: {
                            NOMINATIVE: u'dwie',
                            ACCUSATIVE: u'dwie',
                            GENITIVE: u'dwóch',
                            DATIVE: u'dwom',
                            INSTRUMENTAL: u'dwiema',
                            LOCATIVE: u'dwóch',
                            },
                        },
                    NEUTER: {
                        PLURAL: {
                            NOMINATIVE: u'dwa',
                            ACCUSATIVE: u'dwa',
                            GENITIVE: u'dwóch',
                            DATIVE: u'dwom',
                            INSTRUMENTAL: u'dwoma',
                            LOCATIVE: u'dwóch',
                            },
                        },
                    MIXED: {
                        PLURAL: {
                            NOMINATIVE: u'dwoje',
                            ACCUSATIVE: u'dwoje',
                            GENITIVE: u'dwojga',
                            DATIVE: u'dwojgu',
                            INSTRUMENTAL: u'dwojgiem',
                            LOCATIVE: u'dwojgu',
                            },
                        },
                    },
                }
        self._dictionary = {
                u'filozof': { GENDER: M_HUMAN, },
                u'kot': { GENDER: M_ANIMATE, },
                u'dom': { GENDER: M_INANIMATE, },
                u'ryba': { GENDER: FEMININE, },
                u'jezioro': { GENDER: NEUTER, },
                u'dziecko': { GENDER: MIXED, },
                }

    def random_word(self):
        return random.choice(self._dictionary.keys())

    def decline(self, word, case, number, gender=None):
        if word in self._gendered_dictionary.keys():
            return self._gendered_dictionary[word].get(gender).get(number).get(case)

        else:
            if self.gender_for_word(word) == MIXED and number == PLURAL:
                decline_case = GENITIVE
            else:
                decline_case = case

            forms = self._get_forms(word)
            return forms.get(lektorek_key(number, decline_case))

    def _get_forms(self, word):
        url = u'https://lektorek.org/lapi/v1/public/index.php/polish/grammar/search/noun/{}'.format(word)
        response = requests.get(url)
        return response.json()[0]


    def gender_for_word(self, word):
        return self._dictionary[word].get(GENDER)

def lektorek_key(number, case):
    case_part = {
            NOMINATIVE: u'nom',
            ACCUSATIVE: u'acc',
            GENITIVE: u'gen',
            DATIVE: u'dat',
            INSTRUMENTAL: u'ins',
            LOCATIVE: u'loc',
            }.get(case)
    number_part = 'sg' if number == SINGULAR else 'pl'
    return u'{}_{}'.format(case_part, number_part)
