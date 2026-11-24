import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="접두사 영어 단어 결합기", page_icon="🔤", layout="centered")

# 접두사 및 어근 데이터 정의
WORD_DATA = {
    "pre": {
        "meaning": "미리",
        "roots": {
            "dict": ("말하다", "예측하다"),
            "view": ("보다", "미리 보기(시사회)"),
            "prepare": ("준비하다", "미리 준비하다"),
        },
    },
    "sub": {
        "meaning": "아래에",
        "roots": {
            "way": ("길", "지하철(지하도)"),
            "marine": ("바다의", "잠수함"),
            "merge": ("가라앉다", "잠수하다"),
        },
    },
    "infer": {
        "meaning": "사이에/서로",
        "roots": {
            "act": ("행동하다", "상호작용하다"),
            "play": ("작용하다", "상호작용"),
            "national": ("국가의", "국제적인"),
        },
    },
}

CHEER_MESSAGES = [
    "접두사의 뜻만 알아도 어휘력이 2배로 늘어납니다!",
    "원리를 이해하면 처음 보는 단어도 뜻을 추측할 수 있어요.",
    "다른 접두사와 어근 조합도 눌러보며 비교해 보세요!",
]

# 세션 상태 초기화
if "prefix" not in st.session_state:
    st.session_state.prefix = "pre"
if "root" not in st.session_state:
    st.session_state.root = "dict"


# random 라이브러리를 활용한 랜덤 단어 선택 함수
def pick_random_word():
    rand_prefix = random.choice(list(WORD_DATA.keys()))
    rand_root = random.choice(list(WORD_DATA[rand_prefix]["roots"].keys()))
    st.session_state.prefix = rand_prefix
    st.session_state.root = rand_root


st.title("🔤 접두사로 배우는 영어 단어 결합기")
st.write("접두사와 단어를 차례대로 선택해 단어의 형성 원리를 확인해 보세요.")

# 랜덤 추천 버튼
st.button("🎲 랜덤 단어 조합 뽑기", on_click=pick_random_word)

st.divider()

# 1단계: 접두사 선택
st.subheader("1단계: 접두사를 선택하세요")
selected_prefix = st.radio(
    "접두사 선택",
    options=list(WORD_DATA.keys()),
    horizontal=True,
    key="prefix",
    label_visibility="collapsed",
)

# 2단계: 선택한 접두사에 따른 하위 단어 선택
st.subheader(f"2단계: '{selected_prefix}' 뒤에 붙일 단어를 선택하세요")
root_options = list(WORD_DATA[selected_prefix]["roots"].keys())

# 접두사가 바뀌었을 때 기존 선택값이 목록에 없으면 첫 번째 단어로 초기화
if st.session_state.root not in root_options:
    st.session_state.root = root_options[0]

selected_root = st.radio(
    "어근 선택",
    options=root_options,
    horizontal=True,
    key="root",
    label_visibility="collapsed",
)

st.divider()

# 선택된 단어와 뜻 가져오기
prefix_meaning = WORD_DATA[selected_prefix]["meaning"]
root_meaning, full_meaning = WORD_DATA[selected_prefix]["roots"][selected_root]

# 결과 화면 출력 (접두사 및 접두사 뜻은 파란색, 나머지는 검은색으로 크게 표시)
result_html = f"""
<div style="
    background-color: #F8F9FA;
    border: 2px solid #E1E4E8;
    border-radius: 12px;
    padding: 32px 20px;
    text-align: center;
    margin-top: 10px;
">
    <div style="font-size: 38px; font-weight: 800; line-height: 1.5; word-break: keep-all;">
        <span style="color: #0066FF;">{selected_prefix}</span><span style="color: #111111;">{selected_root}</span>
        <span style="color: #111111;"> = </span>
        <span style="color: #0066FF;">{prefix_meaning}</span><span style="color: #111111;">{root_meaning}</span>
        <span style="color: #111111;"> = </span>
        <span style="color: #111111;">{full_meaning}</span>
    </div>
</div>
"""

st.markdown(result_html, unsafe_allow_html=True)
st.caption(f"💡 {random.choice(CHEER_MESSAGES)}")
