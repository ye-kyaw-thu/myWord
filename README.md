# myWord
syllable, word and phrase segmenter for Burmese (Myanmar language)  
(Plan to release soon & please wait...)   

ဗမာစာ စာလုံးတွေကို ပေါ့ပေါ့ပါးပါးနဲ့ ဖြတ်ပေးနိုင်ပြီး developer တွေက လွယ်လွယ်ကူကူ ယူသုံးနိုင်တဲ့ ပြီးတော့လည်း မြန်မြန်ဆန်ဆန်နဲ့ ကိုယ့်စက်ထဲမှာ extend လုပ်နိုင်တဲ့ "syllable, word, phrase segmentation" လုပ်ပေးနိုင်တဲ့ segmentation tool က ဒီနေ့အထိ မရှိသေးဘူးလို့ နားလည်ထားတယ်။ အဲဒီ ကွက်လပ်ကိုဖြည့်နိုင်ဖို့ရည်ရွယ်ပြီးတော့ myWord ကို R&D လုပ်ခဲ့ပါတယ်။  

အားလုံး ပြီးစီးနေပေမဲ့ coding မှာ comment တွေ လိုက်ဖြည့်ဖို့နဲ့ final evaluation လုပ်ဖို့ကျန်နေသေးတာနဲ့ ပြီးတော့တခြား အလုပ်တွေနဲ့မအားတာနဲ့ မတင်ပေးနိုင်သေးဘူး ဖြစ်နေတယ်...  

Note: WAT2021 Machine Translation Share Task အလုပ်မှာ word segmentation လုပ်ဖို့အတွက် myWord ကိုသုံးထားတဲ့အတွက် စာတမ်းထဲမှာ link ထည့်ပေးလိုက်နိုင်ဖို့အတွက် repository ကို အရင်ဆောက်ထားလိုက်တာ။ ဒီလထဲမှာ release လုပ်ပေးနိုင်အောင် အချိန်လုမယ်...

Draft Writing ...  


## Unsupervised Phrase Segmentation with NPMI

Wrod2Vec နဲ့ ပတ်သက်တဲ့ နာမည်ကြီး စာတမ်းနှစ်စောင် ကို အရင်ဆုံး refer လုပ်ချင်ပါတယ်။

ပထမစာတမ်း ဖြစ်တဲ့ [Efficient Estimation of Word Representations in Vector Space, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲမှာ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။

```We have included in our test set only single token words, thus multi-word entities are not present (such as New York).```

ပထမစာတမ်းရဲ့ test set မှာ single token word တွေပဲ သုံးထားကြောင်း ဖော်ပြထားပါတယ်။ ဆိုလိုတာက "New York", "ice cream", "high school", "hot dog", "living room", "full moon", "up to date", "part-time work", "state of the art" တို့လို စာလုံး နှစ်လုံးနဲ့ အထက်တွဲနေတဲ့ စကားလုံးတွေ (word) တွေကို word2vec အနေနဲ့ train လုပ်မယ်ဆိုရင် အရင်ဆုံး အမြဲတမ်း တွဲပြီးသုံးနေတဲ့ စာလုံးတွဲတွေ တနည်းအားဖြင့် phrase တွေကို ငါတို့က ကြိုသိဖို့ လိုအပ်ပါတယ်။ အဲဒီလို သိပြီးမှသာ word2vec ကို train မလုပ်ခင်မှာ preprocessing အနေနဲ့ ဥပမာ "new_york", "ice_cream", ..., "up_to_date", "part_time_work", "state_of_the_art" အဖြစ် underscore နဲ့ တွဲတာမျိုး လုပ်ပြီး စာလုံးတစ်လုံးအနေနဲ့ training corpus ထဲမှာ ကြိုပြင်ထားဖို့ လိုအပ်ပါလိမ့်မယ်။ အဲဒီ လိုမျိုး NLP task အတွက်က supervised approach နဲ့ ဆိုရင် NER (Name Entity Recognition) model နဲ့ လုပ်လို့ ရပေမဲ့ NER model ဆောက်ဖို့အတွက်က NER corpus က ရှိနေမှ ဖြစ်ပါလိမ့်မယ်။ အဲဒါကြောင့် NER corpus ကို မသုံးပဲနဲ့ unsupervised approach အနေနဲ့ သွားမယ်ဆိုရင် ဘယ်လို လုပ်လို့ ရနိုင်တယ် ဆိုတာကို Word2Vec ရဲ့ဒုတိယစာတမ်းလို့ ပြောလို့ရတဲ့ [Distributed Representations of Words and Phrases and their Compositionality, (Mikolov et al., 2013)](https://arxiv.org/pdf/1310.4546.pdf) စာတမ်းထဲရဲ့ Section 4. Learning Phrases မှာ Formula No. 6 အနေနဲ့ အောက်ပါအတိုင်း ဖော်ပြထားတာကို တွေ့ရပါလိမ့်မယ်။  


<img src="https://github.com/ye-kyaw-thu/myWord/blob/main/documentation/formula-6.png" />

ဒီနေရာမှာ ပြောနေတဲ့ n (v, w), n (v), n (w) တွေက bigram နဲ့ unigram frequency တွေ ဖြစ်ပြီးတော့ δ က frequency နိမ့်တဲ့ စကားလုံးတွဲတွေက ထိပ်ပိုင်းကို ရောက်မလာဖို့အတွက် ထိန်းညှိတဲ့ discount factor ပါ။ Phrase တွေကို ဆွဲထုတ်နိုင်ဖို့အတွက်က threshold တစ်ခု သတ်မှတ်ထားပြီး အဲဒီ threshold value အထက်မှာ ရှိတဲ့ bigram စကားလုံးတွဲတွေကို ရွေးယူလိုက်ယုံပါပဲ။ Threshold value အထက် ဆိုတာကို probability အနေနဲ့ စဉ်းစားကြည့်ရင် p (v, w) = n (v, w) / N, p (v) = n (v) / N, p (w) = n ဆိုပြီး ဖော်မြူလာအနေနဲ့ ရေးလို့ ရပါတယ်။ ဒီနေရာမှာ "N" ဆိုတာက unigram စုစုပေါင်းတန်ဖိုးပါ။ δ ကို ဖယ်ပြီးတော့ score တွက်ဖို့အတွက် စဉ်းစားရင် အောက်ပါအတိုင်း ရေးလို့ ရပါတယ်

score (v, w) = n (v, w) / (n (v) * n (w)) = (p (v, w) * N) / (p (v) * N * p (w) * N) = p (v, w) / (p (v) * p (w) * N)

ဒါကြောင့် ဒီ score တွက်တဲ့ အပိုင်းက self-mutual information PMI တွက်တဲ့ PMI (v, w) = log p (v, w) / (p (v) * p (w)) ဆိုတဲ့ ဖော်မြူလာနဲ့ အကုန်လုံးလိုလို ဆင်တူဖြစ်တာကို တွေ့ရပါလိမ့်မယ်။ ဒါပေမဲ့ သေသေချာချာ ပြန် နှိုင်းယှဉ်ကြည့်တဲ့ အခါမှာ၊ အော်ရဂျင်နယ် ဖော်မြူလာမှာက 1/N ဆိုတဲ့ factor က ပါဝင်ပြီးတော့ အဲဒါက corpus အပေါ်မှာ မူတည်နေလို့ ထွက်လာမယ့် score က အခြေခံအားဖြင့် corpus ရဲ့ length ပေါ်မှာ သွားပြီး မူတည်နေပါတယ်။ corpus ကို အပြောင်းအလဲ ထပ်တိုးတာမျိုး မလုပ်ပဲ fixed လုပ်ထားပြီးတော့ threshold တန်ဖိုးကို search လုပ်တာမျိုးလုပ်ရင်တော့ အတိုင်းအတာ တစ်ခုအထိ ပြေလည်ပေမဲ့ threshold ရဲ့ အဓိပ္ပါယ်က နားလည်ရခက်တဲ့အပြင် length မတူတဲ့ စာကြောင်းတွေကို သုံးပြီးတော့ score တွေကို နှိုင်းယှဉ်ကြည့်ပြီးသွားမယ်ဆိုရင် ရလာတဲ့ phrase တွေက ပုံမှန် လူတွေက သုံးနေကြတဲ့ phrase နဲ့တော့ တထပ်တည်း ကျမှာ မဟုတ်ပါဘူး။  

