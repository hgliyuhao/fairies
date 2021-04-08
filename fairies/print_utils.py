import datetime

def print_to_log(out_put):   
    
    # 增量写入

    log_name = 'log_' + datetime.datetime.now().strftime('%Y') + '_' + datetime.datetime.now().strftime('%m') + '_' + datetime.datetime.now().strftime('%d') + '.txt'

    try:

        man_out = open(log_name,"a")
        print('Log',out_put,file=man_out)
        man_out.close()

    except IOError:
        print ('data file is not exist')
