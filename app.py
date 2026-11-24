import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="접두사 영어 단어 결합기", page_icon="🔤", layout="centered")

# 입체감 있는 3D 버튼 스타일 CSS
st.markdown(
    """
    <style>
    /* 기본(미선택) 3D 버튼 스타일 */
    div.stButton > button[kind="secondary"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%);
        color: #1E293B;
        border: 2px solid #CBD5E1;
        border-bottom: 6px solid #94A3B8;
        border-radius: 14px;
        font-size: 19px;
        font-weight: 700;
        padding: 14px 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.08);
        transition: all 0.12s ease;
    }
    div.stButton > button[kind="secondary"]:hover {
        background: linear-gradient(180deg, #F8FAFC 0%, #E2E8F0 100%);
        border-color: #60A5FA;
        border-bottom-color: #3B82F6;
        color: #0066FF;
        transform: translateY(-1px);
    }
    div.stButton > button[kind="secondary"]:active {
        transform: translateY(4px);
        border-bottom-width: 2px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    }

    /* 선택된 버튼 & 결합하기 3D 버튼 스타일 */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(180deg, #3B82F6 0%, #0066FF 100%);
        color: #FFFFFF;
        border: 2px solid #0052CC;
        border-bottom: 6px solid #003D99;
        border-radius: 14px;
        font-size: 20px;
        font-weight: 800;
        padding: 14px 10px;
        box-shadow: 0 5px 10px rgba(0, 102, 255, 0.28);
        transition: all 0.12s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(180deg, #60A5FA 0%, #1D4ED8 100%);
        transform: translateY(-1px);
    }
    div.stButton > button[kind="primary"]:active {
        transform: translateY(4px);
        border-bottom-width: 2px;
        box-shadow: 0 2px 4px rgba(0, 102, 255, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 접두사 및 어근 데이터
WORD_DATA = {
    "pre": {
        "meaning": "미리",
        "roots": {
            "dict": ("말하다", "예측하다"),
            "view": ("보다", "미리 보기(시사회)"),
            "prepare": ("준비하다", "미리 준비하다"),
            "vent": ("오다/막다", "예방하다"),
            "pay": ("지불하다", "선불하다"),
            "mature": ("성숙한", "조숙한(시기상조의)"),
        },
    },
    "sub": {
        "meaning": "아래에",
        "roots": {
            "way": ("길", "지하철(지하도)"),
            "marine": ("바다의", "잠수함"),
            "merge": ("가라앉다", "잠수하다"),
            "title": ("제목", "부제목(자막)"),
            "topic": ("주제", "하위 주제"),
            "urban": ("도시의", "교외의"),
        },
    },
    "inter": {
        "meaning": "사이에/서로",
        "roots": {
            "act": ("행동하다", "상호작용하다"),
            "play": ("작용하다", "상호작용"),
            "national": ("국가의", "국제적인"),
            "rupt": ("깨뜨리다", "방해하다(중단시키다)"),
            "cept": ("잡다", "가로채다"),
            "val": ("간격", "간격(중간 휴식)"),
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
if "is_combined" not in st.session_state:
    st.session_state.is_combined = False


# 버튼 클릭 콜백 함수들
def select_prefix(prefix_name: str):
    st.session_state.prefix = prefix_name
    st.session_state.root = list(WORD_DATA[prefix_name]["roots"].keys())[0]
    st.session_state.is_combined = False


def select_root(root_name: str):
    st.session_state.root = root_name
    st.session_state.is_combined = False


def combine_word():
    st.session_state.is_combined = True


def pick_random_word():
    rand_prefix = random.choice(list(WORD_DATA.keys()))
    rand_root = random.choice(list(WORD_DATA[rand_prefix]["roots"].keys()))
    st.session_state.prefix = rand_prefix
    st.session_state.root = rand_root
    st.session_state.is_combined = True


st.title("🔤 접두사로 배우는 영어 단어 결합기")
st.write("입체 버튼을 눌러 접두사와 단어를 고른 뒤 **결합하기** 버튼을 눌러보세요!")

# 랜덤 추천 버튼
st.button("🎲 랜덤 단어 조합 뽑기", on_click=pick_random_word, type="secondary")

st.divider()

# 1단계: 접두사 선택 (3D 버튼 3개 가로 배치)
st.subheader("1단계: 접두사를 선택하세요")
prefix_cols = st.columns(3)
for idx, prefix_key in enumerate(WORD_DATA.keys()):
    is_selected = st.session_state.prefix == prefix_key
    with prefix_cols[idx]:
        st.button(
            prefix_key,
            key=f"btn_prefix_{prefix_key}",
            type="primary" if is_selected else "secondary",
            use_container_width=True,
            on_click=select_prefix,
            args=(prefix_key,),
        )

st.write("")

# 2단계: 선택한 접두사에 따른 하위 단어 선택 (3D 버튼 3열 그리드 배치)
selected_prefix = st.session_state.prefix
st.subheader(f"2단계: '{selected_prefix}' 뒤에 붙일 단어를 선택하세요")
root_options = list(WORD_DATA[selected_prefix]["roots"].keys())

for row_start in range(0, len(root_options), 3):
    row_cols = st.columns(3)
    for col_idx, root_key in enumerate(root_options[row_start : row_start + 3]):
        is_selected = st.session_state.root == root_key
        with row_cols[col_idx]:
            st.button(
                root_key,
                key=f"btn_root_{selected_prefix}_{root_key}",
                type="primary" if is_selected else "secondary",
                use_container_width=True,
                on_click=select_root,
                args=(root_key,),
            )

st.divider()

# 3단계: 결합하기 버튼
selected_root = st.session_state.root
st.button(
    f"🔗 결합하기 ({selected_prefix} + {selected_root})",
    key="btn_combine",
    type="primary",
    use_container_width=True,
    on_click=combine_word,
)

# 결과 출력 영역
if st.session_state.is_combined:
    prefix_meaning = WORD_DATA[selected_prefix]["meaning"]
    root_meaning, full_meaning = WORD_DATA[selected_prefix]["roots"][selected_root]

    # 접두사 영어와 한국어 뜻은 파란색(#0066FF) + 더 큰 글씨(52px)로 강조
    result_html = f"""
    <div style="
        background-color: #F8FAFC;
        border: 3px solid #CBD5E1;
        border-radius: 16px;
        padding: 36px 20px;
        text-align: center;
        margin-top: 16px;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06);
    ">
        <div style="line-height: 1.6; word-break: keep-all;">
            <span style="color: #0066FF; font-size: 52px; font-weight: 900;">{selected_prefix}</span><span style="color: #111111; font-size: 32px; font-weight: 700;">{selected_root}</span>
            <span style="color: #111111; font-size: 32px; font-weight: 700;"> = </span>
            <span style="color: #0066FF; font-size: 52px; font-weight: 900;">{prefix_meaning}</span><span style="color: #111111; font-size: 32px; font-weight: 700;">{root_meaning}</span>
            <span style="color: #111111; font-size: 32px; font-weight: 700;"> = </span>
            <span style="color: #111111; font-size: 34px; font-weight: 800;">{full_meaning}</span>
        </div>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
    st.caption(f"💡 {random.choice(CHEER_MESSAGES)}")
else:
    st.info("위에서 접두사와 단어를 선택한 후 파란색 **'결합하기'** 버튼을 눌러 결과를 확인하세요!")
