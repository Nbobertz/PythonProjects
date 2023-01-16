alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


end = False
while end != True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  #decoding definition
  def decrypt():
    old_word = input("What was the word you were given?\n").lower()
    new_word = []
    shift_amount = int(input("What was the shift you were given?\n"))
    shift_amount = shift_amount*-1
    old_list = list(old_word)
    for n in old_list:
      variable = alphabet.index(n)
      new_letter = alphabet[variable+shift_amount]
      new_word += new_letter
    new_word = "".join(new_word)
    print(new_word)
  #encrypt definition
  def encrypt(text, shift):
    new_word = []
    text_list = list(text)
    for n in text_list:
      variable = alphabet.index(n)
      new_letter = alphabet[variable+shift]
      new_word += new_letter
    new_word = "".join(new_word)
    print(f"Send the word {new_word} to the other party along with this shift amount of {shift}")
    
  
  #this is logic for decoding
  if direction == "decode":
    decrypt()
    end = True
  if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
    end = True

