import streamlit as st
st.set_page_config(page_title= "Growth Mind Set")
st.title("Growth Mind Set:")
st.write("""
         Convert Your Fixed Mind Set to Growth mind Set Set Learning Goals: Instead of only focusing on grades, set goals that help you develop new skills and understand complex concepts.
Reflect on Your Learning: Regularly take time to think about what you learned from both your successes and your challenges.
Seek Feedback: Embrace constructive criticism and use it as a tool for improvement.
Stay Positive: Believe in your capacity to grow, and encourage your peers to do the same.

         """)

st.header("Set Learning Goal's:")
user_goal_input = st.text_input("Enter Your Learning Goal's")
if user_goal_input:
    st.success(f"Your Learning Idea's {user_goal_input} i very good allway's Be possitive And Keep' Up")


st.header("Chalenges You Face:")
user_chalenges_input = st.text_input("Enter Your Chalenges You Facing")
if user_chalenges_input:
    st.success(f"every chalenge of your project and your life is fix on his time {user_chalenges_input} this is fixed but never give stay strong research and contact your seniors and fixed any problem with ai")


st.header("Celebrate Your Work:")
user_work_input = st.text_input("Your Celebrate Prapretion's")
if user_work_input:
    st.success(f"Celebrate Your Win And Happy  Your Celebrating {user_work_input} technieque are good ")
st.write("Good Bye Saim-Hk")

