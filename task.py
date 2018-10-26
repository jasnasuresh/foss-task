from PIL import Image 
print("SHOPPING CART")
print("here are some categories")
list=["clothing","shoes","watches","books"]
print("select one from these categories:")
print("1=clothing")
print("2=shoes")
print("3=watches")
print("4=books")
print("enter yes to shop no to exit")
total=[]
cart=[]
b=input()
while(b=="yes"):
    print("select either a category or enter 0 to exit")
    c=int(input())
#c=category
    if(c==0):
        break
    if(c==1):
        print("select for girls or boys")
#a=gender
        a=input()
        if(a=="girls"):
            print("select 1 for tops ")
            print("select 2 for leggings ")
            print("select 3 for jeans")
            print("discount offer is 10%")
        if(a=="boys"):
            print("select 4 for t-shirts")
            print("select 5 for formal shirts")
            print("select 6 for boys jeans")
            print("discount offer is 10%")
        d=int(input())
        if(d==1):
            img=Image.open("/home/hp/Desktop/images/top.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/top1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/top2.jpeg")
            img2.show()
            img2.close()
            print("which top do u want??")
            print("1 for red top")
            print("2 for blue top")
            print("3 for white top")
            m=int(input())
            if(m==1):
                price=500
            if(m==2):   
                price=1500
            if(m==3):
                price=1000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("tops")
        if(d==2):
            img=Image.open("/home/hp/Desktop/images/lg.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/lg1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/lg2.jpeg")
            img2.show()
            img2.close()
            print("which legging do u want??")
            print("1 for black legging")
            print("2 for pink legging")
            print("3 for white legging")
            n=int(input())
            if(n==1):
                price=500
            if(n==2):   
                price=1000
            if(n==3):
                price=1500
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("leggings")
        if(d==3):
            img=Image.open("/home/hp/Desktop/images/jeans.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/jeans1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/jeans2.jpeg")
            img2.show()
            img2.close()
            print("which jeans do u want??")
            print("1 for black jeans")
            print("2 for pink jeans")
            print("3 for white jeans")
            o=int(input())
            if(o==1):
                price=500
            if(o==2):   
                price=1000
            if(o==3):
                price=2000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("jeans")
        if(d==4):
            img=Image.open("/home/hp/Desktop/images/ts.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/ts1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/ts2.jpeg")
            img2.show()
            img2.close()
            print("which t-shirt do u want??")
            print("1 for black t-shirt")
            print("2 for red t-shirt")
            print("3 for white t-shirt")
            p=int(input())
            if(p==1):
                price=5000
            if(p==2):   
                price=3000
            if(p==3):
                price=2000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("t-shirts")
        if(d==5):
            img=Image.open("/home/hp/Desktop/images/fs.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/fs1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/fs2.jpeg")
            img2.show()
            img2.close()
            print("which formal-shirt do u want??")
            print("1 for black formal-shirt")
            print("2 for blue formal-shirt")
            print("3 for white formal-shirt")
            q=int(input())
            if(q==1):
                price=2000
            if(q==2):   
                price=5000
            if(q==3):
                price=6000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("formal shirts")
        if(d==6):
            img=Image.open("/home/hp/Desktop/images/bj.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/bj1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/bj2.jpeg")
            img2.show()
            img2.close()
            print("which color jeans do u want??")
            print("1 for black ")
            print("2 for cream")
            print("3 for white")
            r=int(input())
            if(r==1):
                price=7000
            if(r==2):   
                price=5000
            if(r==3):
                price=6000
            k=price-float((price)*(0.1))
            print(float(k))
            cart.append("boys jeans")
        total.append(k)
    if(c==2):
        print("select for girls or boys")
        e=input()
        if(e=="girls"):
            print("select 1 for adidas-price ")
            print("select 2 for nike-price ")  
            print("select 3 for reebok-price ")
            print("discount offer is 10%")
        if(e=="boys"):
            print("select 4 for adidas-price ")
            print("select 5 for nike-price ")
            print("select 6 for puma-price")
            print("discount offer is 10%")
        f=int(input())
        if(f==1):
            img=Image.open("/home/hp/Desktop/images/ag.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/ag1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/ag2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for white")
            s=int(input())
            if(s==1):
                price=7000
            if(s==2):   
                price=10000
            if(s==3):
                price=6000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("adidas")
        if(f==2):
            img=Image.open("/home/hp/Desktop/images/nb.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/nb1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/nb2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for white")
            u=int(input())
            if(u==1):
                price=7000
            if(u==2):   
                price=10000
            if(u==3):
                price=8000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("nike")
        if(f==3):
            img=Image.open("/home/hp/Desktop/images/rg.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/rg1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/rg2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for white")
            w=int(input())
            if(w==1):
                price=7000
            if(w==2):   
                price=10000
            if(w==3):
                price=5000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("reebok")
        if(f==4):
            img=Image.open("/home/hp/Desktop/images/ag.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/ag1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/ag2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for white")
            t=int(input())
            if(t==1):
                price=7000
            if(t==2):   
                price=10000
            if(t==3):
                price=10000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("adidas")
        if(f==5):
            img=Image.open("/home/hp/Desktop/images/nb.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/nb1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/nb2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for white")
            t=int(input())
            if(t==1):
                price=7000
            if(t==2):   
                price=10000
            if(t==3):
                price=9000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("nike")
        if(f==6):
            img=Image.open("/home/hp/Desktop/images/pb.jpeg")
            img.show()
            img.close()
            img1=Image.open("/home/hp/Desktop/images/pb1.jpeg")
            img1.show()
            img1.close()
            img2=Image.open("/home/hp/Desktop/images/pb2.jpeg")
            img2.show()
            img2.close()
            print("which color shoes do u want??")
            print("1 for black ")
            print("2 for pink")
            print("3 for blue")
            t=int(input())
            if(t==1):
                price=7000
            if(t==2):   
                price=10000
            if(t==3):
                price=6000
            g=price-float((price)*(0.1))
            print(float(g))
            cart.append("puma")
        total.append(g)
    if(c==3):
        print("select for girls or boys")
        h=input()
        if(h=="girls"):
            print("select 1 for fastrack-price 5000")
            print("select 2 for titan-price 6000")  
            print("select 3 for timex-price 5000")
            print("discount offer is 10%")
        if(h=="boys"):
            print("select 4 for fastrack-price 7000")
            print("select 5 for titan-price 9000")
            print("select 6 for timex-price 6000")
            print("discount offer is 10%")
        i=int(input())
        if(i==1):
            img=Image.open("/home/hp/Desktop/images/fg.jpeg")
            img.show()
            img.close()
            price=5000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("fastrack")
        if(i==2):
            img=Image.open("/home/hp/Desktop/images/tg.jpeg")
            img.show()
            img.close()
            price=6000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("titan")
        if(i==3):
            img=Image.open("/home/hp/Desktop/images/tig.jpeg")
            img.show()
            img.close()
            price=5000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("timex")
        if(i==4):
            img=Image.open("/home/hp/Desktop/images/fb.jpeg")
            img.show()
            img.close()
            price=7000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("fastrack")
        if(i==5):
            img=Image.open("/home/hp/Desktop/images/tb.jpeg")
            img.show()
            img.close()
            price=9000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("titan")
        if(i==6):
            img=Image.open("/home/hp/Desktop/images/tib.jpeg")
            img.show()
            img.close()
            price=6000
            j=price-float((price)*(0.1))
            print(float(j))
            cart.append("timex")
        total.append(j)
    if(c==4):
        print("select 1 for harry potter")
        print("select 2 for ignited minds")
        print("select 3 for wings of fire")
        print("select 4 for my truth")
        print("select 5 for my experience with truth")
        print("select 6 for INDIA2020")
        print("discount offer is 50%")
        k=int(input())
        if(k==1):
            img=Image.open("/home/hp/Desktop/images/hp1.jpeg")
            img.show()
            img.close()
            price=5000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("harry potter")
        if(k==2):
            img=Image.open("/home/hp/Desktop/images/im1.jpeg")
            img.show()
            img.close()
            price=6000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("ignited minds")
        if(k==3):
            img=Image.open("/home/hp/Desktop/images/wf.jpeg")
            img.show()
            img.close()
            price=5000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("wings of fire")
        if(k==4):
            img=Image.open("/home/hp/Desktop/images/mt.jpeg")
            img.show()
            img.close()
            price=7000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("my truth")
        if(k==5):
            img=Image.open("/home/hp/Desktop/images/mg.jpeg")
            img.show()
            img.close()
            price=9000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append(" my experience with truth")
        if(k==6):
            img=Image.open("/home/hp/Desktop/images/i20.jpeg")
            img.show()
            img.close()
            price=6000
            l=price-float((price)*(0.5))
            print(float(l))
            cart.append("INDIA2020")
        total.append(l)
print("your cart consists of")
print(cart)
add=0
for i in range(0,len(cart)):
    add=add+total[i]
print("your total price is:")
print(add)


















