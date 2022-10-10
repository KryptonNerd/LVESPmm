def ESPMM_calc(pitch,starts,rs,rb,steps,usteps):
    ls = pitch * starts
    espmm = steps * usteps * (rb**2)/(ls * (rs**2))
    return espmm


#x = ESPMM_calc(0.8, 1, 9.565, 2, 200, 16)
#print(x)
