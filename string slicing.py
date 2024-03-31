#string slicing
    #index[]
    #slice()
    #[start:stop:step]
name="thanasis meow"

firstName=name[0:8]     #thanasis
print(firstName)

lastName=name[9:13]
print(lastName)         #meow

crazyName=name[::2]
print(crazyName)        #taai ew

reversedName=name[::-1]
print(reversedName)     #woem sisanaht


#slice()
url1="http://google.com"
url2="http://facebook.com"
slice=slice(7,-4)
print(url1[slice])      #google
print(url2[slice])      #facebook
