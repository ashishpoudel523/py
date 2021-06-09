post=input("\n Enter your post : ")
n1="harry"
n2="HARRY"
n3="Harry"
if(n1 in post or n2 in post or n3 in post):
    if n1.islower() or n2.isupper() or n3.istitle():
        print("\n This post is about harry")
else:
    print("\n This post is not about harry")