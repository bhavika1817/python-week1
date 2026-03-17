
class functions:

    def Subfields():
        print("Sub-fields in AI are:")
        fields=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for i in fields:
            print(i)
            
    def OddEven():
         num=int(input("Enter a number"))
         if num%2==0:
             print(num," is a even number")
         else:
              print(num," is a odd number")

    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if (gender==("male"or"Male")and age>=21):
            print("ELIGIBLE")
        elif(gender==("female"or"Female") and age>=18):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")


    def percentage():
        list=[1,2,3,4,5]
        overall=0
        for i in list:
            mark=int(input(f"Subject {i}"))
            overall=overall+mark

        total=overall
        percentage=overall/len(list)

        print("Total:", total)
        print("Percentage:", percentage)


    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of triangle:", area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        peri=height1+height2+breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",peri)

