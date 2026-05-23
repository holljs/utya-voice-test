import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

style = tts.get_voice_style(voice_name="F4")

phrases = {
    "na1.wav": "Кошка.",
    "na2.wav": "Собака.",
    "na3.wav": "Корова.",
    "na4.wav": "Лошадь.",
    "na5.wav": "Овца.",
    "na6.wav": "Свинья.",
    "na7.wav": "Коза.",
    "na8.wav": "Волк.",
    "na9.wav": "Гусь.",
    "na10.wav": "Лягушка.",
    "na11.wav": "Лев.",
    "na12.wav": "Тигр.",
    "na13.wav": "Змея.",
    "na14.wav": "Комар.",
    "na15.wav": "Пчела.",
    "na16.wav": "Лиса.",
    "na17.wav": "Ёжик.",
    "na18.wav": "Курица.",
    "na19.wav": "Петушок.",
    "na20.wav": "Ворона.",
    "na21.wav": "Ослик.",
    "na22.wav": "Сова.",
    "na23.wav": "Слон.",
    "na24.wav": "Мышка."
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

print("✅ Готово! Названия животных успешно сохранены.")
