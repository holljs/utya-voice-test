import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)

style = tts.get_voice_style(voice_name="F4")

phrases = {
    # Фразы для игры "Цвета"
    "color_intro.wav": "Помоги у́тачкам найти свои ло́дочки!",
    "color_win.wav": "Ура́! Все у́тачки в ло́дочках!",
    "color_correct.wav": "Прáвильно!",
    
    # Названия 8 цветов
    "color_yellow.wav": "Жёлтый.",
    "color_orange.wav": "Орáнжевый.",
    "color_red.wav": "Крáсный.",
    "color_pink.wav": "Рóзовый.",
    "color_purple.wav": "Фиолéтовый.",
    "color_blue.wav": "Сýний.",
    "color_green.wav": "Зелёный.",
    "color_grey.wav": "Сéрый."
}

print(f"Начинаем озвучку {len(phrases)} фраз для игры Цвета...")

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

print("✅ Готово! Все звуки для игры Цвета успешно сохранены.")
