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

class list_task :
    def __init__(self,mylist):
        self.mylist = mylist
        self.logger_list = log_recor('listlog.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')

    def list_reverse(self):
        try:
            l2 = self.mylist[::-1]
            self.logger_list.log('list reversed', 'INFO')
            return l2
        except Exception as e:
            self.logger_list.log('list reversed failed')
            self.logger_list.log('e', "error")
    def list_dict_extract(self):
        try:
            self.logger_list.log('Dict extraction from list started', 'INFO')
            d=self.mylist
            c= list(d[8].values())
            self.logger_list.log('Dict extraction from list completed', 'INFO')
            return c
        except Exception as e:
            self.logger_list.log('Dict extraction from list failed','Error')

    def list_list_extract(self):
        try:
            self.logger_list.log('List to list element extraction started','INFO')
            l2=self.mylist
            l3 = []
            for i in l2:
                if type(i) == list:
                    l3.append(i)
            self.logger_list.log('List to list element extraction completed', 'INFO')
            return l3
        except:
            self.logger_list.log('Dict extraction from list failed', 'Error')

    def list_comb(self):
        try:
            self.logger_list.log('element  extraction from list started', 'Error')
            l3=self.mylist
            l4 = []
            for i in l3:
                if type(i) == list:
                    l4.extend(i)
                if type(i) == dict:
                    k = i.values()
                    l4.extend(k)
                if type(i) == int or type(i) == str:
                    l4.append(i)
            self.logger_list.log('All element extracted', 'INFO')
            return l4
        except Exception as e:
            self.logger_list.log('Element extraction from list failed', 'Error')
####
list1= [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
mylist_var=list_task(list1) ### creating object for list class
print('1. Reverse the list',mylist_var.list_reverse())  ### calling reverse function
print('2. extract all the value element form dict available in list',mylist_var.list_dict_extract())
print('3. extract only a list collection form list',mylist_var.list_list_extract())
print ('4. Extract all elemnts in the list',mylist_var.list_comb())