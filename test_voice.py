import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Словарь: имя файла -> текст с ударениями (для 'у' под ударением — удвоение)
phrases = {
    # ---------- Названия фигур (обучающие карточки) ----------
    "shape_circle.wav": "Крууг",              # ударение на 'у' -> удваиваем
    "shape_square.wav": "Квадра́т",
    "shape_triangle.wav": "Треуго́льник",
    "shape_rect.wav": "Прямоуго́льник",
    "shape_star.wav": "Звезда́",
    "shape_rhombus.wav": "Ро́мб",

    # ---------- Игровые реакции ----------
    "shapes_intro.wav": "Дава́й подберём пра́вильную запла́тку!",
    "shape_correct.wav": "Пра́вильно!",
    "shapes_win.wav": "Ура́! Ты спра́вился!",
    "wrong.wav": "О́й!",
}

print(f"Запуск озвучки {len(phrases)} фраз...")

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

print("✅ Готово! Все звуковые файлы для фигур успешно сгенерированы.")
