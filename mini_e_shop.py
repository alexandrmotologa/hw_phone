# PRODUCTS
# DATA LAYER
p_1_name = 'IPhone IX'
p_1_price = 1000
p_1_q = 3
P_1_ava = True


p_2_name = 'IPhone XI'
p_2_price = 2000
p_2_q = 0
P_2_ava = False


p_3_name = 'Xiaomi Mi 9T Pro'
p_3_price = 450
p_3_q = 99
P_3_ava = True

# LOGIC LAYER
p_total_q = p_1_q + p_2_q + p_3_q
p_total_c = p_1_q * p_1_price + p_2_q * p_2_price + p_3_q * p_3_price
p_total_ava = P_1_ava and P_2_ava and P_3_ava

# PRESENTATION LAYER
print("\u26CC"*40)
print("TOTAL PHONES: " + str(p_total_q))
print("TOTAL WORTH: " + str(p_total_c))
print("IS " + p_1_name + " Available?\n\t" + str(P_1_ava))
print("IS " + p_2_name + " Aavailable?\n\t" + str(P_2_ava))
print("IS " + p_3_name + " Aavailable?\n\t" + str(P_3_ava))
print("ARE ALL AVAILABLE?\n\t" + str(p_total_ava))
print("\u26CC"*40)
