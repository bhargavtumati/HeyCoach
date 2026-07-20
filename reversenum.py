def reverse( x: int) -> int:
        nega=False
        
        if x<0:
            nega=True
            x=x*-1
        y=0
        while x:
            y=y*10
            y=y+(x%10)
            x=int(x/10)
        if y > (2147483647) or y < (-2147483647):
                return 0
        if nega:
            return -y
        return y

print(reverse(-123))