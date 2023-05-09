#reverse

def rev(num):
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
        print(rev)

rev(1142)
rev(1240)
rev(500264)
