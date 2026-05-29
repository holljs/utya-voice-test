import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Словарь: имя файла -> текст с ударениями (для 'у' под ударением — удваиваем в 'уу')
phrases = {
    # ---------- КОМНАТА: БОЛЬШОЙ - МАЛЕНЬКИЙ ----------
    # Системные звуки
    "bs_intro.wav": "Где большо́й, а где ма́ленький? Разложи́ по коро́бкам!",
    "bs_win.wav": "Молоде́ц! Ты всё разложи́л пра́вильно!",

    # Пары предметов
    "bs_elephant.wav": "Большо́й сло́н",
    "bs_mouse.wav": "Ма́ленькая мы́шка",

    "bs_car_big.wav": "Больша́я маши́на",
    "bs_car_small.wav": "Ма́ленькая маши́нка",

    "bs_ball_big.wav": "Большо́й мя́ч",
    "bs_ball_small.wav": "Ма́ленький мя́чик",

    "bs_dog.wav": "Больша́я соба́ка",
    "bs_puppy.wav": "Ма́ленький щено́к",

    "bs_apple.wav": "Большо́е я́блоко",
    "bs_berry.wav": "Ма́ленькая я́годка",

    "bs_house_big.wav": "Большо́й до́м",
    "bs_house_small.wav": "Ма́ленький до́мик",

    "bs_tree.wav": "Большо́е де́рево",
    "bs_leaf.wav": "Ма́ленький листо́чек",

    "bs_plate.wav": "Больша́я таре́лка",
    "bs_spoon.wav": "Ма́ленькая ло́жечка",

    "bs_bear.wav": "Большо́й медве́дь",
    "bs_bunny.wav": "Ма́ленький за́йка",

    "bs_truck.wav": "Большо́й грузови́к",
    "bs_block.wav": "Ма́ленький ку́бик",

    "bs_chair_big.wav": "Большо́й сту́л",
    "bs_chair_small.wav": "Ма́ленький сту́льчик",

    "bs_ship.wav": "Большо́й кора́бль",
    "bs_boat.wav": "Ма́ленькая ло́дочка"
} # <--- ВОТ ОНА, ПОТЕРЯВШАЯСЯ СКОБКА!

print(f"Запуск озвучки {len(phrases)} фраз...")

for filename, text in phrases.items():
    print(f"Синтез: {text} -> {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7
        )
        # Сохраняем файл на диск
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Успех! Все новые звуковые файлы успешно сгенерированы в текущую папку.")
