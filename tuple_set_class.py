import logging
class log_recor:
    def __init__(self,filename,level,format):
        self.filename =filename
        self.level =level
        self.format =format
        logging.basicConfig(filename=self.filename,
                            level=self.level,
                            format=self.format)

    def log(self, message, method):
        '''
        to give message based on Method

        '''
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)


class set_task:

    def __init__(self,myset):
        self.myset=myset
        self.logger_set=log_recor('setlog.txt','INFO','%(levelname)s  %(asctime)s %(name)s %(message)s')

    def value_extract(self):
        '''  Extracting values from a given set '''
        self.logger_set.log('values extraction operation started', 'INFO')

        try:
            v=self.myset
            self.logger_set.log('vowels now extracted','INFO')
            return v
        except Exception as e:
            self.logger_set.log('Error in value extraction','INFO')
            self.logger_set.log('e', 'error')

    def settolist(self):
        self.logger_set.log('Processing set to list conversion','INFO')
        try:
            s5 = list(self.myset)
            self.logger_set.log('Set to list conversion successful','INFO')
            return s5
        except Exception as e:
            self.logger_set.log('Set to list conversion unsuccessful','INFO')
            self.logger_set.log('e','error')

    def discard_val(self):
        self.logger_set.log('Processing Discard','INFO')
        try:
            s7 = self.myset
            s7 = s7.pop(6)
            return s7
            ##self.logger_set.log('Discarding element successful','INFO')
            ##return s6
        except Exception as e:
            self.logger_set.log('e','error')

    def set_to_tuple(self):
        self.logger_set.log('Procesing set to tuple ','INFO')
        try:
           s8 = self.myset
           t= tuple(s8)
           self.logger_set.log('set to tuple conversion successful', 'INFO')
           return t
        except Exception as e:
            self.logger_set.log('set to tuple conversion unsuccessful','INFO')


s1 = {3,4,4,5,6,6,7,7,8,8,9,9,0,0,0,'sudh'}
set_var = set_task(s1)
print('1.Reading value from set',set_var.value_extract())
print('2.set to list Conversion',set_var.settolist())
print('3.Discard specific element from set',set_var.discard_val())
print('4.Set to tuple conversion',set_var.set_to_tuple())