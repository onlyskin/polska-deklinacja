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
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    M_ANIMATE: {
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    M_INANIMATE: {
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    FEMININE: {
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    NEUTER: {
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    MIXED: {
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    },
                u'dwa': {
                    M_HUMAN: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    M_ANIMATE: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    M_INANIMATE: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    FEMININE: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    NEUTER: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    MIXED: {
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                    },
                }
        self._dictionary = {
                u'filozof': {
                    GENDER: M_HUMAN,
                    SINGULAR: {
                        NOMINATIVE: u'filozof',
                        ACCUSATIVE: u'filozofa',
                        GENITIVE: u'filozofa',
                        DATIVE: u'filozofowi',
                        INSTRUMENTAL: u'filozofem',
                        LOCATIVE: u'filozofie',
                        },
                    PLURAL: {
                        NOMINATIVE: u'filozofowie',
                        ACCUSATIVE: u'filozofów',
                        GENITIVE: u'filozofów',
                        DATIVE: u'filozofom',
                        INSTRUMENTAL: u'filozofami',
                        LOCATIVE: u'filozofach',
                        },
                    },
                u'kot': {
                    GENDER: M_ANIMATE,
                    SINGULAR: {
                        NOMINATIVE: u'',
                        ACCUSATIVE: u'',
                        GENITIVE: u'',
                        DATIVE: u'',
                        INSTRUMENTAL: u'',
                        LOCATIVE: u'',
                        },
                    PLURAL: {
                        NOMINATIVE: u'',
                        ACCUSATIVE: u'',
                        GENITIVE: u'',
                        DATIVE: u'',
                        INSTRUMENTAL: u'',
                        LOCATIVE: u'',
                        },
                    },
                u'dom': {
                    GENDER: M_INANIMATE,
                    SINGULAR: {
                        NOMINATIVE: u'',
                        ACCUSATIVE: u'',
                        GENITIVE: u'',
                        DATIVE: u'',
                        INSTRUMENTAL: u'',
                        LOCATIVE: u'',
                        },
                    PLURAL: {
                        NOMINATIVE: u'',
                        ACCUSATIVE: u'',
                        GENITIVE: u'',
                        DATIVE: u'',
                        INSTRUMENTAL: u'',
                        LOCATIVE: u'',
                        },
                    },
                u'ryba': {
                        GENDER: FEMININE,
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                u'jezioro': {
                        GENDER: NEUTER,
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                u'dziecko': {
                        GENDER: MIXED,
                        SINGULAR: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        PLURAL: {
                            NOMINATIVE: u'',
                            ACCUSATIVE: u'',
                            GENITIVE: u'',
                            DATIVE: u'',
                            INSTRUMENTAL: u'',
                            LOCATIVE: u'',
                            },
                        },
                }

    def random_word(self):
        return random.choice(self._dictionary.keys())

    def decline(self, word, case, number, gender=None):
        if word in self._gendered_dictionary.keys():
            forms = self._gendered_dictionary[word].get(gender).get(number).get(case)

        else:
            url = u'https://lektorek.org/lapi/v1/public/index.php/polish/grammar/search/noun/{}'.format(word)
            response = requests.get(url)
            forms = response.json()[0]
            return forms.get(lektorek_key(number, case))

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
