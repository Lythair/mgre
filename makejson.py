import json

tumblrs = {
  'male': ['femfreq.tumblr.com', 'the-daily-feminist.tumblr.com', 'carolrossettidesign.tumblr.com', 'fuck-yeah-feminist.tumblr.com', 'plannedparenthood.tumblr.com'],
  'female': ['femfreq.tumblr.com', 'plannedparenthood.tumblr.com', 'whoneedsfeminism.tumblr.com', 'lacigreen.tumblr.com', 'bitchsandwich.tumblr.com'],
  'unicorn': ['theunicornverse.tumblr.com', 'drawingunicorns.tumblr.com']
}


with open('tumblr_dictionary.json', 'w') as outfile:
    json.dump(tumblrs, outfile)