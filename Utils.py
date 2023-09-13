
class utils:
    def reversed(number):
        if isinstance(number,int):
            return int(str(number)[::-1])
        else:
            print("Input type is wrong")
        
    def formatter(number):
        if isinstance(number,int):
            return bin(number), oct(number)
        else:
            print("Input type is wrong")
            

