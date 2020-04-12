def check_unique(string):
    ascii_kinds = 128
    if len(string) > ascii_kinds:
        return False 
    else:
        ascii_bool_list = [False for _ in range(ascii_kinds)]
        for letter in string:
            ascii_number = ord(letter)
            ascii_bool = ascii_bool_list[ascii_number]
            if not ascii_bool:
                ascii_bool_list[ascii_number] = True
            else:
                return False 
        return True 


if __name__ == "__main__":

    def assert_status(bool_status):
        if bool_status:
            return 'OK!'
        else:
            return 'Failed'

    print('-------TEST-------')
    print('CASE 1: ', assert_status(check_unique('aaa') == False))
    print('CASE 2: ', assert_status(check_unique('ajifpw') == True))
    print('CASE 3: ', assert_status(check_unique('ngjkes.bgjafn;') == False))
    print('CASE 4: ', assert_status(check_unique('ngjae;ongjv;anejigers;gn.sln.gjlns.gnfjelsbgjkvbsgjv.bnsjnjkdsl;bgairweghuuui;') == False))