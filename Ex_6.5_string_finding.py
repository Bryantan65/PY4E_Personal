text = "X-DSPAM-Confidence:    0.8475"

number = text.find(":")
#find the text starting from :

#piece is equal  to the position of the text from : onwards, in this case it is : and 3 spaces , so position 21 + 3 = 24 sth like that, : means print from here to thr, if i just put that 1 numb, it will print the position of that one charaac
piece = text[number+4:]
print(float(piece))