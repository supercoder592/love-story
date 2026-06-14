import random
import streamlit as st
import base64


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


try:
    bin_str = get_base64_of_bin_file("bg.jpg")
    st.html(f"""
        <style>
        /* 1. 設定背景圖 */
        .stApp {{
            background-image: url("data:image/jpeg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* 2. 讓網頁標題和內文變黑 */
        .stApp h1, .stApp h2, .stApp h3, .stApp p {{
            color: #000000 !important;
        }}

        /* 3. 【核心修正】強制按鈕內的文字變成白色（不被上面染黑），按鈕維持原本的深色 */
        .stButton > button, .stButton > button p, .stButton > button span {{
            color: #FFFFFF !important;
        }}
        </style>
    """)
except FileNotFoundError:
    st.html("""
        <style>
        .stApp h1, .stApp h2, .stApp h3, .stApp p {
            color: #000000 !important;
        }
        .stButton > button, .stButton > button p, .stButton > button span {
            color: #FFFFFF !important;
        }
        </style>
    """)
if "page" not in st.session_state:
   st.session_state.page = 1
if st.session_state.page==1:

   col1, col2 = st.columns(2)
   with col1:
       st.title("國二八愛情檔案")
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" )
       st.image("0538.jpg")
       if st.button("0538"):
           st.session_state.page = 2
           st.rerun()
   with col2:
       st.image("1131.jpg")
       if st.button("1131"):
           st.session_state.page = 3
           st.rerun()
       st.image("1021.jpg")
       if st.button("1021"):
            st.session_state.page = 4
            st.rerun()


elif st.session_state.page==4:
   images = ["1021-1.jpg", "1021-2.jpg", "1021-3.jpg"]
   col3, col4 = st.columns(2)
   with col3:
       picture3=st.empty()
       picture3.image(random.choice(images))
   with col4:
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.title("男方:李柏承")
       st.write("\n"*8)
       st.title("女方:游涵方")
   st.write("\n")
   st.title("事蹟:")
   st.title("  怕妳跌倒")
   st.write("\n")
   st.title("  看影片不往前而是去後面")
   st.write("\n")
   st.title("  喜歡 日向")
   st.write("\n")
   st.title("  玩游涵方髮圈")
   if st.button("主畫面",key=1):
      st.session_state.page=1
      st.rerun()
elif st.session_state.page==3:
   images3 = ["1131-1.jpg","1131-3.jpg"]
   col3, col4 = st.columns(2)
   with col3:
       picture2=st.empty()
       picture2.image(random.choice(images3))




   with col4:
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.title("男方:陳子沅")
       st.write("\n"*8)
       st.title("女方:童品瑄")
   st.write("\n")
   st.title("事蹟:")
   st.title("  一起打電動")
   st.write("\n")
   st.title("  捏肚子")
   if st.button("主畫面",key=2):
      st.session_state.page=1
      st.rerun()
elif st.session_state.page==2:
   images2 = ["0538-1.jpg","0538-2.jpg","0538-3.jpg"]
   col3, col4 = st.columns(2)
   with col3:
       picture=st.empty()
       picture.image(random.choice(images2))




   with col4:
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.write("\n" * 8)
       st.title("男方:蔡侑辰")
       st.write("\n"*8)
       st.title("女方:李為樂")
   st.write("\n")
   st.title("事蹟:")
   st.title("  上課互塗白膠")
   st.write("\n")
   st.title("  互比愛心")
   st.write("\n")
   st.title("  用木棒互戳")
   st.write("\n")
   st.title("  喜歡黑尾 研磨")
   if st.button("主畫面",key=3):
      st.session_state.page=1
      st.rerun()
