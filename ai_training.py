import streamlit as st
import streamlit.components.v1 as components
import os
import pandas as pd

st.set_page_config(page_title="AI_Training", page_icon="📊")

# HTMLファイルのパス（同じディレクトリ内）
html_file = os.path.join(os.path.dirname(__file__), "BPO_AI活用図.html")

# HTML読み込み
with open(html_file, "r", encoding="utf-8") as f:
    html_content = f.read()

# 表示（zoomなど調整も可能）
components.html(html_content, height=1000, scrolling=True)

# 別タブで開きたい場合（GitHub上でhostしてない限りこれは埋め込みだけ）
st.markdown(
    f'<a href="BPO_AI活用図.html" target="_blank">別タブで開く</a>',
    unsafe_allow_html=True
)
