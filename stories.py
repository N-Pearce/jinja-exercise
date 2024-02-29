"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

stories = [
    story,
    Story(["place", "noun", "verb", "adjective", "plural_noun"],
          """I was in my {place} one day when I saw a bunch of rats, and I think one of them was holding a {noun}.
    It was really {adjective}, but the rat dropped it when a chef started throwing a bunch of {plural_noun} at it"""),
    Story(["place", "noun", "verb", "adjective", "plural_noun"],
          """I had a dream once that I was at {place}. There were a lot of {plural_noun} there, 
    but the {adjective} {noun} told me not to {verb} them.""")
]
