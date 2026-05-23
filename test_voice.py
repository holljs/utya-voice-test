import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

style = tts.get_voice_style(voice_name="F4")

phrases = {
    "na1.wav": "Кóшка.",
    "na2.wav": "Собáка.",
    "na3.wav": "Корóва.",
    "na4.wav": "Лóшадь.",
    "na5.wav": "Овцá.",
    "na6.wav": "Свинья.",
    "na7.wav": "Козá.",
    "na8.wav": "Волк.",
    "na9.wav": "Гусь.",
    "na10.wav": "Лягушка.",
    "na11.wav": "Лев.",
    "na12.wav": "Тигр.",
    "na13.wav": "Змея.",
    "na14.wav": "Комáр.",
    "na15.wav": "Пчелá.",
    "na16.wav": "Лисá.",
    "na17.wav": "Ёжик.",
    "na18.wav": "Курица.",
    "na19.wav": "Петушóк.",
    "na20.wav": "Ворóна.",
    "na21.wav": "О́слик.",
    "na22.wav": "Совá.",
    "na23.wav": "Слон.",
    "na24.wav": "Мы́шка."
}

print(f"Начинаем озвучку {len(phrases)} названий...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    wav, duration = tts.synthesize(
        text=text,
        lang="ru",
        voice_style=style,
        total_steps=10,
        speed=0.7 
    )
    sf.write(filename, wav.squeeze(), 54000)

print("✅ Готово! Названия животных с правильными ударениями успешно сохранены.")
