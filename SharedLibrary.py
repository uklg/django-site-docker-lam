#!/usr/bin/python3

# can share this by appending its path to anther app

import urllib.request


class ParseLine:


  def get_accessport(self):

    fd=open('build','r')
    lines=fd.readlines()
    fd.close()


    ACCESSPORT=None

    for l in lines:
      if 'accessport=' in l:
        ACCESSPORT=(l.split('=')[-1].strip())
    
    return(ACCESSPORT)


class TestURL:


  errors=0
  tests=0


  def get_url(self,  port):

    self.URL="http://127.0.0.1:%s" % str(port)

    return self.URL



  def get_response(self,url):

    response=urllib.request.urlopen(url)
    #help(response)
    code=response.getcode()
    responselines=response.read()
    return [code,responselines]


 
  def check_return_code(self,code):
    if code !=200:
      print('error code not 200')
      self.errors +=1




  def caseless_match(self,searchstring,contenttosearch):
    if searchstring.casefold() in str(contenttosearch).casefold():
      return True
    else:
      return False



  def execute(self,port=8003):

    url=self.get_url(8003)
    print(url)
    responselines=self.get_response(url)[1]
    


    if not self.caseless_match('nextArrow',responselines):
      print('Cannot find string')
      self.errors +=1

    if not self.caseless_match('Professional wedding DJ',responselines):
      print('Cannot find string')
      self.errors +=1

    print("This is a test that checks certain http requests are correct")
    print("errors: %s" % self.errors )
    #print("total errors: %s out of %s" % len(errors))


#  if __name__ == '__main__':
#    main()

