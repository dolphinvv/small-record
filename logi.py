import time
import json

class Logok():

    def foramt_time(self):

        localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        return localtime

    def start_record(self,var=None,file_path="D:/LOG/common.txt"):
        """recoed the variable change in appoint file"""
        # log_dict={}
        log_str=str(self.foramt_time())+' <=====> '+str(var)
        try:
            with open(file_path,'r') as f:
                init_info=f.read()
            record_str=init_info+'\n'+log_str
            # print record_str
            # print dump_dict
            with open(file_path,'w') as f:
                f.write(record_str)
        except:
            with open(file_path,'w') as f:
                f.write(log_str)


        # with open(file_path,'w') as f:
        #     json.dump(log_dict,f)






if __name__=='__main__':
    logok=Logok()
    logok.foramt_time()
    logok.start_record(var=43)