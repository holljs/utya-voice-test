import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

garden_phrases = {
    "g_level1.wav": "Памоги́ за́йке пасади́ть однуу марко́вку!",
    "g_level2.wav": "Памоги́ ми́шке сабра́ть два́ арбууза!",
    "g_level3.wav": "Памоги́ ко́зочке найти́ три́ капуусты!",
    "g_level4.wav": "Памоги́ ёжику сабра́ть четы́ре грибо́чка!",
    "g_level5.wav": "Памоги́ бе́лочке спря́тать пя́ть оре́шков!",
    "g_level6.wav": "Памоги́ сви́нке сабра́ть ше́сть ты́кв!",
    "g_level7.wav": "Памоги́ мы́шке пасади́ть се́мь реди́сок!",
    "g_level8.wav": "Памоги́ ено́ту сабра́ть во́семь кукурууз!",
    "g_level9.wav": "Памоги́ Ууте сабра́ть де́вять я́годок клубни́ки!"
}

print(f"Запуск озвучки {len(garden_phrases)} фраз...")

for filename, text in garden_phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7 
        )
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все файлы для 'Нейро-Малыша' готовы к скачиванию!")
