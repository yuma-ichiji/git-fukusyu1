import streamlit as st
st.title("ユーザー情報")
if ("name" in st.session_state and st.session_state.name):
    st.success("✅ 保存されている情報:")
    col1, col2 = st.columns(2)    
    with col1:
        st.metric("名前", st.session_state.name)
        st.metric("学年", st.session_state.get("gakunen", "未設定"))
    with col2:
        if st.session_state.get("syumi"):
            st.write("趣味:")
            for hobby in st.session_state.hobbies:
                st.write(f"• {hobby}")
        else:
            st.write("趣味: 未設定")   
    st.balloons()
else:
    st.error("ユーザー情報が設定されていません")
    st.write("メインページで情報を入力してください")