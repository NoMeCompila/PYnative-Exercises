import re
import pprint
text = """Lorem ipsum! dolor? sit! amet. consectetur adipiscing elit. Maecenas ornare augue 
in ex finibus imperdiet. Suspendisse at fringilla nunc, in iaculis eros. 
Sed quis est ac mi auctor hendrerit at sed massa. Nulla facilisi. 
Aenean id magna sollicitudin, facilisis mi sed, malesuada ex. Fusce at nunc nec 
justo suscipit lobortis. Praesent quam leo, sollicitudin at nibh nec, volutpat 
sagittis libero. Praesent ultricies ipsum ac massa lacinia, eu pharetra ligula 
semper. Integer tincidunt sit amet metus feugiat malesuada.
"""


def generate_list(l1):
    return re.findall(r"\w+", l1)


def word_counter(list1):
    d = {}
    for i in list1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


splite_text = generate_list(text)
counter_text = word_counter(splite_text)

print(counter_text)

ordered_words = sorted(counter_text.items(), key=lambda x: x[1], reverse=True)

print(ordered_words)
