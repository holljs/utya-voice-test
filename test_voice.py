import os
import soundfile as sf
from supertonic import TTS

print("Инициализация Supertonic 3 TTS...")
tts = TTS(auto_download=True)
style = tts.get_voice_style(voice_name="F4")

quiz_phrases = {
    # === СКАЗКА: ЛЕСНОЙ ОБМЕН (ЦЕПОЧКА) ===
    "chain_story_1.wav": "Одна́жды.. хи́трая лиса́.. нашла́ под де́ревом.. краси́ивую коро́обку.",
    "chain_story_2.wav": "Она́ обра́довалась.. и поду́умала, что внутри́ лежи́т.. сла́адкая я́года.",
    "chain_story_3.wav": "Но когда́ она́ откры́ыла коро́бку.. та́м оказа́лась.. то́олько бе́лая ко́ость.",
    "chain_story_4.wav": "В э́тот моме́нт.. из кусто́ов вы́бежала.. голо́одная соба́ака.",
    "chain_story_5.wav": "Лиса́ отдала́ ко́сть.. а соба́ака подари́ла ей.. большо́ой жёлудь.",
    "chain_story_6.wav": "Лиса́ расколо́ла жёлудь.. а внутри́ оказа́лся.. густо́ой.. сла́адкий мёёд!",
    
    # === ПОЛНЫЕ СЛОВА (с ударениями для правильной интонации) ===
    # 2 слога
    "w_lisa.wav": "лиса́", "w_ryba.wav": "ры́ба", "w_kasha.wav": "ка́ша",
    "w_medved.wav": "медве́дь", "w_zaychik.wav": "за́йчик", "w_myshka.wav": "мы́шка",
    "w_banan.wav": "бана́н", "w_domik.wav": "до́мик", "w_krysha.wav": "кры́ша",
    "w_limon.wav": "лимо́н", "w_lodka.wav": "ло́дка", "w_myachik.wav": "мя́чик",
    "w_okno.wav": "окно́", "w_poezd.wav": "по́езд", "w_zholud.wav": "жёлудь",
    "w_arbuz.wav": "арбу́з", "w_oreh.wav": "оре́х", "w_tykva.wav": "ты́ква",
    "w_chashka.wav": "ча́шка", "w_gribok.wav": "грибо́к",
    
    # 3 слога
    "w_sobaka.wav": "соба́ка", "w_raketa.wav": "раке́та", "w_mashina.wav": "маши́на",
    "w_kapusta.wav": "капу́ста", "w_moloko.wav": "молоко́", "w_morkovka.wav": "морко́вка",
    "w_ogurets.wav": "огуре́ц", "w_yabloko.wav": "я́блоко", "w_yagoda.wav": "я́года",
    "w_korobka.wav": "коро́бка", "w_kostochka.wav": "ко́сточка", "w_rediska.wav": "реди́ска",
    "w_klubnika.wav": "клубни́ка", "w_slonenok.wav": "слонёнок",
    
    # 4 слога
    "w_kukuruza.wav": "кукуру́за", "w_avtomobil.wav": "автомоби́ль",
    "w_lokomotiv.wav": "локомоти́в", "w_medvezhonok.wav": "медвежо́нок",
    "w_zemlyanika.wav": "земляни́ка",

    # === УНИКАЛЬНЫЕ СЛОГИ (без дубликатов) ===
    "sl_li.wav": "ли", "sl_sa.wav": "са", "sl_ry.wav": "ры", "sl_ba.wav": "ба",
    "sl_ka.wav": "ка", "sl_sha.wav": "ша", "sl_med.wav": "мед", "sl_ved.wav": "ведь",
    "sl_zay.wav": "зай", "sl_chik.wav": "чик", "sl_mysh.wav": "мыш", "sl_nan.wav": "нан",
    "sl_do.wav": "до", "sl_mik.wav": "мик", "sl_kry.wav": "кры", "sl_mon.wav": "мон",
    "sl_lod.wav": "лод", "sl_mya.wav": "мя", "sl_ok.wav": "ок", "sl_no.wav": "но",
    "sl_po.wav": "по", "sl_ezd.wav": "езд", "sl_zho.wav": "жё", "sl_lud.wav": "лудь",
    "sl_ar.wav": "ар", "sl_buz.wav": "буз", "sl_o.wav": "о", "sl_reh.wav": "рех",
    "sl_tyk.wav": "тык", "sl_va.wav": "ва", "sl_chash.wav": "чаш", "sl_gri.wav": "гри",
    "sl_bok.wav": "бок", "sl_so.wav": "со", "sl_ra.wav": "ра", "sl_ke.wav": "ке",
    "sl_ta.wav": "та", "sl_ma.wav": "ма", "sl_shi.wav": "ши", "sl_na.wav": "на",
    "sl_pus.wav": "пус", "sl_mo.wav": "мо", "sl_lo.wav": "ло", "sl_ko.wav": "ко",
    "sl_mor.wav": "мор", "sl_kov.wav": "ков", "sl_gu.wav": "гу", "sl_rets.wav": "рец",
    "sl_yab.wav": "яб", "sl_ya.wav": "я", "sl_go.wav": "го", "sl_da.wav": "да",
    "sl_rob.wav": "роб", "sl_kos.wav": "кос", "sl_toch.wav": "точ", "sl_re.wav": "ре",
    "sl_dis.wav": "дис", "sl_klub.wav": "клуб", "sl_ni.wav": "ни", "sl_slo.wav": "сло",
    "sl_nyo.wav": "нё", "sl_nok.wav": "нок", "sl_ku.wav": "ку", "sl_ru.wav": "ру",
    "sl_za.wav": "за", "sl_av.wav": "ав", "sl_to.wav": "то", "sl_bil.wav": "биль",
    "sl_tiv.wav": "тив", "sl_ve.wav": "ве", "sl_zem.wav": "зем", "sl_lya.wav": "ля"
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
        # Вернули правильную частоту 24000!
        sf.write(filename, wav.squeeze(), 54000)
    except Exception as e:
        print(f"❌ Ошибка при генерации {filename}: {e}")

print("✅ Готово!")
