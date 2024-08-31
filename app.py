import streamlit as st
import requests
import time
import urllib.parse
import wave
from datetime import datetime
import os


# VOICEVOX URLのオプション
voicevox_urls = ["http://127.0.0.1:50021/", "http://127.0.0.1:50121/"]

# 話者リストの定義
speakers_50021 = [
    ("VOICEVOX: 四国めたん(ノーマル)", 2),
    ("VOICEVOX: 四国めたん(あまあま)", 0),
    ("VOICEVOX: 四国めたん(ツンツン)", 6),
    ("VOICEVOX: 四国めたん(セクシー)", 4),
    ("VOICEVOX: 四国めたん(ささやき)", 36),
    ("VOICEVOX: 四国めたん(ヒソヒソ)", 37),
    ("VOICEVOX: ずんだもん(ノーマル)", 3),
    ("VOICEVOX: ずんだもん(あまあま)", 1),
    ("VOICEVOX: ずんだもん(ツンツン)", 7),
    ("VOICEVOX: ずんだもん(セクシー)", 5),
    ("VOICEVOX: ずんだもん(ささやき)", 22),
    ("VOICEVOX: ずんだもん(ヒソヒソ)", 38),
    ("VOICEVOX: ずんだもん(ヘロヘロ)", 75),
    ("VOICEVOX: ずんだもん(なみだめ)", 76),
    ("VOICEVOX: 春日部つむぎ(ノーマル)", 8),
    ("VOICEVOX: 雨晴はう(ノーマル)", 10),
    ("VOICEVOX: 波音リツ(ノーマル)", 9),
    ("VOICEVOX: 波音リツ(クイーン)", 65),
    ("VOICEVOX: 玄野武宏(ノーマル)", 11),
    ("VOICEVOX: 玄野武宏(喜び)", 39),
    ("VOICEVOX: 玄野武宏(ツンギレ)", 40),
    ("VOICEVOX: 玄野武宏(悲しみ)", 41),
    ("VOICEVOX: 白上虎太郎(ふつう)", 12),
    ("VOICEVOX: 白上虎太郎(わーい)", 32),
    ("VOICEVOX: 白上虎太郎(びくびく)", 33),
    ("VOICEVOX: 白上虎太郎(おこ)", 34),
    ("VOICEVOX: 白上虎太郎(びえーん)", 35),
    ("VOICEVOX: 青山龍星(ノーマル)", 13),
    ("VOICEVOX: 青山龍星(熱血)", 81),
    ("VOICEVOX: 青山龍星(不機嫌)", 82),
    ("VOICEVOX: 青山龍星(喜び)", 83),
    ("VOICEVOX: 青山龍星(しっとり)", 84),
    ("VOICEVOX: 青山龍星(かなしみ)", 85),
    ("VOICEVOX: 青山龍星(囁き)", 86),
    ("VOICEVOX: 冥鳴ひまり(ノーマル)", 14),
    ("VOICEVOX: 九州そら(ノーマル)", 16),
    ("VOICEVOX: 九州そら(あまあま)", 15),
    ("VOICEVOX: 九州そら(ツンツン)", 18),
    ("VOICEVOX: 九州そら(セクシー)", 17),
    ("VOICEVOX: 九州そら(ささやき)", 19),
    ("VOICEVOX: もち子さん(ノーマル)", 20),
    ("VOICEVOX: もち子さん(セクシー／あん子)", 66),
    ("VOICEVOX: もち子さん(泣き)", 77),
    ("VOICEVOX: もち子さん(怒り)", 78),
    ("VOICEVOX: もち子さん(喜び)", 79),
    ("VOICEVOX: もち子さん(のんびり)", 80),
    ("VOICEVOX: 剣崎雌雄(ノーマル)", 21),
    ("VOICEVOX: WhiteCUL(ノーマル)", 23),
    ("VOICEVOX: WhiteCUL(たのしい)", 24),
    ("VOICEVOX: WhiteCUL(かなしい)", 25),
    ("VOICEVOX: WhiteCUL(びえーん)", 26),
    ("VOICEVOX: 後鬼(人間ver.)", 27),
    ("VOICEVOX: 後鬼(ぬいぐるみver.)", 28),
    ("VOICEVOX: 後鬼(人間（怒り）ver.)", 87),
    ("VOICEVOX: 後鬼(鬼ver.)", 88),
    ("VOICEVOX: No.7(ノーマル)", 29),
    ("VOICEVOX: No.7(アナウンス)", 30),
    ("VOICEVOX: No.7(読み聞かせ)", 31),
    ("VOICEVOX: ちび式じい(ノーマル)", 42),
    ("VOICEVOX: 櫻歌ミコ(ノーマル)", 43),
    ("VOICEVOX: 櫻歌ミコ(第二形態)", 44),
    ("VOICEVOX: 櫻歌ミコ(ロリ)", 45),
    ("VOICEVOX: 小夜/SAYO(ノーマル)", 46),
    ("VOICEVOX: ナースロボ＿タイプＴ(ノーマル)", 47),
    ("VOICEVOX: ナースロボ＿タイプＴ(楽々)", 48),
    ("VOICEVOX: ナースロボ＿タイプＴ(恐怖)", 49),
    ("VOICEVOX: ナースロボ＿タイプＴ(内緒話)", 50),
    ("VOICEVOX: †聖騎士 紅桜†(ノーマル)", 51),
    ("VOICEVOX: 雀松朱司(ノーマル)", 52),
    ("VOICEVOX: 麒ヶ島宗麟(ノーマル)", 53),
    ("VOICEVOX: 春歌ナナ(ノーマル)", 54),
    ("VOICEVOX: 猫使アル(ノーマル)", 55),
    ("VOICEVOX: 猫使アル(おちつき)", 56),
    ("VOICEVOX: 猫使アル(うきうき)", 57),
    ("VOICEVOX: 猫使ビィ(ノーマル)", 58),
    ("VOICEVOX: 猫使ビィ(おちつき)", 59),
    ("VOICEVOX: 猫使ビィ(人見知り)", 60),
    ("VOICEVOX: 中国うさぎ(ノーマル)", 61),
    ("VOICEVOX: 中国うさぎ(おどろき)", 62),
    ("VOICEVOX: 中国うさぎ(こわがり)", 63),
    ("VOICEVOX: 中国うさぎ(へろへろ)", 64),
    ("VOICEVOX: 栗田まろん(ノーマル)", 67),
    ("VOICEVOX: あいえるたん(ノーマル)", 68),
    ("VOICEVOX: 満別花丸(ノーマル)", 69),
    ("VOICEVOX: 満別花丸(元気)", 70),
    ("VOICEVOX: 満別花丸(ささやき)", 71),
    ("VOICEVOX: 満別花丸(ぶりっ子)", 72),
    ("VOICEVOX: 満別花丸(ボーイ)", 73),
    ("VOICEVOX: 琴詠ニア(ノーマル)", 74),
]

speakers_50121 = [
    ("VOICEVOX Nemo: 女声1(ノーマル)", 10005),
    ("VOICEVOX Nemo: 女声2(ノーマル)", 10007),
    ("VOICEVOX Nemo: 女声3(ノーマル)", 10004),
    ("VOICEVOX Nemo: 女声4(ノーマル)", 10003),
    ("VOICEVOX Nemo: 女声5(ノーマル)", 10008),
    ("VOICEVOX Nemo: 女声6(ノーマル)", 10006),
    ("VOICEVOX Nemo: 男声1(ノーマル)", 10001),
    ("VOICEVOX Nemo: 男声2(ノーマル)", 10000),
    ("VOICEVOX Nemo: 男声3(ノーマル)", 10002),
]


def voicevox_engine(text, VOICEVOX_URL, SPEAKER_ID, wav_file_path):
    # サーバーの状態をチェック
    try:
        requests.get(VOICEVOX_URL, timeout=5)
    except requests.RequestException:
        raise ConnectionError("VOICEVOXサーバーが起動していないか、接続できません")

    # テキストをURLエンコード
    encoded_text = urllib.parse.quote(text)

    # audio_queryエンドポイントにリクエスト
    query_url = f"{VOICEVOX_URL}audio_query?text={encoded_text}&speaker={SPEAKER_ID}"
    query_response = requests.post(query_url)
    query_response.raise_for_status()

    # synthesisエンドポイントにリクエスト
    synthesis_url = f"{VOICEVOX_URL}synthesis?speaker={SPEAKER_ID}"
    synthesis_response = requests.post(synthesis_url, json=query_response.json())
    synthesis_response.raise_for_status()

    # WAVファイルに保存
    with wave.open(wav_file_path, "wb") as wav_file:
        wav_file.setnchannels(1)  # モノラル
        wav_file.setsampwidth(2)  # 16ビット
        wav_file.setframerate(24000)  # サンプリングレート
        wav_file.writeframes(synthesis_response.content)

    print(f"音声ファイルが {wav_file_path} に保存されました。")


# Streamlitアプリケーションの設定
st.title("VOICEVOX音声生成")

# リンクの追加
st.markdown(
    """
<ul>
<li>
    <a href="https://voicevox.hiroshiba.jp/" target="_blank" rel="noopener noreferrer">VOICEVOX公式サイト</a> 
</li>
<li>
    <a href="https://voicevox.hiroshiba.jp/nemo/" target="_blank" rel="noopener noreferrer">VOICEVOX Nemo</a>
</li>
</ul>

""",
    unsafe_allow_html=True,
)

# VOICEVOX URLの選択（フォームの外）
voicevox_url = st.selectbox("VOICEVOX URL", voicevox_urls)

# 選択されたURLに基づいて話者リストを選択
if voicevox_url.endswith("50021/"):
    speakers = speakers_50021
else:
    speakers = speakers_50121

# フォームの作成
with st.form("voicevox_form"):
    # 話者の選択
    speaker_name, speaker_id = st.selectbox(
        "話者を選択してください", options=speakers, format_func=lambda x: x[0]
    )

    # テキスト入力
    text = st.text_input("生成するテキスト")

    # 送信ボタン
    submit_button = st.form_submit_button("音声生成")

# 送信ボタンが押されたときの処理
if submit_button:
    if text:
        # 進捗バーの表示
        progress_bar = st.progress(0)
        status_text = st.empty()

        # ファイル名の生成
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        wav_file_path = f"./voicefile/{timestamp}.wav"

        # ディレクトリの作成（存在しない場合）
        os.makedirs("./voicefile", exist_ok=True)

        try:
            status_text.text("音声生成中...")
            progress_bar.progress(25)

            # voicevox_engine関数の呼び出し
            voicevox_engine(text, voicevox_url, speaker_id, wav_file_path)

            progress_bar.progress(75)
            status_text.text("音声ファイル保存中...")

            time.sleep(2)  # ファイル保存の待機時間（調整可能）

            progress_bar.progress(100)
            status_text.text("音声生成完了！")

            # 音声ファイルの再生（オプション）
            audio_file = open(wav_file_path, "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav")

        except Exception as e:
            st.error(f"エラーが発生しました: {str(e)}")
    else:
        st.warning("テキストを入力してください。")
