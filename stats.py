
def get_num_words(text):
    words = text.split()
    return len(words)



def get_chars_dict(text):
  chars = {}
  for c in text:
     lowered_character = c.lower()
     if lowered_character  in chars:
        chars[lowered_character] += 1
     else:
        chars[lowered_character] = 1
  return chars

def sort_on(items):
   return items['num']

def chars_dict_to_sorted_list(num_char_dict):
    sort_list = []
    for ch in num_char_dict:
       sort_list.append({'char':ch, "num": num_char_dict[ch]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list