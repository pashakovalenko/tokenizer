# 25 lines long tokenizer

This Python function gets a text in one string (without linebreaks) and splits it into a list of sentences (strings). In each sentence words and punctuation marks are whitespace-separated.

Example of usage:

```python
>>> import tokenizer
>>> text = """But there's one sound that no one knows... What does the fox say? \
... 'Ring-ding-ding-ding-dingeringeding!'"""
>>> tokenizer.tokenize(text)
["But there's one sound that no one knows ...", 
 'What does the fox say ?', 
 "' Ring-ding-ding-ding-dingeringeding ! '"]
```
Hope comments are not included in 25 lines =)

Some examples of work can be seen in `input.txt` -> `output.txt` and `input_alice.txt` -> `output_alice.txt`.

The whole book 'Alice in Wonderland' is processed in about 0.1 sec.
