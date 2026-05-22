# Câu 1
price = float(input('Nhập vào giá tiền của sản phẩm: '))
quantity = int(input('Nhập vào số lượng sản phẩm: '))

total = price * quantity

if total >= 1000000:
    total *= 0.9
else:
    total = total

print(f'Số tiền phải thanh toán là: {total}')

# Câu 2
password = '123456'
count = 3
current_attempt = 1
user_number = -1

while current_attempt <= count and user_number != password:
    user_number = input('Nhập mật khẩu của bạn: ')
    
    if user_number != password and current_attempt <= count:
        print('Mật khẩu sai, vui lòng nhập lại!')
    current_attempt += 1
    
if user_number == password:
    print('Đăng nhập thành công!')
else:
    print('Tài khoản đã bị khóa!')
    
# Câu 3
total_box = 0
total_quantity = 0

while True:
    val = int(input('Nhập số lượng sản phẩm của thùng (nhập 0 để thoát): '))

    if val < 0:
        print('Số lượng không hợp lệ, bỏ qua thùng này!')
        continue

    if val == 0:
        break

    total_quantity += val
    total_box += 1

print(f'Tổng số thùng hàng hợp lệ đã đếm: {total_box}')
print(f'Tổng số lượng sản phẩm thu được: {total_quantity}')
