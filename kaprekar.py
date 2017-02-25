# https://www.reddit.com/r/dailyprogrammer/comments/56tbds/20161010_challenge_287_easy_kaprekars_routine/
def largest_digit(input_num):
    num_list = [int(i) for i in str(input_num)]
    print(max(num_list))

def asc_digit(input_num):
    s = ''.join(sorted(str(input_num).zfill(4)))
    return str(s)

def desc_digit(input_num):
    return str(asc_digit(input_num))[::-1]

def kaprekar(input_num, kap_count = 0):
    if(input_num == 6174):
        return kap_count
    return kaprekar(int(desc_digit(input_num)) - int(asc_digit(input_num)), kap_count + 1)


# largest_digit(1234)
# desc_digit(1234)
print(kaprekar(5455))