# myWord
syllable, word and phrase segmenter for Burmese (Myanmar language)  
(Plan to release soon & please wait...)   

ဗမာစာ စာလုံးတွေကို ပေါ့ပေါ့ပါးပါးနဲ့ ဖြတ်ပေးနိုင်ပြီး developer တွေက လွယ်လွယ်ကူကူ ယူသုံးနိုင်တဲ့ ပြီးတော့လည်း မြန်မြန်ဆန်ဆန်နဲ့ ကိုယ့်စက်ထဲမှာ extend လုပ်နိုင်တဲ့ "syllable, word, phrase segmentation" လုပ်ပေးနိုင်တဲ့ segmentation tool က ဒီနေ့အထိ မရှိသေးဘူးလို့ နားလည်ထားတယ်။ အဲဒီ ကွက်လပ်ကိုဖြည့်နိုင်ဖို့ရည်ရွယ်ပြီးတော့ myWord ကို R&D လုပ်ခဲ့ပါတယ်။  

အားလုံး ပြီးစီးနေပေမဲ့ coding မှာ comment တွေ လိုက်ဖြည့်ဖို့နဲ့ final evaluation လုပ်ဖို့ကျန်နေသေးတာနဲ့ ပြီးတော့တခြား အလုပ်တွေနဲ့မအားတာနဲ့ မတင်ပေးနိုင်သေးဘူး ဖြစ်နေတယ်...  

Note: WAT2021 Machine Translation Share Task အလုပ်မှာ word segmentation လုပ်ဖို့အတွက် myWord ကိုသုံးထားတဲ့အတွက် စာတမ်းထဲမှာ link ထည့်ပေးလိုက်နိုင်ဖို့အတွက် repository ကို အရင်ဆောက်ထားလိုက်တာ။ ဒီလထဲမှာ release လုပ်ပေးနိုင်အောင် အချိန်လုမယ်...

Draft Writing ...  


## Unsupervised Phrase Segmentation with NPMI

Wrod2Vec နဲ့ ပတ်သက်တဲ့ နာမည်ကြီး စာတမ်းနှစ်စောင် ကို အရင်ဆုံး refer လုပ်ချင်ပါတယ်။

ပထမစာတမ်း ဖြစ်တဲ့ [Efficient Estimation of Word Representations in Vector Space, Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲမှာ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။

```We have included in our test set only single token words, thus multi-word entities are not present (such as New York).```

ပထမစာတမ်းရဲ့ test set မှာ single token word တွေပဲ သုံးထားကြောင်း ဖော်ပြထားပါတယ်။ ဆိုလိုတာက "New York", "ice cream", "high school", "hot dog", "living room", "full moon", "up to date", "part-time work", "state of the art" တို့လို စာလုံး နှစ်လုံးနဲ့ အထက်တွဲနေတဲ့ စကားလုံးတွေ (word) တွေကို word2vec အနေနဲ့ train လုပ်မယ်ဆိုရင် အရင်ဆုံး အမြဲတမ်း တွဲပြီးသုံးနေတဲ့ စာလုံးတွဲတွေ တနည်းအားဖြင့် phrase တွေကို ငါတို့က ကြိုသိဖို့ လိုအပ်ပါတယ်။ အဲဒီလို သိပြီးမှသာ word2vec ကို train မလုပ်ခင်မှာ preprocessing အနေနဲ့ ဥပမာ "new_york", "ice_cream", ..., "up_to_date", "part_time_work", "state_of_the_art" အဖြစ် underscore နဲ့ တွဲတာမျိုး လုပ်ပြီး စာလုံးတစ်လုံးအနေနဲ့ training corpus ထဲမှာ ကြိုပြင်ထားဖို့ လိုအပ်ပါလိမ့်မယ်။ အဲဒီ လိုမျိုး NLP task အတွက်က supervised approach နဲ့ ဆိုရင် NER (Name Entity Recognition) model နဲ့ လုပ်လို့ ရပေမဲ့ NER model ဆောက်ဖို့အတွက်က NER corpus က ရှိနေမှ ဖြစ်ပါလိမ့်မယ်။ အဲဒါကြောင့် NER corpus ကို မသုံးပဲနဲ့ unsupervised approach အနေနဲ့ သွားမယ်ဆိုရင် ဘယ်လို လုပ်လို့ ရနိုင်တယ် ဆိုတာကို Word2Vec ရဲ့ဒုတိယစာတမ်းလို့ ပြောလို့ရတဲ့ [Distributed Representations of Words and Phrases and their Compositionality, Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲရဲ့ Section 4. Learning Phrases မှာ Formula No. 6 အနေနဲ့ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။  

<img src="https://render.githubusercontent.com/render/math?math=e^{i \pi} = -1">
