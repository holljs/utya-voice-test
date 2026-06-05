import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # --- Меморика: Стихи-ассоциации ---
    "poem_48.wav": "Шесть на во́семь... эээто... со́рок во́семь! Мы бегемо́та... куушать про́сим!!!",
    "poem_56.wav": "Семь на во́семь... эээто... пятдеся́т шесть! У лося́... рога́-то еее́сть!!!",
    "poem_42.wav": "Шесть на сее́мь... эээто... со́рок два! На дворе́... растеоот трава́!!!"
}

print(f"Запуск озвучки {len(quiz_phrases)} фраз...")

for filename, text in quiz_phrases.items():
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

print("✅ Успех! Все файлы для 'Нейро-Гения' готовы к скачиванию!")
