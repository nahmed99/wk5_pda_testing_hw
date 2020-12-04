### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:    # double '=' required for comparison; '=='
      return True
    else                  # else clause needs a colon ':'
      return False
   

  dif highest_card(self, card1 card2):    # comma missing between card1 and card2, and "dif" should be "def"
  if card1.value > card2.value:           # if block should be indented
    return card                           # card isn't defined for use in this block/scope.
  else:
    return card2
  


def cards_total(self, cards):           # the function 'header' needs to be indented!
  total                                 # No value assigned to variable 'total'
  for card in cards:
    total += card.value
    return "You have a total of" + total    # return should be un-indented + need to convert 'total' to string
  
```
