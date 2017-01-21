#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandFortune():
    fortunes = [
        "Things will always go bump in the night",
        "Not to alarm you, but your hair is on fire",
        "Cats do <em>not</em> like baths... even with soft music and Lush bath bombs",
        "The Glow Cloud is your friend - all hail the Glow Cloud!",
        "There seems to be an absence of a certain ornithological piece...",
        "Your dog is probably spying on you",
        "Your cat is definitely <em>not</em> spying on you",
        "The person behind you is rather disappointed",
        "Your parrot is currently at home, trying on your clothes",
        "The number 42 is the answer to Life, the Universe, and Everything",
        "Help! I'm a prisoner in a fortune cookie factory!"
    ]

    your_fortune = str(random.choice(fortunes))

    return your_fortune

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = getRandFortune()
        fortune_sentence = "<p>Your fortune:<br /><strong>" + str(fortune) + "</strong>"

        lucky_number = random.randint(1, 100)
        number_sentence = "<p>Your lucky number:<br /><strong>" + str(lucky_number) + "</strong></p>"

        cookie_again_button = "<a href='.'><button>Another cookie please!</button></a>"

        content = header + fortune_sentence + number_sentence + cookie_again_button

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
