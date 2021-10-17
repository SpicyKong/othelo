class a:
    def hello(self):
        print('hello')
        
    def hi(self):
        self.hello()
    
    def __repr__(self):
        return 'repr'
test = [a(), a(), a()]
#test.hi()
print(test)