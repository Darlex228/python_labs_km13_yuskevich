f_tpl = ('Liverpool', 845.15, 21, 134, 358.45, 'price')
print('The initial lot {} of ${} at the {} auction exceeded the expected {} by {}%, but the lot with number {} was nevertheless sold for ${}.'.format(f_tpl[5], round(f_tpl[4], 1), f_tpl[0], f_tpl[5], f_tpl[2], str(f_tpl[3]).zfill(4), int(f_tpl[1])))
