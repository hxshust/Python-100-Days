#coding=utf-8

salary = float(input('输入月工资'))
bonus = float(input('输入年终奖'))
# bonus_rate = float(input('年终奖月均税率（计算包含速算扣除数）'))
insurance_rate = 0.11
house_rate = float(input('输入公积金费率(五险费率默认为11%,公积金范围5-12%)'))
value = salary - salary*(insurance_rate + house_rate) - 5000
if value <= 0:
    tax_rate = 0
elif value <= 3000:
    tax_rate = 0.03
elif value <= 12000:
    tax_rate = 0.1
elif value <= 25000:
    tax_rate = 0.2
elif value <= 35000:
    tax_rate = 0.25
elif value <= 55000:
    tax_rate = 0.3
elif value <= 80000:
    tax_rate = 0.35
else:
    tax_rate = 0.45

bonus_month = bonus / 12
if bonus_month <= 3000:
    bonus_cut = 0
    bonus_rate = 0.03
elif bonus_month <= 12000:
    bonus_rate = 0.1
    bonus_cut = 210
elif bonus_month <= 25000:
    bonus_rate = 0.2
    bonus_cut = 1410
else :
    print 'you must be kidding!'



salary_in_fact = salary - salary * (insurance_rate + house_rate) - value * tax_rate
salary_in_fact_contain = salary_in_fact + salary * 2 *house_rate
salary_years_averag = (salary_in_fact * 12 + (bonus - bonus * bonus_rate - bonus_cut*12 ))/12
print 'vaule',value
print '实际到手工资为 ' ,salary_in_fact
print  '实际到手工资为（含公积金） ' ,salary_in_fact_contain
print  '包含年终奖不含公积金的平均月工资' ,salary_years_averag
