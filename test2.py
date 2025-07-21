import streamlit as st

# ページ設定
st.set_page_config(
    page_title="AI Training Hub", 
    page_icon="🤖", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# カスタムCSS
st.markdown("""
<style>
    /* メインコンテナのスタイル */
    .main-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* タイトルスタイル */
    .title {
        color: #ffffff;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.7);
        filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.8));
    }
    
    .subtitle {
        color: #ffffff;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-style: italic;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
        font-weight: 500;
    }
    
    /* カードスタイル */
    .resource-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 1rem;
        text-align: center;
        transition: transform 0.3s ease;
        backdrop-filter: blur(10px);
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .resource-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    /* アイコンスタイル */
    .icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: block;
    }
    
    .card-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .card-description {
        color: #666;
        margin-bottom: 1.5rem;
        font-size: 0.95rem;
        line-height: 1.5;
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* リンクボタンスタイル */
    .custom-button {
        display: inline-block;
        background: linear-gradient(45deg, #ff6b6b, #ee5a52);
        color: white;
        padding: 12px 25px;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .custom-button:hover {
        background: linear-gradient(45deg, #ee5a52, #ff6b6b);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        color: white;
        text-decoration: none;
    }
    
    /* 音声セクションのスタイル */
    .audio-section {
        background: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin-top: 0.5rem;
    }
    
    .audio-title {
        color: #333;
        font-size: 1rem;
        font-weight: bold;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }
    
    .audio-container {
        min-height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# URLs
external_url = "https://lagavulin1968.github.io/ai_training/bpo_ai_map.html"
voice_url = "https://lagavulin1968.github.io/ai_training/bpo_ai_voice.wav"

# メインコンテナ
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# タイトルセクション
st.markdown('''
<div class="title">🤖 AI Training Hub</div>
<div class="subtitle">BPO業界におけるAI活用の最前線</div>
''', unsafe_allow_html=True)

# リソースセクション
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('''
    <div class="resource-card">
        <div>
            <span class="icon">📊</span>
            <div class="card-title">AI活用マップ</div>
        </div>
        <div class="card-description">
            BPO会社におけるAI技術の活用方法を<br>
            視覚的にマッピングした資料です
        </div>
        <div style="margin-top: auto;">
    ''', unsafe_allow_html=True)
    
    # カスタムボタンリンク
    st.markdown(f'''
            <a href="{external_url}" target="_blank" class="custom-button">
                🔗 資料を開く
            </a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown('''
    <div class="resource-card">
        <div>
            <span class="icon">🎵</span>
            <div class="card-title">音声解説</div>
        </div>
        <div class="card-description">
            AI活用マップの詳細な解説を<br>
            音声でお聞きいただけます
        </div>
        <div class="audio-section">
            <div class="audio-title">
                🎧 解説音声を再生
            </div>
            <div class="audio-container">
    ''', unsafe_allow_html=True)
    
    # 音声プレーヤー
    st.audio(voice_url, format="audio/wav")
    
    st.markdown('''
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# フッター
st.markdown("""
---
<div style="text-align: center; color: #888; padding: 1rem;">
    <small>🚀 Powered by Streamlit | AI Training Hub © 2025</small>
</div>
""", unsafe_allow_html=True)