import streamlit as st

from module9.polymorphisu.function import result_2


def calculator(num1,num2,operation):
    if operation=="add":
        result=num1+num2
    if operation=="sub":
        result=num1+num2
    if operation=="multi":
        result=num1+num2
    if operation=="div":

      try:
          result=num1/num2
      except zerodivsionError:
          result="cannot divide by zero"
      return result

    def main():
        st.title("simple calculator")

        num1=st.number_input("enter the first number",step=1)

        num2=st.number_input("enter the second nubmer",step=1)

        operation=st.radio("select operation",["add","sub","multi",div])

        result=calculator(num1,num2,operation)

        st.write(f"result of the {operation} of {num1} and {num2} is {result}")

if __name__=="__main__":
    main()

























