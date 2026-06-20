import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === СТИШКИ ДЛЯ КОМНАТЫ "ДА И НЕТ" ===
    
    # ❌ Ответ НЕТ
    "yesno_bag.wav": """Ве́щи мы в бага́жник сло́жим,
И игруушки в пууть возьмём.
Запихнём туда́ буфе́т?
Ска́жем вме́сте хо́ром:… НЕ́Т!""",

    "yesno_elephant.wav": """Лю́бит ко́тик пить кефи́р,
А мышо́нок лю́бит сы́р.
Слон скуушал вдрууг брасле́т?
Мы отве́тим друужно:… НЕ́Т!""",

    "yesno_garden.wav": """В огоро́де посади́ли
Огурцы́ и кабачки́.
Вы́растет ли там мопе́д?
Захохо́чем гро́мко:… НЕ́Т!""",

    # ✅ Ответ ДА
    "yesno_walk.wav": """Мы наде́нем босоно́жки,
Побежи́м мы по доро́жке!
Све́тит со́лнце нам всегда́?
Де́тки зво́нко кри́кнут:… ДА́!""",

    "yesno_pie.wav": """Ма́ма испечёт пиро́г,
Сла́дкий-сла́дкий, как медо́к!
Я́год бро́сим мы туда́?
Ска́жем хо́ром сло́во… ДА́!""",

    "yesno_hands.wav": """Мы испа́чкали ладо́шки,
Пока́ пры́гали немно́жко.
Смо́ет грязь у нас вода́?
Мы отве́тим друужно:… ДА́!"""
}

print(f"Запуск озвучки {len(quiz_phrases)} фраз...")

for filename, text in quiz_phrases.items():
    print(f"Синтез: {filename}")
    try:
        wav, duration = tts.synthesize(
            text=text,
            lang="ru",
            voice_style=style,
            total_steps=10,
            speed=0.7 
        )
        # Магия Ути-Те (частота 54000)
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
