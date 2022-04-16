# PlurPoll
_An internal survey tool for plural systems._

Conveniently also a way for me to learn to use python's pattern matching!

On running the program, the input is prompted for a question, then any number of responses. Responses are ended by submitting an empty string.
Voters can vote with "vote [-n $name] <response numbers>". duplicate names will not be rejected.

Votes should optionally start with a name, then be a list of whitespace separated numbers. Each number is the one-indexed index of an option you are voting for. E.G.: `-n Aegis 2 3 5` would add one to the vote totals for options 2, 3, and 5, and add Aegis to the list of voters. `2 3 5` would increment the vote totals and not add any names to the list of voters.
