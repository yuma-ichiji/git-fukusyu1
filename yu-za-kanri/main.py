import streamlit as st
st.title("ユーザー情報入力")
if "name" not in st.session_state:
    st.session_state.name = ""
if "gakunen" not in st.session_state:
    st.session_state.gakunen = ""
if "syumi" not in st.session_state:
    st.session_state.syumi = []
name = st.text_input("あなたの名前を入力してください")
gakunen = st.selectbox("あなたの学年を選択してください", ["小学5年生", "小学6年生", "中学1年生", "中学2年生", "中学3年生"])
syumi = st.multiselect("あなたの趣味を選択してください", ["読書", "スポーツ", "ゲーム","音楽","絵画","その他"])
if st.button("情報を保存"):
    st.session_state.name=name
    st.session_state.gakunen=gakunen
    st.session_state.syumi=syumi
    st.success("情報を保存しました")