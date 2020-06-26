import pandas as pd

# data = pd.read_excel('3000.xls',header= None,names= ['Vocabulary', 'Definition'],encoding = "gb18030")
# print(data.head(5))
# a = data['Vocabulary'].values.tolist()
# b = data.set_index('Vocabulary').to_dict()['Definition']
# b = data['Definition'].values.tolist()
#clean
# c = []
# for i in a:
#     d = ''.join(filter(str.isalpha,i))
#     c.append(d)

# dictionary = dict(zip(c,b))

# print(c)
# print(dictionary)
# print(dictionary['amenable'])

def get_vocabulary():
    data = pd.read_excel('3000.xls',header= None,names= ['Vocabulary', 'Definition'],encoding = "gb18030")
    a = data['Vocabulary'].values.tolist()
    b = data['Definition'].values.tolist()
    c = []
    #clean vocaublary list
    for i in a:
        d = ''.join(filter(str.isalpha,i))
        c.append(d)
    dictionary = dict(zip(c,b))
    return c,dictionary
