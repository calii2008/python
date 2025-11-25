from module6.main import result

# age= 25
# print(type(age))
# age_as_str=str(age)
# print(age_as_str,"of type",type(age_as_str))
#
#
#
# x=5
# y=4.3
#
# result=x+y
# print(type(result))
# age=25
# message="i am"+ str(age) + " years old"
# print(message)
#
#
# a=5
# b="3"
# print(type(b))
# b1=int(b)
# result2=a+int(b)
# print(type(b))
# print(print2)
#
# name=input("enter your name:")
# print(f"hello,{name}")
#
# age=input("enter your age:")
# print(type(age))
#
# num1=int(input("enter the first number:"))
# num2=int(input("enter the secend number:"))
# result=num1+num2
# print(re)


try:
    result=10/2
    print(result)
except ZeroDivisionError:
    print("opps! Tierd to divide to zero")

fruits={
    "apple":5,
    "orange":7

}

try:
    print(fruits["orange"])
except KeyError:
    print("the key does not exist")

    try:
        result = 10 / 2
        print(result)
    except ZeroDivisionError:
        print("opps! Tierd to divide to zero")
finally:
    print("finally block excuted")

def divide_num(a,b):
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("invalid division by zero")
    except TypeError:
        print("invalid type for division")







