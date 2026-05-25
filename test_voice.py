import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

# Полный список фраз для игры "Кто что ест?"
# По вашей просьбе: на букву У ударения НЕ ставятся (никаких ý), на остальные гласные - ставятся.
phrases = {
    "f_intro.wav": "Угадáй, кто что ест? Покорми́ живóтных!",
    "f_yum.wav": "Ам-ням-ням! Вкусно!",
    "f_win.wav": "Урá! Все живóтные сы́ты!",
    "f_cat.wav": "Кóшка ест.",
    "f_dog.wav": "Собáка ест.",
    "f_cow.wav": "Корóва ест.",
    "f_horse.wav": "Лóшадь ест.",
    "f_sheep.wav": "Овцá ест.",
    "f_pig.wav": "Свинья́ ест.",
    "f_goat.wav": "Козá ест.",
    "f_wolf.wav": "Волк ест.",
    "f_goose.wav": "Гусь ест.",
    "f_frog.wav": "Лягуушка ест.",
    "f_lion.wav": "Лев ест.",
    "f_tiger.wav": "Тигр ест.",
    "f_bee.wav": "Пчелá ест.",
    "f_fox.wav": "Лисá ест.",
    "f_hedgehog.wav": "Ёжик ест.",
    "f_hen.wav": "Курица ест.",
    "f_rooster.wav": "Петушóк ест.",
    "f_donkey.wav": "Ослик ест.",
    "f_mouse.wav": "Мы́шка ест."
}

print(f"Запуск озвучки {len(phrases)} фраз для мега-кормления...")

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

print("✅ Готово! Все звуковые файлы для новой комнаты успешно сгенерированы.")
