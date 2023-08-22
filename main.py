import streamlit as st

import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("The best company")
st.write("""
Lorem ipsum dolor sit amet consectetur, adipisicing elit. Voluptates
eligendi fuga est eos nemo ea error, quasi ad magnam doloribus tempora suscipit
alias unde debitis iusto, et, ex dicta dolorem magni nisi exercitationem. Vero iusto adipisci
nobis labore nam quibusdam totam deleniti doloribus distinctio ad quia doloremque sapiente,
quos debitis?
""")
st.subheader("Our team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Make a dataframe with the company members
df = pandas.read_csv("data.csv") # sep argument by default devivded by comma, change if not comma

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])


# Add content to the third column
with col3:
    # Iterate over rows 8:
    for index, row in df[8:].iterrows():
        # Add member's first and last names
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])