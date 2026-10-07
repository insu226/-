import streamlit as st
import random

st.title("🔮 오늘의 운세")

st.write("나의 띠를 선택하고 오늘의 운세를 확인해 보세요!")

zodiac = st.selectbox(
    "띠를 선택하세요",
    [
        "쥐띠",
        "소띠",
        "호랑이띠",
        "토끼띠",
        "용띠",
        "뱀띠",
        "말띠",
        "양띠",
        "원숭이띠",
        "닭띠",
        "개띠",
        "돼지띠"
    ]
)

fortunes = [
    "오늘은 새로운 기회가 찾아올 수 있는 날입니다. 적극적으로 도전해 보세요!",
    "작은 일에서 뜻밖의 행운을 발견할 수 있습니다.",
    "주변 사람들과의 대화에서 좋은 아이디어를 얻을 수 있습니다.",
    "서두르지 않고 차분하게 행동하면 좋은 결과가 따릅니다.",
    "오늘은 자신감을 가지고 행동할수록 좋은 일이 생길 수 있습니다.",
    "예상하지 못한 좋은 소식이 찾아올 수 있습니다.",
    "휴식이 필요한 날입니다. 잠시 여유를 가지는 것도 좋습니다.",
    "집중력이 좋은 날입니다. 미뤄 두었던 일을 해보세요!",
    "친구나 동료의 도움으로 일이 쉽게 풀릴 수 있습니다.",
    "새로운 사람과의 만남이 좋은 인연으로 이어질 수 있습니다."
]

if st.button("오늘의 운세 보기"):
    fortune = random.choice(fortunes)

    st.subheader(f"✨ {zodiac}의 오늘의 운세")
    st.success(fortune)

    lucky_number = random.randint(1, 9)

    colors = [
        "빨강",
        "파랑",
        "초록",
        "노랑",
        "보라",
        "주황",
        "하늘색"
    ]

    lucky_color = random.choice(colors)

    st.write(f"🍀 행운의 숫자: **{lucky_number}**")
    st.write(f"🎨 행운의 색깔: **{lucky_color}**")