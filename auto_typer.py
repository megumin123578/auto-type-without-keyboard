from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(3)

def convert_with_diacritics_to_without(text):
    conversion_dict = {
        'á': 'as', 'à': 'af', 'ả': 'ar', 'ã': 'ax', 'ạ': 'aj',
        'ă': 'aw', 'ắ': 'aws', 'ằ': 'awf', 'ẳ': 'awr', 'ẵ': 'awx', 'ặ': 'awj',
        'â': 'aa', 'ấ': 'aas', 'ầ': 'aaf', 'ẩ': 'aar', 'ẫ': 'aax', 'ậ': 'aaj',
        'é': 'es', 'è': 'ef', 'ẻ': 'er', 'ẽ': 'ex', 'ẹ': 'ej',
        'ê': 'ee', 'ế': 'ees', 'ề': 'eef', 'ể': 'eer', 'ễ': 'eex', 'ệ': 'eej',
        'í': 'is', 'ì': 'if', 'ỉ': 'ir', 'ĩ': 'ix', 'ị': 'ij',
        'ó': 'os', 'ò': 'of', 'ỏ': 'or', 'õ': 'ox', 'ọ': 'oj',
        'ô': 'oo', 'ố': 'oos', 'ồ': 'oof', 'ổ': 'oor', 'ỗ': 'oox', 'ộ': 'ooj',
        'ơ': 'ow', 'ớ': 'ows', 'ờ': 'owf', 'ở': 'owr', 'ỡ': 'owx', 'ợ': 'owj',
        'ú': 'us', 'ù': 'uf', 'ủ': 'ur', 'ũ': 'ux', 'ụ': 'uj',
        'ư': 'uw', 'ứ': 'uws', 'ừ': 'uwf', 'ử': 'uwr', 'ữ': 'uwx', 'ự': 'uwj',
        'ý': 'ys', 'ỳ': 'yf', 'ỷ': 'yr', 'ỹ': 'yx', 'ỵ': 'yj',
        'đ': 'dd'
    }

    # Thay thế các ký tự có dấu bằng ký tự không dấu
    for with_diacritic, without_diacritic in conversion_dict.items():
        text = text.replace(with_diacritic, without_diacritic)

    return text

# Ví dụ sử dụng
input_text = input('Nhập vào dữ liệu: ')
input_text = input_text.lower()
output_text = convert_with_diacritics_to_without(input_text)
print(output_text)


for char in output_text:
    
    keyboard.press(f'{char}')
    keyboard.release(f'{char}')
    time.sleep(0.07) 