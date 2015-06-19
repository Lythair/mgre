#dicts
names_dict = {
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
}
#loops
name_input = raw_input('What is your name? ').lower()
print name_input
x = False
for key in names_dict :
  if key == name_input :
    x = True
    print name_input + ' could be'
    for gender in names_dict[key] :
      print gender
    if len(names_dict[key]) > 1 :
      truth = raw_input('Do you identify as one of these? If so, specify which one. ').lower()
    else :
      yn = raw_input('Is this correct? yes/no ').lower()
      if yn == 'yes' :
        truth = gender
      else :
        break

    break
#endgame
if x  == False :
  ask = raw_input("We're sorry, your name doesn't appear to be in our dictionary. Would you like to add it? ").lower()
  #g = raw_input('We couldn\'t find you. What is your gender?')
  names[name] = [g]
else :
  print truth + ' tumblrs :'
  for gender_key in tumblrs :
    if gender_key == truth :
      for tumblr_url in tumblrs[gender_key] :
        print tumblr_url

