#sprint3a

# 1) x dəyişəni verilmişdir. Əgər x > 0 olarsa "müsbət", x < 0 olarsa "mənfi", bərabərdirsə "sıfır" çap etsin.
x = -4
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2) n rəqəmi cütdürsə "cüt", təkdirsə "tək" çap etsin.
n = 7
if n % 2 == 0:
    print("cüt")
else:
    print("tək")

# 3) a, b, c rəqəmləri verilmişdir. Ən böyük rəqəmi çap etsin.
a, b, c = 15, 20, 10
print("Ən böyük:", max(a, b, c))

# 4) day dəyişəni 1-7 arası rəqəmdir. Müvafiq həftə gününü çap etsin, əks halda "Yanlış gün" yazsın.
day = 5
days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(days.get(day, "Yanlış gün"))

# 5) temp dəyişəni temperaturdur. Şərtə uyğun qiymətləndirmə çap etsin.
temp = 18
if temp < 0:
    print("soyuq")
elif temp <= 20:
    print("normal")
else:
    print("isti")

# 6) password adlı string verilmişdir. Uzunluğa görə qiymətləndirilsin.
password = "parol12345"
length = len(password)
if length < 8:
    print("qısa")
elif length <= 12:
    print("orta")
else:
    print("uzun")

# 7) x rəqəmi həm 3-ə, həm də 5-ə bölünürsə və s. şərtə uyğun çap etsin.
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8) 0-dan 20-yə qədər cüt rəqəmləri çap etsin.
for i in range(0, 21, 2):
    print(i)

# 9) "Bağda ərik var idi …" stringinin hər elementini for ilə ayrı-ayrılıqda çap edin.
text = "Bağda ərik var idi …"
for char in text:
    print(char)

# 10) 1-dən 10-a qədər rəqəmləri çap edin, amma 3 xaric.
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11) 1-dən başlayaraq ilk 5-ə bölünən rəqəmi tapın və while ilə çap edin (break istifadə edin).
i = 1
while True:
    if i % 5 == 0:
        print("İlk 5-ə bölünən:", i)
        break
    i += 1

# 12) (1, 3, 5, 7, 9) listində 5-i tapın və indeksini çap edin (break istifadə edin).
nums = [1, 3, 5, 7, 9]
for index in range(len(nums)):
    if nums[index] == 5:
        print("5-in indeksi:", index)
        break











#sprint 3b


# 1) salam adlı funksiya yaradın ki, heç bir arqument almadan sadəcə "Salam, Dünya!" çap etsin.
def salam():
    print("Salam, Dünya!")

# 2) kub_hesabla adlı funksiya yaradın ki, bir rəqəm (n) qəbul etsin və onun kubunu qaytarsın.
def kub_hesabla(n):
    return n ** 3

# 3) birlesdir adlı funksiya yaradın ki, iki söz qəbul etsin və onları boşluqla birləşdirib qaytarsın.
def birlesdir(s1, s2):
    return s1 + " " + s2

# 4) cap_et adlı funksiya yaradın ki, bir listi arqument olaraq alsın və listin hər elementini for ilə çap etsin.
def cap_et(lst):
    for element in lst:
        print(element)

# 5) toplam adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların cəmini qaytarsın.
def toplam(*args):
    return sum(args)

# 6) ortalama adlı funksiya yaradın ki, istənilən sayda rəqəmi (*args) qəbul edib onların ortalamasını qaytarsın
# (əgər heç bir rəqəm yoxdursa, "Rəqəm yoxdur" qaytarsın).
def ortalama(*args):
    if len(args) == 0:
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7) adlar_rəqəmlər adlı funksiya yaradın ki, istənilən sayda ad və rəqəm cütünü (**kwargs) qəbul edib
# hər cütü çap etsin (məsələn, "ad: bir, rəqəm: 1").
def adlar_reqemler(**kwargs):
    for ad, reqem in kwargs.items():
        print(f"ad: {ad}, rəqəm: {reqem}")

# 8) tip_yoxla adlı funksiya yaradın ki, bir dəyər qəbul edib onun tipini yoxlasın: "mətn", "rəqəm", "başqa" çap etsin.
def tip_yoxla(deyer):
    if isinstance(deyer, str):
        print("mətn")
    elif isinstance(deyer, (int, float)):
        print("rəqəm")
    else:
        print("başqa")

# 9) yas_kateqoriya adlı funksiya yaradın ki, input ilə yaş soruşsun, 18-dən aşağıysa "Gənc", yuxarıdırsa "Yetkin" çap etsin.
def yas_kateqoriya():
    yas = int(input("Yaşınızı daxil edin: "))
    if yas < 18:
        print("Gənc")
    else:
        print("Yetkin")

# 10) soz_uzunluq adlı funksiya yaradın ki, input ilə istifadəçidən söz alsın və onun uzunluğunu çap etsin.
def soz_uzunluq():
    soz = input("Söz daxil edin: ")
    print("Uzunluq:", len(soz))






#sprint 4a




# 1) İstifadəçidən iki rəqəm və bir əməliyyat (toplama, çıxma, vurma, bölmə) daxil etməsini tələb edən funksiya yazın.
# Mümkün xətaları (ValueError, TypeError və s.) idarə edin və müvafiq mesajlar çıxarın. 
# Sonda da "Hesablama bitdi" mesajı çap olunsun.

def kalkulyator():
    try:
        a = float(input("Birinci rəqəmi daxil edin: "))
        b = float(input("İkinci rəqəmi daxil edin: "))
        op = input("Əməliyyatı daxil edin (+, -, *, /): ")

        if op == '+':
            print("Nəticə:", a + b)
        elif op == '-':
            print("Nəticə:", a - b)
        elif op == '*':
            print("Nəticə:", a * b)
        elif op == '/':
            print("Nəticə:", a / b)
        else:
            print("Yanlış əməliyyat!")
    except ValueError:
        print("Rəqəmlər düzgün daxil edilməyib.")
    except ZeroDivisionError:
        print("0-a bölmək olmaz.")
    except TypeError:
        print("Daxil edilən dəyər yanlışdır.")
    finally:
        print("Hesablama bitdi")

# 2) 1-dən 50-yə qədər olan rəqəmlərdən yalnız 11ə qalıqsız bölünənlərini list olaraq qaytarın.
bolunen_11 = [x for x in range(1, 51) if x % 11 == 0]
print("11-ə bölünənlər:", bolunen_11)

# 3) Verilmiş sözlər siyahısından (["kitab", "qələm", "defter", "silgi"]) hər sözün ilk hərfini list olaraq qaytarın.
sozler = ["kitab", "qələm", "defter", "silgi"]
ilk_herfler = [s[0] for s in sozler]
print("İlk hərflər:", ilk_herfler)

# 4) Şəhər adları (["Bakı", "Gəncə", "Sumqayıt"]) və kodları ([12, 22, 18]) siyahılarından {şəhər: kod} dictionary olaraq qaytarın.
seherler = ["Bakı", "Gəncə", "Sumqayıt"]
kodlar = [12, 22, 18]
seher_kod = dict(zip(seherler, kodlar))
print("Şəhər və kodlar:", seher_kod)

# 5) Kilometri milə çevirən (mil = km * 0.621371) lambda funksiyası yazın və 5 fərqli dəyər üçün yoxlayın.
km_to_mil = lambda km: km * 0.621371
km_values = [1, 5, 10, 15, 20]
mil_values = list(map(km_to_mil, km_values))
print("Mil qiymətləri:", mil_values)

# 6) [100, 200, 300, 400] qiymətlərinə 18% vergi əlavə etmək üçün map() və lambda istifadə edin.
qiymetler = [100, 200, 300, 400]
vergi = list(map(lambda x: x * 1.18, qiymetler))
print("Vergili qiymətlər:", vergi)

# 7) [3, 7, 12] və [2, 4, 6] siyahılarının elementlərini ikiqat artırmaq və sonra cəmləmək üçün map() istifadə edin.
list1 = [3, 7, 12]
list2 = [2, 4, 6]
ikiqat_cem = list(map(lambda x, y: (x * 2) + (y * 2), list1, list2))
print("İkiqat cəmlər:", ikiqat_cem)

# 8) [150, 80, 220, 45] siyahısından ən kiçik qiyməti reduce() ilə tapın.
from functools import reduce
qiymet_list = [150, 80, 220, 45]
minimum = reduce(lambda a, b: a if a < b else b, qiymet_list)
print("Ən kiçik qiymət:", minimum)











