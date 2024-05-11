# h=00
# m=00
# s=00
# for h in range(00, 23):
#     h = h+1
#     for m in range(00, 59):
#         m = m+1
#         for s in range(00, 60):
#             print(f"{h}H-{m}m-{s}s")
#             s = s+1


for horas in range(0,24):
    for minutos in range(0,60):
        for segundos in range(0,60):
            print(f"{horas:02d} {minutos:02d} {segundos:02d}")