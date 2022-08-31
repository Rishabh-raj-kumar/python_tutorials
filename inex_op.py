#dictionaries -> a changeable unordered collection of key..
 # value pairs fast because they use hashing

capitals={'india':'delhi',
          'china':'beijing',
          'russia':'moscow',
          'amrica':'usa'}
print(capitals)

#access keys ..
print(capitals.keys())

#access values..
print(capitals.values());

#check wether a key is present or not..
print(capitals.get("german"))

#insert new values..
capitals.update({'france':'samp'});
print(capitals)

#remove  element..
print(capitals.pop('france'));

#clear elements..
capitals.clear()
print(capitals);

#index operator[] -> give access to a sequence element
name = "ghanta"
print(name[0:3].upper())
print(name[3:6].lower())