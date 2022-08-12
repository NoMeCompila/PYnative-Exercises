import re

text = """Lorem ipsum! dolor? sit! amet.., consectetur adipiscing elit. Maecenas ornare augue 
in ex finibus imperdiet. Suspendisse at fringilla nunc, in iaculis eros. 
Sed quis est ac mi auctor hendrerit at sed massa. Nulla facilisi. 
Aenean id magna sollicitudin, facilisis mi sed, malesuada ex. Fusce at nunc nec 
justo suscipit lobortis. Praesent quam leo, sollicitudin at nibh nec, volutpat 
sagittis libero. Praesent ultricies ipsum ac massa lacinia, eu pharetra ligula 
semper. Integer tincidunt sit amet metus feugiat malesuada.
"""


def split_text(txt):
    return txt.split(" ")


def generalize(s):
    return re.sub("\!|\?|\'|\.|\,|\n", "", s.lower())



def generalize_list(l1):
    #return re.findall(r"\w+", s)
    return list(map(lambda x: generalize(x), l1))


txt1 = split_text(text)
txt2 = generalize_list(txt1)



def word_counter(list1):
    d = {}
    for i in list1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d


#print(word_counter(txt2))


def  get_moda(dic1):
    return max(dic1, key=dic1.get)


print(get_moda(word_counter(txt2)))
