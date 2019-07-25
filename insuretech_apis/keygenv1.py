import  string
import random
SEQ = string.ascii_uppercase + string.digits
def shake(seq,n):
    randomstr = (','.join(random.choice(seq) for _ in range(n))).split(',')
    for i in range(n):
        random.shuffle(randomstr)
    return ''.join(randomstr)
def main( pattern_no,str_len,count=1000):
    
    keygen = lambda :'-'.join(shake(SEQ,pattern_no) for _ in range(str_len))
    keygen2 = lambda: ''.join(shake(SEQ, pattern_no) for _ in range(str_len))
    table=[keygen() for i in range(count)]
    return keygen2()
    #print("\nCreated {} serial keys!".format(count))

if __name__ == '__main__':
    main(300000,4,8)

