import streamlit as st

def find_largest_number(a, b, c):
    return max(a, b, c)

def main():
    st.title("Largest Number Finder")

    st.write("Enter three numbers to find the largest among them:")

    num1 = st.number_input("Number 1", value=0)
    num2 = st.number_input("Number 2", value=0)
    num3 = st.number_input("Number 3", value=0)

    if st.button("Find Largest"):
        largest = find_largest_number(num1, num2, num3)
        st.write(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")

if __name__ == "__main__":
    main()
