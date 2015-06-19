#dicts
'''names_dict = {
  'garnet': ['female', 'other'],
  'amethyst': ['female'],
  'pearl': ['female'],
  'steven': ['male'],
  'stevonnie': ['other'],
  'leliana': ['female'],
  'amelia': ['male'],
  'sarah': ['male'],
  'hank': ['female'],
  'john': ['female'],
  'alex': ['male', 'female', 'other'],
  'lee': ['male', 'female', 'other'],
  'alistair': ['male', 'other'],
  'loweer': ['unicorn']
}
tumblrs = {
  'male': ['femfreq.tumblr.com', 'the-daily-feminist.tumblr.com', 'carolrossettidesign.tumblr.com', 'fuck-yeah-feminist.tumblr.com', 'plannedparenthood.tumblr.com'],
  'female': ['femfreq.tumblr.com', 'plannedparenthood.tumblr.com', 'whoneedsfeminism.tumblr.com', 'lacigreen.tumblr.com', 'bitchsandwich.tumblr.com'],
  'unicorn': ['theunicornverse.tumblr.com', 'drawingunicorns.tumblr.com']
}'''

import json, sys
with open('names_dictionary.json') as data_file:    
    names_dict = json.load(data_file)
with open('tumblr_dictionary.json') as data_file:    
    tumblrs = json.load(data_file)

#loops
name_input = raw_input('What is your name? ').lower()
print name_input
x = False
if name_input in names_dict :
  x = True
  if len(names_dict[name_input]) >= 1 :
    print "Your name is associated with the following genders: "
    for gender in names_dict[name_input]:
      print gender
    truth = raw_input('Do you identify as one of these? If so, specify which one. ').lower()
    if truth == 'no':
      truth = raw_input('What is your gender? ').lower()
      names_dict[name_input].append(truth)
      if truth not in tumblrs:
        tumblrs[truth] = []
        ask_tumblr = raw_input('Great! Please provide a link to your favorite tumblr, this will help us improve user experience for others of your gender. ').lower()
        if ask_tumblr in tumblrs:
          print "Our apologies, but that Tumblr is already in our database."
        else:
          tumblrs[truth].append(ask_tumblr)
          print "Thanks for your input! Here's our personal reccomendations for you:"
          for blog in tumblrs['unicorn']:
            print blog
          print "Thanks for using the M.G.R.E.!"
          with open('tumblr_dictionary.json', 'w') as outfile:
            json.dump(tumblrs, outfile)

          with open('names_dictionary.json', 'w') as outfile:
           json.dump(names_dict, outfile)
          exit(0)
      else:
        x = True
    else:
      print "Ok then! Bye!"
      exit(0)
  else:
    truth = raw_input('What gender do you identify as? ').lower()

#endgame
if x  == False :
  ask = raw_input("We're sorry, your name doesn't appear to be in our dictionary. Would you like to add it? ").lower()
  #g = raw_input('We couldn\'t find you. What is your gender?')
  if ask == 'yes':
    names_dict[name_input] = []
    truth = raw_input('Ok! Your name has been added. What is your gender? ').lower()
    names_dict[name_input].append(truth)
    if truth not in tumblrs:
      tumblrs[truth] = []
      ask_tumblr = raw_input('Great! Please provide a link to your favorite tumblr, this will help us improve user experience for others of your gender. ').lower()
      if ask_tumblr in tumblrs:
        print "Our apologies, but that Tumblr is already in our database."
      else:
        tumblrs[truth].append(ask_tumblr)
        print "Thanks for your input! Here's our personal reccomendations for you:"
        for blog in tumblrs['unicorn']:
          print blog
        print "Thanks for using the M.G.R.E.!"
        with open('tumblr_dictionary.json', 'w') as outfile:
          json.dump(tumblrs, outfile)

        with open('names_dictionary.json', 'w') as outfile:
         json.dump(names_dict, outfile)
        exit(0)
    else:
      x = True
  else:
    print "Ok then! Bye!"
    exit(0)

if x:
  print truth + ' tumblrs :'
  for gender_key in tumblrs :
    if gender_key == truth :
      for tumblr_url in tumblrs[gender_key] :
        print tumblr_url

with open('tumblr_dictionary.json', 'w') as outfile:
    json.dump(tumblrs, outfile)

with open('names_dictionary.json', 'w') as outfile:
    json.dump(names_dict, outfile)
