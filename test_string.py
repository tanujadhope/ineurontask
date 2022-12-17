import logging


class log_recor:
        def __init__(self, filename, level, format):
            self.filename = filename
            self.level = level
            self.format = format
            logging.basicConfig(filename=self.filename,
                                level=self.level,
                                format=self.format)

        def log(self, message, method):
            '''
            logging the message based on the method passed in this function in the file
            '''
            if method == 'INFO':
                logging.info(message)
            else:
                logging.error(message)

class stringtask :
     def __init__(self,mystring):
         self.mystring = mystring
         self.logger_string = log_recor('stringlog_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

     def vowels_extract(self):
         '''  Extracting Vowles from a given string '''
         self.logger_string.log('String extraction operation started','INFO')
         v=[]
         try:
             for i in self.mystring:
                 if i in  [ 'a','A','e','E','i','I','o','O','u','U']:
                     v.append(i)
             self.logger_string.log('vowels now extracted', 'INFO')
             return v
         except Exception as e:
             self.logger_string.log('Error in vowel extraction')

     def string_read(self):
         '''  Extracting Vowles from a given string '''
         self.logger_string.log('Reading strings letters with predefined oreder','INFO')

         try:
             s1=self.mystring[0:300:3]
             self.logger_string.log('vowels now extracted', 'INFO')
             return s1
         except Exception as e:
             self.logger_string.log('Error in reading letters in string with predefined order')

     def string_reverse(self):
         try:
             s2=self.mystring[::-1]
             self.logger_string.log('String reversed','INFO')
             return s2
         except Exception as e:
             self.logger_string.log('String reversed failed')
             self.logger_string.log('e',"error")
     def string_upper_split(self):
         try:
            s3=self.mystring.upper()
            s4=s3.split('R')
            self.logger_string.log('String Splitted based on R letter after uppercase conversion', 'INFO')
            return s4
         except Exception as e:
             self.logger_string.log('Error in String split opeartion based on R letter')
             self.logger_string.log('e', "error")

     def string_exch(self):
         self.logger_string.log("string exchange started",'INFO')
         try:
             s5 = self.mystring
             s5=s5.replace('Python','MATLAB')
             self.logger_string.log("String Exchange Successful",'INFO')
             return s5

         except Exception as e:
             self.logger_string.log('e','Error')


mystring="this is My First Python programming class and i am learNING Python string and its function"
s_var=stringtask(mystring)
print('1.The String Vowel extraction:',s_var.vowels_extract())
print('2.The string letter reading in order:',s_var.string_read())
print('3.String without using reverse function:',s_var.string_reverse())
print('4.split a string using R letter after conversion of entire string in uppercase:',s_var.string_upper_split())
print('5.String Exchange:',s_var.string_exch())




