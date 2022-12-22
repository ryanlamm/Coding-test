import aiofiles
import asyncio
import nest_asyncio
class LogComponent:
    def __init__(self, file_name):
        self.file_name = file_name
    
    async def write_file(self, msg):
        async with aiofiles.open("{}.txt".format(self.file_name), mode='a') as text_file:
            await text_file.write(msg+"\n")
    
    def run(self,list_of_strings):
        loop = asyncio.get_event_loop()
        nest_asyncio.apply()
        for string in list_of_strings:
            loop.run_until_complete(self.write_file(string))


#Unit test:

if __name__=='__main__':
    # Scenario 1: A call to run will end up in writing something
    testing = LogComponent('test')
    list_of_strings = ['f1','f2','f3','f4']
    testing.run(list_of_strings)
    # Output: file with 'f1','f2','f3','f4'



