import streamlit as st
import requests
from datetime import datetime
import pytz
import re
#FPT-Conf-2026Jun3rd

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzlvMgr_78oWXJA63hmPe17fnZz0uF8E54txuSd3FKkbLX_rcRWPOseJVGKcpF-L0Ui/exec"
st.set_page_config(
    page_title="Check-in Hội thảo FPT",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}

.block-container {
    max-width: 480px;
    padding-top: 18px;
    padding-left: 18px;
    padding-right: 18px;
    padding-bottom: 30px;
}

.checkin-card {
    background: #ffffff;
    border-radius: 18px;
    padding: 22px 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    border: 1px solid #eeeeee;
}

.main-title {
    text-align: center;
    color: #1b7f3a;
    font-size: 28px;
    font-weight: 800;
    line-height: 1.35;
    margin-top: 18px;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #555555;
    font-size: 16px;
    margin-bottom: 22px;
}

label {
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #222222 !important;
}

.stTextInput input {
    height: 50px;
    font-size: 17px;
    border-radius: 12px;
}

.stSelectbox div[data-baseweb="select"] > div {
    min-height: 50px;
    font-size: 17px;
    border-radius: 12px;
}

.stButton button {
    width: 100%;
    height: 54px;
    font-size: 19px;
    font-weight: 800;
    border-radius: 14px;
    background-color: #1b7f3a;
    color: white;
    border: none;
    margin-top: 8px;
}

.stButton button:hover {
    background-color: #14682f;
    color: white;
}

@media screen and (max-width: 600px) {
    .block-container {
        max-width: 100%;
        padding-left: 14px;
        padding-right: 14px;
        padding-top: 12px;
    }

    .main-title {
        font-size: 24px;
    }

    .sub-title {
        font-size: 15px;
    }

    .checkin-card {
        padding: 18px 14px;
        border-radius: 16px;
    }
}
</style>
""", unsafe_allow_html=True)

# st.markdown("""
# <div class="checkin-card">
#     <div class="main-title">CHECK-IN<br>HỘI THẢO FPT 10/06/2026</div>
#     <div class="sub-title">Sinh viên vui lòng nhập thông tin để điểm danh</div>
# </div>
# """, unsafe_allow_html=True)

st.markdown("""
<div class="checkin-card">
<div class="main-title">CHECK-IN<br>HỘI THẢO FPT 10/06/2026</div>
<div class="sub-title">Sinh viên vui lòng nhập thông tin để điểm danh</div>
<div style="text-align:center;color:#d60000;font-size:15px;font-weight:600;margin-top:-10px;margin-bottom:5px;">
📢 Thông tin CHECK-IN sẽ được chia sẻ với Doanh nghiệp Tuyển dụng
</div>
</div>
""", unsafe_allow_html=True)

def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def valid_phone(phone):
    return phone.isdigit() and 9 <= len(phone) <= 11

with st.form("checkin_form", clear_on_submit=False):
    full_name = st.text_input("Họ tên", placeholder="Ví dụ: Nguyễn Văn A")

    student_id = st.text_input(
        "Mã số sinh viên",
        placeholder="Ví dụ: N23DCCN001 hoặc 2211565"
    )

    email = st.text_input("Email", placeholder="Ví dụ: nguyenvana@gmail.com")
    phone = st.text_input("Số điện thoại", placeholder="Ví dụ: 0901234567")
    year = st.selectbox(
        "SV đang học năm mấy?",
        ["Chọn năm học", "Năm 1", "Năm 2", "Năm 3", "Năm 4", "Năm 5", "Khác"]
    )

    submitted = st.form_submit_button("✅ Check-in")

if submitted:
    full_name = full_name.strip()
    student_id = student_id.strip()
    email = email.strip()
    phone = phone.strip().replace(" ", "")

    if WEB_APP_URL == "DAN_LINK_APPS_SCRIPT_CUA_ANH_VAO_DAY":
        st.error("Anh chưa dán link Apps Script vào biến WEB_APP_URL.")
    elif not full_name or not student_id or not email or not phone or year == "Chọn năm học":
        st.error("Vui lòng nhập đầy đủ thông tin.")
    elif not valid_email(email):
        st.error("Email chưa hợp lệ.")
    elif not valid_phone(phone):
        st.error("Số điện thoại chưa hợp lệ. Vui lòng nhập 9–11 chữ số.")
    else:
        vn_time = datetime.now(pytz.timezone("Asia/Ho_Chi_Minh"))
        checkin_time = vn_time.strftime("%d/%m/%Y %H:%M:%S")

        payload = {
            "time": checkin_time,
            "full_name": full_name,
            "student_id": student_id,
            "email": email,
            "phone": phone,
            "year": year
        }

        # try:
           
        #     response = requests.post(WEB_APP_URL, json=payload, timeout=15)
    
        #     st.write("Mã phản hồi:", response.status_code)
        #     st.write("Nội dung trả về:", response.text)

        #     result = response.json()

        #     if result.get("status") == "success":
        #         st.success("✅ Check-in thành công. Cảm ơn bạn!")
        #     elif result.get("status") == "duplicate":
        #         st.warning("⚠️ Bạn đã check-in trước đó.")
        #     else:
        #         st.error("Có lỗi xảy ra. Vui lòng thử lại.")

        # except Exception as e:
        #     st.error("Không gửi được dữ liệu. Lỗi chi tiết:")
        #     st.code(str(e))
        try:
            response = requests.post(WEB_APP_URL, json=payload, timeout=20)
            result = response.json()

            if result.get("status") == "success":
                st.success("✅ Check-in thành công. Cảm ơn bạn!")
            elif result.get("status") == "duplicate":
                st.warning("⚠️ Bạn đã check-in trước đó.")
            else:
                st.error("Có lỗi xảy ra. Vui lòng thử lại.")

        except Exception:
                st.error("Không gửi được dữ liệu. Vui lòng thử lại.")