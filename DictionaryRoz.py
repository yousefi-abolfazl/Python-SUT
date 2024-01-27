#soaldictionaryRoz2
class RoseDictionary(dict):
    dict_roz = {}
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.dict_roz[key] = value
    def pop_item(self, raise_error = False, error_msg = '', default = ''):
        try:
            for i, j in enumerate(self.dict_roz):
                if i == len(self.dict_roz) - 1:
                    last_value = self.dict_roz[j]
                    del self.dict_roz[j]
                    return last_value
        except:
            if raise_error == True:
                raise KeyError(error_msg)
            elif raise_error == False and error_msg != '':
                return error_msg
            elif raise_error == False and default == '':
                return print('Dictionary was empty and no default value/message was specified.')
            else:
                return default
    def get_item(self, key, raise_error = None, error_msg = '', default = ''):
        try:
            return self.dict_roz[key]
        except:
            if raise_error == True:
                raise KeyError(error_msg)
            elif raise_error == None and error_msg != '':
                return error_msg
            elif raise_error == None and default == ''  and error_msg == '':
                return print('Value was not found and no default value/message was specified.')
            else:
                return default
#clean_code