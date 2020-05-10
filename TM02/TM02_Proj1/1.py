dic={'Bill':'Co-Founded Microsoft.',
     'Plato':'Helped to lay the foundations of natural philosophy.',
     'Jiano':'A pioneer in Chinese rock music.',
     'Lenin':'A Russian revolutionary',
     'Korchagin':'The hero of the book How the Steel Was Tempered.',
     'Clinton':'Served as the 42nd President of the United States.',
     'Peter':'Carried out a policy of modernization and expansion.'}
for z in dic:
    print(z,':',dic[z])
print('\n')
dic['Clinton']='soccer Player'
for z in dic:
    print(z,':',dic[z])
dic['Arun']='Player'
for z in dic:
    print(z,':',dic[z])