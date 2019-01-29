# Simple Tweet Processing

To run the test suite from the command line `python testParser.py`

Alternatively, run the program from the command line `python messageParser.py`
- Use the --help option at the prompt for input options.
---
**Implemented Methods**

`extract_mentions`: searches for mentions in the message argument and adds each instance to a mentions dictionary with the key as the username mentioned and the value being the number of times that user was mentioned.

`extract_topics`: functions identically to the above method but searches for topics instead.

`extract_urls`: functions identically to the above methods but for valid URL's.

`is_mentioned(username)`: returns true if the given username was mentioned in the processed tweet, false if it was not.

`times_mentioned(mention)`: returns the total number of times a given username was mentioned in the processed tweet.

`total_mentions`: returns the total number of mentions in the processed tweet as an integer.

`has_topic`: returns true if the topic given was mentioned in the processed tweet, false if it was not. 

`total_topics`: returns the total number of topics in the processed tweet as an intege.

`is_referenced(url)`: returns true if the given URL was mentioned in the processed tweet, false if it was not.

`total_url`: returns the total number of valid links in the processed tweet as an integer.
---
**Citations**
The idea and implementation for a regex that also checked for unicode characters as well as basic text comes from this Gist:
https://gist.github.com/mahmoud/237eb20108b5805aed5f

---
**What still needs doing**
-More unit tests! Specifically, write tests that use unicode @ and # to see if the regex is truly functioning properly.
-some kind of abstraction to remove the code repetition in the extract functions.
