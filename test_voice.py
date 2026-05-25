import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Словарь цветов и фраз для раскраски
phrases = {
    # Цвета (названия при выборе)
    "color_red.wav": "Крáсный!",
    "color_blue.wav": "Си́ний!",
    "color_yellow.wav": "Жёлтый!",
    "color_green.wav": "Зелёный!",
    "color_orange.wav": "Орáнжевый!",
    "color_purple.wav": "Фиолéтовый!",
    "color_pink.wav": "Рóзовый!",
    "color_brown.wav": "Корúчневый!",
    
    # Служебные звуки
    "paint_clear.wav": "Чи́сто! Рисуууем занóво!",
    "paint_good.wav": "Отли́чно получи́лось!",
    "paint_beautiful.wav": "Как крáсиво!"
}

print(f"Запуск озвучки {len(phrases)} фраз для раскрасок...")

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

print("✅ Готово! Все звуковые файлы для раскрасок успешно сгенерированы.")
