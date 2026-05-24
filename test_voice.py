import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

phrases = {
    # === 1. НАЗВАНИЯ БУКВ (Режим "🗣️ Буквы") ===
    "n_b_a.wav": "А.",
    "n_b_b.wav": "Бэ.",
    "n_b_v.wav": "Вэ.",
    "n_b_g.wav": "Гэ.",
    "n_b_d.wav": "Дэ.",
    "n_b_e.wav": "Е.",
    "n_b_yo.wav": "Ё.",
    "n_b_zh.wav": "Жэ.",
    "n_b_z.wav": "Зэ.",
    "n_b_i.wav": "И.",
    "n_b_y.wav": "И крáткое.",
    "n_b_k.wav": "Ка.",
    "n_b_l.wav": "Эль.",
    "n_b_m.wav": "Эм.",
    "n_b_n.wav": "Эн.",
    "n_b_o.wav": "О.",
    "n_b_p.wav": "Пэ.",
    "n_b_r.wav": "Эр.",
    "n_b_s.wav": "Эс.",
    "n_b_t.wav": "Тэ.",
    "n_b_u.wav": "У.",          # Без ударения!
    "n_b_f.wav": "Эф.",
    "n_b_h.wav": "Ха.",
    "n_b_ts.wav": "Цэ.",
    "n_b_ch.wav": "Чэ.",
    "n_b_sh.wav": "Ша.",
    "n_b_sch.wav": "Ща.",
    "n_b_tv.wav": "Твё́рдый знак.",
    "n_b_ы.wav": "Ы.",
    "n_b_myag.wav": "Мя́гкий знак.",
    "n_b_e_ob.wav": "Э.",
    "n_b_yu.wav": "Ю.",
    "n_b_ya.wav": "Я.",

    # === 2. ЗВУКИ-АССОЦИАЦИИ (Режим "🔊 Звуки") ===
    "s_b_a.wav": "Ааа-ааа.",
    "s_b_b.wav": "Ба-бáх!",
    "s_b_v.wav": "Вввввв.",
    "s_b_g.wav": "Га-га-гá.",
    "s_b_d.wav": "Дын-ды́н.",
    "s_b_e.wav": "Е-е-хáли!",
    "s_b_yo.wav": "Пы́х-пы́х.",
    "s_b_zh.wav": "Жжжжжж.",
    "s_b_z.wav": "Зззззз.",
    "s_b_i.wav": "И-го-гó!",
    "s_b_y.wav": "Ой-óй!",
    "s_b_k.wav": "Кап-кáп.",
    "s_b_l.wav": "Ла-ла-лá.",
    "s_b_m.wav": "Мууууу.",      # Хак для У
    "s_b_n.wav": "Но-нó!",
    "s_b_o.wav": "Ооооох!",
    "s_b_p.wav": "Пи-пи-пи.",
    "s_b_r.wav": "Рррррр!",
    "s_b_s.wav": "Сссссс.",
    "s_b_t.wav": "Туу-тýу!",     # Хак для У
    "s_b_u.wav": "Уууууу.",      # Хак для У
    "s_b_f.wav": "Фыр-фы́р.",
    "s_b_h.wav": "Ха-ха-хá!",
    "s_b_ts.wav": "Цып-цы́п.",
    "s_b_ch.wav": "Чок-чóк.",
    "s_b_sh.wav": "Шшшшшш.",
    "s_b_sch.wav": "Щё́лкает.",
    "s_b_tv.wav": "Твё́рдо.",
    "s_b_ы.wav": "Ыыыы.",
    "s_b_myag.wav": "Мя́гко.",
    "s_b_e_ob.wav": "Э́й!",
    "s_b_yu.wav": "Юлá.",
    "s_b_ya.wav": "Я сáм!",

    # === 3. ВОПРОСЫ ДЛЯ ВИКТОРИНЫ (Режим "🎓 Игра") ===
    "q_b_a.wav": "Где бýква А?",
    "q_b_b.wav": "Где бýква Бэ?",
    "q_b_v.wav": "Где бýква Вэ?",
    "q_b_g.wav": "Где бýква Гэ?",
    "q_b_d.wav": "Где бýква Дэ?",
    "q_b_e.wav": "Где бýква Е?",
    "q_b_yo.wav": "Где бýква Ё?",
    "q_b_zh.wav": "Где бýква Жэ?",
    "q_b_z.wav": "Где бýква Зэ?",
    "q_b_i.wav": "Где бýква И?",
    "q_b_y.wav": "Где бýква И крáткое?",
    "q_b_k.wav": "Где бýква Ка?",
    "q_b_l.wav": "Где бýква Эль?",
    "q_b_m.wav": "Где бýква Эм?",
    "q_b_n.wav": "Где бýква Эн?",
    "q_b_o.wav": "Где бýква О?",
    "q_b_p.wav": "Где бýква Пэ?",
    "q_b_r.wav": "Где бýква Эр?",
    "q_b_s.wav": "Где бýква Эс?",
    "q_b_t.wav": "Где бýква Тэ?",
    "q_b_u.wav": "Где бýква У?",       # Без ударения!
    "q_b_f.wav": "Где бýква Эф?",
    "q_b_h.wav": "Где бýква Ха?",
    "q_b_ts.wav": "Где бýква Цэ?",
    "q_b_ch.wav": "Где бýква Чэ?",
    "q_b_sh.wav": "Где бýква Ша?",
    "q_b_sch.wav": "Где бýква Ща?",
    "q_b_tv.wav": "Где твё́рдый знак?",
    "q_b_ы.wav": "Где бýква Ы?",
    "q_b_myag.wav": "Где мя́гкий знак?",
    "q_b_e_ob.wav": "Где бýква Э?",
    "q_b_yu.wav": "Где бýква Ю?",
    "q_b_ya.wav": "Где бýква Я?"
}

print(f"Начинаем чистую раздельную озвучку {len(phrases)} файлов для Букв...")

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

print("✅ Идеально! Все файлы сгенерированы по отдельным папкам-режимам.")
