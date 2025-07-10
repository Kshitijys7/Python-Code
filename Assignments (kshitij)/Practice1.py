def sorthead(byte_arr):
    if(byte_arr[0]==68):
        resp_num=-2
        data_out={}
        resp_num+=1
        data_out[resp_num]={}

    curr_port=int(byte_arr[1])

    data_out[resp_num]=curr_port
    print('success')

bytearray=[68,7,9]
sorthead(bytearray)