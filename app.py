import streamlit as st


def main():
    st.set_page_config(
        page_title="My Streamlit App", page_icon=":guardsman:", layout="wide"
    )

    pg = st.navigation([st.Page("pages/page_1.py"), st.Page("pages/page_2.py")])

    pg.run()


if __name__ == "__main__":
    main()
