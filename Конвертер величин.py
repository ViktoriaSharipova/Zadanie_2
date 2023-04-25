d_ft = int(input("Введите расстояние в метрах: "))
d_santimetr = d_ft * 100
d_detsimetr = d_ft * 10
d_millimetr = d_ft * 1000
d_mil = d_ft * 0.0006213711922373339
print("Расстояние в сантиметрах %i см." % d_santimetr)
print("Расстояние в дециметрах %i дм." % d_detsimetr)
print("Расстояние в миллиметрах %i мм." % d_millimetr)
print("Расстояние в милях %f, mil." % d_mil)