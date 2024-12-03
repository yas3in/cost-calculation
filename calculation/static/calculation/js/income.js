const usernameInput = document.getElementById('income');

    // تنظیم پیام خطای سفارشی
    usernameInput.addEventListener('invalid', function () {
      if (!usernameInput.value) {
        usernameInput.setCustomValidity('لطفاً این فیلد را پر کنید.');
      } else {
        usernameInput.setCustomValidity(''); // پیام خطا را پاک می‌کند.
      }
    });

    // پاک کردن پیام خطا هنگام وارد کردن اطلاعات صحیح
    usernameInput.addEventListener('input', function () {
      usernameInput.setCustomValidity('');
    });