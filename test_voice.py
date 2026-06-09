import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # 1. УТЯ
    "p_q1.wav": "На́ша Уутя ло́вко ска́чет, ло́вит крууглый, я́ркий...",
    "p_opt_myach.wav": "Мя́чик", "p_opt_mashinka.wav": "Маши́нка", "p_opt_domik.wav": "До́мик",
    "p_f1.wav": "...мя́чик!",

    # 2. МИШКА
    "p_q2.wav": "Ми́шка по́ лесу идё́т, и́щет сла́дкий, вкуусный...",
    "p_opt_med.wav": "Мё́д", "p_opt_grib.wav": "Гри́б", "p_opt_yagoda.wav": "Я́года",
    "p_f2.wav": "...мё́д!",

    # 3. ЗАЙКА
    "p_q3.wav": "За́йка развива́л сноро́вку, на́ полуу нашё́л...",
    "p_opt_morkovka.wav": "Марко́вку", "p_opt_kapusta.wav": "Капуусту", "p_opt_yabloko.wav": "Я́блоко",
    "p_f3.wav": "...марко́вку!",

    # 4. МЫШОНОК
    "p_q4.wav": "Уу мышо́нка сего́дня пи́р, емуу подари́ли...",
    "p_opt_sir.wav": "Сы́р", "p_opt_tort.wav": "То́рт", "p_opt_banan.wav": "Бана́н",
    "p_f4.wav": "...сы́р!",

    # 5. ОБЕЗЬЯНКА
    "p_q5.wav": "Жё́лтый, сла́дкий, ка́к луна́, обезья́нка е́ст...",
    "p_opt_ogurec.wav": "Агуре́ц", "p_opt_limon.wav": "Лимо́н",
    "p_f5.wav": "...бана́н!", # Банан уже есть выше, можно переиспользовать p_opt_banan.wav

    # 6. КОТИК
    "p_q6.wav": "Све́тит со́лнышко в окно́, ко́тик пьё́т из блю́дца...",
    "p_opt_moloko.wav": "Малако́", "p_opt_sok.wav": "Со́к", "p_opt_chay.wav": "Ча́й",
    "p_f6.wav": "...малако́!",

    # 7. ТАКСИСТ
    "p_q7.wav": "Е́дет по́ дороге бы́стро, за́ рулё́м сиди́т такси́ст там. Уу неё́ четы́ре ши́ны, э́то си́няя...",
    "p_opt_mashina.wav": "Маши́на", "p_opt_lodka.wav": "Ло́дка", "p_opt_poezd.wav": "По́езд",
    "p_f7.wav": "...маши́на!",

    # 8. СТРОЙКА
    "p_q8.wav": "Что́бы стро́ить ба́шню вы́ше, мы́ поста́вим све́рху...",
    "p_opt_krisha.wav": "Кры́шу", "p_opt_okno.wav": "Акно́", "p_opt_dver.wav": "Две́рь",
    "p_f8.wav": "...кры́шу!"
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

print("✅ Готово!")
