stop_words = {'동반한','손실한','상태이고','이상없음으로','눈에',"계속해서", "동반하고 있음", "동반한 상태이고", "동반함", "동반하고있음", "살짝 보이며", "섭취가 어려우며", "의심되고", "의심됨", "잇으며", "일으키면서", "있으며", "우려되고", "있다",'증상도','섭취가','어려우며','계속되는','어려우며','동반함','동반하였습니다','보이며','증세까지','판단됨','환자는','다른부분은','이상없으므로','불안하여','증상','눈','판단','증상만','없으며','심하고','심지어','유지됨','일으키고','상도','의심','이고','극심한','하고있음','보이','살짝','되어','입게','인해','일으키며','보인다','증세','음','심하며','이상','있고','조금','끼','음으로','없','부분','다른','파악','있으므로','관리','있음','위','시행','해야','합니다','겪고','된','대한','시급합니다','동반','있습니다','하였습니다','되는','나타나며','입원','나','머','됨','됌','면서','헤','보이게','씩','증도','닮다','다','없다','엔','힘들다','액체','까지','두','야하다','오늘','아침','오늘아침','커지다','급격하다','치가','나타나다','조','이상승','이송이','병원','력','지속','함피','함','즉시','집중','떨어지다','하고','심하다','인','적','며','필요하다','되어다','되었다','인하다','심해지다','계속','있다','심각하다','점점','때문','을','로','상','하','지다','않다','이다','되다','에서','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','아침','또','또한','가끔','감','코',"계,'속",'현재','이어진','상황','와','환자','도','과','대응','신속한','조치','인한','나타났습니다','되었습니다','호소','필요합니다','있습니다','입니다','의','에','를','은','는','이','가','으로','로','으','적','확인','불편','되었습니다','있습니다','면서','별','부분은','보임','씩','증도','닮다','다','없다','고','엔','힘들다','액체','까지','두','야하다','오늘','아침','오늘아침','커지다','급격하다','치가','나타나다','조','이상승','이송이','병원','력','지속','함피','함','즉시','집중','떨어지다','하고','심하다','인','적','며','필요하다','되어다','되었다','인하다','심해지다','계속','있다','심각하다','점점','때문','을','로','상','하','지다','않다','이다','되다','에서','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다','아침','또','또한','가끔','감','코',"계,'속",'현재','이어진','상황'}
compound_words = {}

#사지 = 사지마비
#손실 = 청각손실
#통증 = 가슴통증
#섭취 = 음식물섭취곤란
#상태 = 혼란상태
#부종 = 목의부종
#호흡 => 호흡음 유사도 0.99
#곤란 => 호흡곤란 유사도 0.99